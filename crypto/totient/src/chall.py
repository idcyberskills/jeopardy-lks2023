from Crypto.Util.number import getPrime, inverse
import gmpy2
import signal

signal.alarm(5)

flag = open('flag.txt').read()
p = getPrime(1024)
q = getPrime(1024)
N = p * q
totient = (p - 1) * (q - 1)
e = getPrime(128)
d = inverse(e, totient)

assert (e * d) % totient == 1

z = e * d - 1

print(f'{z = }')
print(f'{N = }')

try:
    ans = int(input('totient = ').strip())
    if ans == totient:
        print(flag)
except:
    print('error')