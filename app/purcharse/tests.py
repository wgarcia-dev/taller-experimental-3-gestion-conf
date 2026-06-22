from django.test import TestCase

from app.core.models import Supplier
from app.purcharse.models import Purchase


class PurchaseModelTests(TestCase):
    def test_purchase_delete_marks_record_inactive(self):
        supplier = Supplier.objects.create(
            name="Proveedor prueba",
            ruc="0916517791",
            phone="0999999999",
            address="Centro",
            latitude="-2.17",
            longitude="-79.90",
        )
        purchase = Purchase.objects.create(
            num_document="001-001-000000001",
            supplier=supplier,
        )

        purchase.delete()
        purchase.refresh_from_db()

        self.assertFalse(purchase.active)
        self.assertIn("001-001-000000001", str(purchase))
