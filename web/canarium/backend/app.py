import os
import secrets
from flask import Flask, render_template, render_template_string, redirect, request, session, url_for
from flask_session import Session
from database.DBManager import DBManager
from werkzeug.wrappers import Request, Response, ResponseStream
import datetime

server = Flask(__name__, static_folder='public', static_url_path='')
server.config["SESSION_PERMANENT"] = False
server.config["SESSION_TYPE"] = "filesystem"
server.secret_key = os.environ['SECRET_KEY']
conn = None

def render_template_from_html(template_file, **args):
    def sanitize(data):
        if not data:
            data = "<b>empty.</b>"

        data = data.replace('\'', '').replace('*', '')
        banning = ['self', 'config', 'request']

        for b in banning:
            if b in data:
                data = "<b>halting. dangerous token detected.</b>"

        return data
    
    args = {x: sanitize(y) for (x,y) in args.items()}
    
    with open('./templates/{}'.format(template_file), 'r') as f:
        return render_template_string(f.read().format(**args))

@server.before_request
def before_request():
    global conn
    if not conn:
        conn = DBManager(password_file='/run/secrets/db-password')
        conn.populate_db()

    user_agent = request.headers.get('User-Agent')
    ip_address = get_user_ip_address(request)

    if not session.get("canary_id"):
        set_canary_session(user_agent, ip_address)
    else:
        canary_id = session.get("canary_id")
        canary = conn.query_canary_entry(canary_id)
        if not canary:
            set_canary_session(user_agent, ip_address)
        else:
            canary_blacklist = conn.query_canary_blacklist(canary_id)

            if canary_blacklist and request.endpoint != 'display_warning':
                return redirect(url_for('display_warning'))
    
def get_user_ip_address(request):
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
    else:   
        return request.environ['HTTP_X_FORWARDED_FOR']
    
def set_canary_session(user_agent, ip_address):
    global conn
    can_id = secrets.token_hex(nbytes=16)
    session['canary_id'] = can_id

    return conn.cursor.execute("INSERT INTO canary (canary_id, user_agent, ip_address) VALUES (%s, %s, %s);", (can_id, user_agent, ip_address))

def get_canary_session(canary_id):
    global conn

    canary = conn.query_canary_entry(canary_id)    
    return canary

@server.route('/health/<canary_id>')
def ban_user(canary_id):
    global conn

    canary = get_canary_session(canary_id)
    conn.cursor.execute("INSERT INTO canary_blacklist (canary_id, since, is_valid) VALUES (%s, %s, %s);", (canary_id, datetime.datetime.now(), True))

    return redirect(url_for('display_warning'))

@server.route('/oops')
def display_warning():
    global conn

    canary_id = session.get('canary_id')
    canary = get_canary_session(canary_id)

    canary['ip_address'] = get_user_ip_address(request)
    canary['user_agent'] = request.headers.get('User-Agent')

    if not session.get('warning_count'):
        session['warning_count'] = 1
    else:
        session['warning_count'] = session.get('warning_count') + 1

    canary_blacklist = conn.query_canary_blacklist(canary_id)
    if not canary_blacklist:
        return redirect(url_for('list_blog'))
    else:
        if session.get('warning_count') <= 3:
            return render_template_from_html('warning.html', canary_id=canary_id, ip_address=canary['ip_address'], user_agent=canary['user_agent'])
        else:
            message = "No data is shown as you have ignores the previous 3 warnings. Ckckck."
            return render_template_from_html('warning.html', canary_id=message, ip_address=message, user_agent=message)

@server.route('/')
def list_blog():
    global conn
    posts = conn.query_titles()

    canary_id = session.get("canary_id")
    canary_link = "{}health/{}".format("http://13.212.234.124:16161/", get_canary_session(canary_id)['canary_id'])

    return render_template('index.html', canary_link=canary_link, posts=posts)

if __name__ == '__main__':
    server.run()