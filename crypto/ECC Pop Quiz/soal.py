from Crypto.Util.number import *
import random
from libnum.ecc import *
import signal

def handle_timeout(signum, frame):
    print("Too Slow!")
    exit()

signal.signal(signal.SIGALRM, handle_timeout)

def gen_curve():
    p = getPrime(512)
    a = random.randint(1, p)
    b = random.randint(1, p)

    E = Curve(a, b, p)
    return E, p, a, b

def verify_ans(answer):
    try:
        ans = int(input("answer: "))
        if ans == answer:
            print("correct!")
        else:
            print("wrong!")
            exit()
    except Exception as e:
        print("wrong!")
        exit()

signal.alarm(8)
E,p,a,b = gen_curve()
P = list(E.find_points_rand(1)[0])[0]
x, y = P
print("Curve: y^2 = x^3 + ax + b (mod p)")
print(f"p = {p}")
print(f"a = {a}")
print(f"b = {b}")
print(f"x = {x}")
print(f"y = ???")

verify_ans(y)

E,p,a,b = gen_curve()
P = list(E.find_points_rand(1)[0])[0]
x, y = P

print("Curve: y^2 = x^3 + ax + b (mod p)")
print(f"p = {p}")
print(f"a = {a}")
print(f"x = {x}")
print(f"y = {y}")
print(f"b = ???")

verify_ans(b)

E,p,a,b = gen_curve()
P = list(E.find_points_rand(1)[0])[0]
x, y = P

print("Curve: y^2 = x^3 + ax + b (mod p)")
print(f"p = {p}")
print(f"x = {x}")
print(f"y = {y}")
print(f"b = {b}")
print(f"a = ???")

verify_ans(a)

E,p,a,b = gen_curve()
P = list(E.find_points_rand(1)[0])[0]
P2 = list(E.find_points_rand(1)[0])[0]
x, y = P
x1, y1 = P2
print("Curve: y^2 = x^3 + ax + b (mod p)")
print(f"p = {p}")
print(f"x1 = {x}")
print(f"y1 = {y}")
print(f"x2 = {x1}")
print(f"y2 = {y1}")
print(f"a = ???")
verify_ans(a)
print(f"b = ???")
verify_ans(b)

print(open("flag.txt").read())