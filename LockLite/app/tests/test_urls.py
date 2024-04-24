from django.test import TestCase
from django.urls import reverse, resolve


class TestsUrls(TestCase):
	def _test_url(self, route, kwargs=None):
		path = reverse(route)
		match = resolve(path, kwargs)
		self.assertEqual(match.view_name, route)

	def setUp(self):
		pass

	def test_login(self):
		self._test_url('login')

	def test_register(self):
		self._test_url('register')
