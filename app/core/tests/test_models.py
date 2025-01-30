"""
<<<<<<< HEAD
tests for models
"""
=======
Tests for models.
"""
from decimal import Decimal
>>>>>>> 11a424c09313af2d3ebfccd2f858b976cb12a05b

from django.test import TestCase
from django.contrib.auth import get_user_model

<<<<<<< HEAD

class ModelTests(TestCase):
    # test models

    def test_create_user_with_email_successful(self):
        # test create a user with an email is successful
=======
from core import models


def create_user(email='user@example.com', password='testpass123'):
    """Create a return a new user."""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
>>>>>>> 11a424c09313af2d3ebfccd2f858b976cb12a05b
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
<<<<<<< HEAD
            password = password,
=======
            password=password,
>>>>>>> 11a424c09313af2d3ebfccd2f858b976cb12a05b
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
<<<<<<< HEAD
        # test user email is normalised for new users
=======
        """Test email is normalized for new users."""
>>>>>>> 11a424c09313af2d3ebfccd2f858b976cb12a05b
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
<<<<<<< HEAD
=======
        """Test that creating a user without an email raises a ValueError."""
>>>>>>> 11a424c09313af2d3ebfccd2f858b976cb12a05b
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
<<<<<<< HEAD
        # tests setting up a super user
=======
        """Test creating a superuser."""
>>>>>>> 11a424c09313af2d3ebfccd2f858b976cb12a05b
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
<<<<<<< HEAD
=======

    def test_create_recipe(self):
        # test create a recipe is successful
        user = get_user_model().objects.create_user(
            'test@example.com', 'testpass123'
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title='sample recipe name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample recipe description'
        )

        self.assertEqual(str(recipe), recipe.title)
>>>>>>> 11a424c09313af2d3ebfccd2f858b976cb12a05b
