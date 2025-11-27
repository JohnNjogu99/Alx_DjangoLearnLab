from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book, Author


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers CRUD operations and permission scenarios.
    """

    def setUp(self):
        # Create a test user and log them in
        self.user = User.objects.create_user(username="john", password="password123")
        self.client.login(username="john", password="password123")

        # Create an Author instance
        self.author = Author.objects.create(name="Author A")

        # Create a Book linked to that Author
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            publication_year=2020
        )

    def test_create_book(self):
        """Ensure we can create a book and it is saved correctly."""
        new_author = Author.objects.create(name="Author B")
        data = {"title": "New Book", "author": new_author.id, "publication_year": 2021}
        response = self.client.post("/api/books/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_get_book(self):
        """Ensure we can retrieve a book by ID."""
        response = self.client.get(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_update_book(self):
        """Ensure we can update a book and changes are reflected."""
        data = {"title": "Updated Book"}
        response = self.client.patch(f"/api/books/{self.book.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book")

    def test_delete_book(self):
        """Ensure we can delete a book and it is removed from the database."""
        response = self.client.delete(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_permission_denied_for_unauthenticated_user(self):
        """Ensure unauthenticated users cannot create, update, or delete books."""
        self.client.logout()
        data = {"title": "Fail Book", "author": self.author.id, "publication_year": 2022}
        response = self.client.post("/api/books/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)