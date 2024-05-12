from unittest.mock import MagicMock, patch

from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase

from .forms import RememberForm
from .models import Remember
from .views import (
    RememberCreateView,
    RememberDeleteView,
    RememberListView,
    RememberUpdateView,
)


class RememberListViewTest(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="test", password="test")

    def test_get(self) -> None:
        Remember.objects.create(
            user=self.user,
            title="Test Title 1",
            comment="Test Comment 1",
            location="SRID=4326;POINT (0 0)",
        )
        Remember.objects.create(
            user=self.user,
            title="Test Title 2",
            comment="Test Comment 2",
            location="SRID=4326;POINT (0 0)",
        )
        Remember.objects.create(
            user=self.user,
            title="Test Title 3",
            comment="Test Comment 3",
            location="SRID=4326;POINT (0 0)",
        )

        request = self.factory.get("/remembers")
        request.user = self.user

        response = RememberListView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context_data["remembers"]),
            list(Remember.objects.filter(user=self.user)),
        )


class RememberCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="test", password="test")

    @patch.object(RememberForm, "is_valid")
    @patch.object(RememberForm, "save")
    def test_form_valid(
        self, mock_save: MagicMock, mock_is_valid: MagicMock
    ) -> None:
        mock_is_valid.return_value = True
        mock_save.return_value = Remember()

        request = self.factory.post("/remembers/new")
        request.user = self.user

        response = RememberCreateView.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/remembers/")


class RememberUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="test", password="test")
        self.remember = Remember.objects.create(
            user=self.user,
            title="Test Title",
            comment="Test Comment",
            location="SRID=4326;POINT (0 0)",
        )

    @patch.object(RememberForm, "is_valid")
    @patch.object(RememberForm, "save")
    def test_form_valid(
        self, mock_save: MagicMock, mock_is_valid: MagicMock
    ) -> None:
        mock_is_valid.return_value = True
        mock_save.return_value = self.remember

        request = self.factory.post(f"/remembers/{self.remember.id}")
        request.user = self.user

        response = RememberUpdateView.as_view()(request, pk=self.remember.id)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/remembers/")


class RememberDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="test", password="test")
        self.remember = Remember.objects.create(
            user=self.user,
            title="Test Title",
            comment="Test Comment",
            location="SRID=4326;POINT (0 0)",
        )

    def test_delete(self) -> None:
        request = self.factory.delete(f"/remembers/{self.remember.id}/delete")
        request.user = self.user

        response = RememberDeleteView.as_view()(request, pk=self.remember.id)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/remembers/")
        self.assertFalse(Remember.objects.filter(pk=self.remember.id).exists())
