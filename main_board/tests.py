from django.test import TestCase
from django.test import Client
from main_board import models
# Create your tests here.


class Tests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.category = models.Category.objects.create(name='Политика')
        self.author = models.User.objects.create(
            username='TestAuthor',
            first_name='Test',
            last_name='Testovich',
        )
        self.news = models.NewsPost.objects.create(
            title='Lorem llll',
            body='lorem lorem lorem lorem lorem lorem',
            author=self.author,
            category=self.category,
        )

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get(f'/{self.news.created.year}'
                                   f'/{self.news.created.month}'
                                   f'/{self.news.created.day}'
                                   f'/{self.news.slug}/')
        self.assertEqual(response.status_code, 200)

    def test_category(self):
        response = self.client.get(f'/{self.category.slug}')
        self.assertEqual(response.status_code, 200)
