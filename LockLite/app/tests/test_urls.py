from django.test import TestCase


class TestsUrls(TestCase):
	def setUp(self):
		pass

	def test_login(self):
		hello = 'hello'
		self.assertEqual(hello, 'hello')
