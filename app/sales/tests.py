from django.test import TestCase

from app.core.models import Customer, PaymentMethod
from app.sales.models import Invoice


class SalesModelTests(TestCase):
    def test_invoice_delete_marks_record_inactive(self):
        customer = Customer.objects.create(
            first_name="Ana",
            last_name="Mora",
            latitude="-2.17",
            longitude="-79.90",
        )
        payment_method = PaymentMethod.objects.create(description="Efectivo")
        invoice = Invoice.objects.create(
            customer=customer,
            payment_method=payment_method,
        )

        invoice.delete()
        invoice.refresh_from_db()

        self.assertFalse(invoice.active)
        self.assertIn("MORA ANA", str(invoice))
