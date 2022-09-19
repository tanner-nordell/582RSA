import random
from rsa_util import mod_inverse
from rsa_util import is_prime

#The encryption exponent, e
#Do not change this value
e = 65537

def RSAKeygen(bitlen):
	n = 0
	d = 0
	while not is_prime(n):
		n = random.SystemRandom().randint(pow(2,bitlen-1), pow(2, bitlen)-1)
	while not is_prime(d):
		d = random.SystemRandom().randint(pow(2,bitlen-1), pow(2, bitlen)-1)

	return n,d

def RSAEncrypt(n,m):
	e = 65537
	c = pow(m,e,n)
	#Code goes here
	return c

def RSADecrypt(n,d,c):
	m = pow(c,d,n)
	#Code goes here
	return m

