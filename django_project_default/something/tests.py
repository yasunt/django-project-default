from django.test import TestCase

from .views import ObjectCreateView, ObjectDeleteView, ObjectUpdateView


class SomethingViewsTest(TestCase):

    def setUp(self):
        pass

    def test_create_view_with_permission(self):
        self.assertTrue(False)

    def test_update_view_with_permission(self):
        self.assertTrue(False)

    def test_delete_view_with_permission(self):
        self.assertTrue(False)

    def test_create_view_without_permission(self):
        self.assertTrue(False)

    def test_update_view_without_permission(self):
        self.assertTrue(False)

    def test_delete_view_without_permission(self):
        self.assertTrue(False)
