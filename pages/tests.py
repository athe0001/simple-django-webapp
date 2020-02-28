from django.test import SimpleTestCase

# Create your tests here.

class PagesTests(SimpleTestCase):
    def test_hello_world_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)