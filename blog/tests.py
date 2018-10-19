from django.test import TestCase

# Create your tests here.

from django.contrib.auth import get_user_model
from django.test import client, TestCase
from django.urls import reverse

from.models import Post

class BlogTests(TestCase):

    def setUp(self):
        self.user=get_user_model().object.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'

        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        Post = Post(title='A sample title')
        self.assertEqual(str(Post),Post.title)

    def test_Post_content(selfself):
        self.assertEqual(f'{self.Post.title}', 'A good title')
        self.assertEqual(f'{self.Post.author}', 'testuser')
        self.assertEqual(f'{self.Post.body}', 'Nice body content')


    def test_Post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Nice body content')
        self.assertTemplateUsed(response,'home.html')

    def test_Post_detail_view(self):
        response = self.client.get('/Post/1/')
        no_response = self.client.get('/Post/100000/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'Post_detail.html')

