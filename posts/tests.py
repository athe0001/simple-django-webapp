from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.

test_string = 'test'
test_string_with_special_character = 'tést^'

def before():
    Post.objects.create(text=test_string)
    Post.objects.create(text=test_string_with_special_character)

class PostPageViewTest(TestCase):
    def test_post_page(self):
        before()
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_post_page_by_name(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)

    def test_post_page_correct_template(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post.html')

class PostModelTest(TestCase):
    def test_text_content(self):
        before()
        self.assertEqual(f'{Post.objects.get(id=1).text}', test_string)
        self.assertEqual(f'{Post.objects.get(id=2).text}', test_string_with_special_character)