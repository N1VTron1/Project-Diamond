import unittest
import app2
import hashlib,hmac, base64
import urllib.request, urllib.parse
import json

class app2UnitTests(unittest.TestCase):

	#s = (app2.set_connection())
	#print(s)

	#def test(self):
	#	self.assertEqual(s, "<ssl.SSLSocket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8080)>")


	def test_hash_payload(self):
		jsonPayload = '{"Hello" : "World"}'
		jsonHash = app2.hash_payload(jsonPayload)
		self.assertEqual(jsonHash,"cd460a5a26d4e03a4f7022dae10e64cea9e30f291fb2dfa70eefb17063f63d6c")



if __name__ == '__main__':
    unittest.main()

