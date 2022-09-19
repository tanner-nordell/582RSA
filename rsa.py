import random
from rsa_util import mod_inverse
from rsa_util import is_prime

#The encryption exponent, e
#Do not change this value
e = 65537

def RSAKeygen(bitlen):
	n = 0
	d = 0
	p = 0
	q = 0
	while not is_prime(p):
		p = random.SystemRandom().randint(pow(2,bitlen-1), pow(2, bitlen)-1)
	while not is_prime(q):
		q = random.SystemRandom().randint(pow(2,bitlen-1), pow(2, bitlen)-1)
	n=p*q
	phiN = (p-1)(q-1)
	d = mod_inverse(e, phiN)
	return n,d

def RSAEncrypt(n,m):
	c = pow(m,e,n)
	#Code goes here
	return c

def RSADecrypt(n,d,c):
	m = pow(c,d,n)
	#Code goes here
	return m

