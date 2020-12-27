from django.test import TestCase
from .models import Post
# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="Solo un texto")
        Post2.objects.create(text="Solo un texto 2")

    def test_text_content_1(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.text}"
        self.assertEqual(expected_object_name, "Solo un texto")

