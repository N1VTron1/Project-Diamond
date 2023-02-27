import unittest
import app3
import urllib.request, urllib.parse
import json

class app3UnitTests(unittest.TestCase):

	"""
	Description: Performs unit test on App3 hash_payload method
	Expected Return: True
	"""
	def test_hash_payload(self):

		with open('receive/App1jsonFile.json', 'r') as f:
			payload = f.read()

		payload = str(payload)
		json_payload = (payload[0:(len(payload) - 64)]).strip()

		self.assertEqual(app3.hash_payload(json_payload), "26d0908288e6b81226dd4b8f7652e0265f157901c6d691984a902ef09391d626")

	"""
	Description: Performs unit test on App3 compare_hash method
	Expected Return: True
	"""

	def test_compare_hash(self):

		with open('receive/App1jsonFile.json', 'r') as f:
			payload = f.read()

		payload = str(payload)
		json_payload = (payload[0:(len(payload) - 64)]).strip()

		hash1 = app3.hash_payload(json_payload)
		hash2 = "26d0908288e6b81226dd4b8f7652e0265f157901c6d691984a902ef09391d626"

		self.assertEqual(hash1, hash2)

	"""
	Description: Performs unit test on App3 send_file_email method
	Expected Return: True
	"""

	def test_send_file_email(self):
		self.assertTrue(app3.send_file_email("aza5975@psu.edu"))

if __name__ == '__main__':
	unittest.main()
