from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="john", password="password123")
        self.client.login(username="john", password="password123")

        # Create an Author instance
        self.author = Author.objects.create(name="Author A")

        # Create a Book linked to that Author
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            publication_year=2020   # ✅ corrected field name
        )

    def test_create_book(self):
        new_author = Author.objects.create(name="Author B")
        data = {"title": "New Book", "author": new_author.id, "publication_year": 2021}  # ✅ corrected
        response = self.client.post("/api/books/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_get_book(self):
        response = self.client.get(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_update_book(self):
        data = {"title": "Updated Book"}
        response = self.client.patch(f"/api/books/{self.book.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book")

    def test_delete_book(self):
        response = self.client.delete(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_filter_books(self):
        response = self.client.get(f"/api/books/?author={self.author.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get("/api/books/?search=Test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Test Book")

    def test_order_books(self):
        response = self.client.get("/api/books/?ordering=publication_year")  # ✅ corrected
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data[0]["publication_year"] <= response.data[-1]["publication_year"])  # ✅ corrected

    def test_permission_denied_for_unauthenticated_user(self):
        self.client.logout()
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)