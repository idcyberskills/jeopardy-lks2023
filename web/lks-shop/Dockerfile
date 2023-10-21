FROM faishol27/gunicorn:latest

COPY src/web/requirements.txt .
RUN apk --no-cache add py3-pip python3-dev sqlite && \
    pip3 install -r requirements.txt && rm requirements.txt && \
    apk del py3-pip python3-dev

ENV GUNICORN_WSGI_MODULE=web.wsgi:application
COPY src/web/ .
RUN chmod +x *.sh && \
    mv nginx.conf /etc/nginx/nginx.conf

# SQLite read-only solving trick
RUN mkdir -m 777 db
RUN python3 manage.py migrate
RUN chmod -R 777 db

RUN mkdir -p -m 777 /var/www/html/static/image/photo/

ENTRYPOINT ["./start.sh"]