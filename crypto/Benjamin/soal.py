from Crypto.Util.number import getPrime, bytes_to_long
import random

p = getPrime(512)
q = getPrime(512)
N = p*q
a = random.randint(1, p)
b = random.randint(1, q)
m = bytes_to_long(open('flag.txt', 'rb').read())
assert m**3 > N
assert m*123 + (a*b) < N
assert m*a + (b*1337) < N

c1 = pow(m*123 + (a*b), 7, N)
c2 = pow(m*a + (b*1337), 3, N)

print(f"{N = }")
print(f"{a = }")
print(f"{b = }")
print(f"{c1 = }")
print(f"{c2 = }")
