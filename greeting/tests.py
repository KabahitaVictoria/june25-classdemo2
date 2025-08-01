"""Test cases for the greeting app."""

from django.test import TestCase, Client
from django.urls import reverse


class GreetingTests(TestCase):
    """Tests for greeting view responses and templates."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    def test_index_page(self):
        """Test that index page returns correct status, template, and content."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello')
        self.assertTemplateUsed(response, 'index.html')

    def test_index_context_greeting(self):
        """Test that the greeting in context is 'Hello'."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.context['greeting'], 'Hello')
        