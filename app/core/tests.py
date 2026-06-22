from decimal import Decimal

from django.test import TestCase

from app.core.models import (
    Brand,
    Category,
    Customer,
    Iva,
    Line,
    PaymentMethod,
    Product,
)


class CoreModelTests(TestCase):
    def test_customer_save_uppercases_names_and_full_name(self):
        customer = Customer.objects.create(
            first_name="ana",
            last_name="mora",
            latitude="-2.17",
            longitude="-79.90",
        )

        self.assertEqual(customer.first_name, "ANA")
        self.assertEqual(customer.last_name, "MORA")
        self.assertEqual(customer.get_full_name, "MORA ANA")

    def test_brand_delete_marks_record_inactive(self):
        brand = Brand.objects.create(description="Generica")

        brand.delete()
        brand.refresh_from_db()

        self.assertFalse(brand.active)

    def test_product_stock_helpers(self):
        product = self._create_product(stock=10)

        product.reduce_stock(3)
        product.refresh_from_db()

        self.assertEqual(product.stock, 7)
        self.assertEqual(str(product), "Producto prueba - 7")

    def test_product_reduce_stock_rejects_insufficient_stock(self):
        product = self._create_product(stock=2)

        with self.assertRaisesMessage(ValueError, "No hay suficiente stock disponible."):
            product.reduce_stock(3)

    def test_payment_method_delete_marks_record_inactive(self):
        payment_method = PaymentMethod.objects.create(description="Efectivo")

        payment_method.delete()
        payment_method.refresh_from_db()

        self.assertFalse(payment_method.active)

    def _create_product(self, stock):
        brand = Brand.objects.create(description="Marca prueba")
        iva = Iva.objects.create(description="IVA 12", value=Decimal("12.00"))
        line = Line.objects.create(description="Linea prueba")
        category = Category.objects.create(description="Categoria prueba")
        product = Product.objects.create(
            description="Producto prueba",
            brand=brand,
            cost=Decimal("1.00"),
            price=Decimal("2.00"),
            stock=stock,
            iva=iva,
            line=line,
        )
        product.categories.add(category)
        return product
