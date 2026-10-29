import re

from django.test import Client, TestCase
from django.urls import reverse

from .models import Product


class ProductDeleteModalTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test shirt",
            stock_keep_unit="TEST-SHIRT-001",
            supplier="Test supplier",
            quantity=3,
            price=12.5,
        )
        self.client = Client(enforce_csrf_checks=True)

    def test_product_list_renders_delete_modal_and_csrf_token(self):
        response = self.client.get(reverse("product_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            f'data-bs-target="#deleteProductModal{self.product.product_id}"',
        )
        self.assertContains(
            response,
            f'id="deleteProductModal{self.product.product_id}"',
        )
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_delete_requires_post_and_valid_csrf_token(self):
        delete_url = reverse("product_del", args=[self.product.product_id])

        self.assertEqual(self.client.get(delete_url).status_code, 405)

        list_response = self.client.get(reverse("product_list"))
        token = re.search(
            rb'name="csrfmiddlewaretoken" value="([^"]+)"',
            list_response.content,
        )
        self.assertIsNotNone(token)

        response = self.client.post(
            delete_url,
            {"csrfmiddlewaretoken": token.group(1).decode()},
        )

        self.assertRedirects(response, reverse("product_list"))
        self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())
