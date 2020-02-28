from django.test import TestCase

from .models import Post


# Create your tests here.
class PostModelTest(TestCase):

    def test_post_page(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_text_content(self):
        test_string = 'test'
        test_string_with_special_character = 'tést^'

        Post.objects.create(text=test_string)
        Post.objects.create(text=test_string_with_special_character)

        self.assertEqual(f'{Post.objects.get(id=1).text}', test_string)
        self.assertEqual(f'{Post.objects.get(id=2).text}', test_string_with_special_character)