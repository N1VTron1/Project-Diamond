import unittest
import app1

class app1UnitTests(unittest.TestCase):

	def test_start_connection(self):
		app1.start_connection()


if __name__ == '__main__':
	unittest.main()
	print("All tests passed")
