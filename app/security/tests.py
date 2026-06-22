from django.contrib.auth.models import Group
from django.test import TestCase

from app.security.models import Menu, Module, User


class SecurityModelTests(TestCase):
    def test_user_uses_email_as_login_identifier(self):
        user = User.objects.create_user(
            username="amora",
            email="ana@example.com",
            password="secret",
            first_name="Ana",
            last_name="Mora",
        )

        self.assertEqual(User.USERNAME_FIELD, "email")
        self.assertEqual(user.get_full_name, "Ana Mora")
        self.assertEqual(user.get_short_name(), "amora")
        self.assertEqual(user.get_image(), "/static/img/usuario_anonimo.png")

    def test_module_defaults_and_string_representation(self):
        menu = Menu.objects.create(name="Ventas", icon="")
        module = Module.objects.create(
            menu=menu,
            name="Facturas",
            url="/sales/invoices/",
        )

        self.assertEqual(menu.get_icon(), "bi bi-calendar-x-fill")
        self.assertEqual(module.get_icon(), "bi bi-x-octagon")
        self.assertEqual(str(module), "Facturas [/sales/invoices/]")

    def test_user_groups_are_returned(self):
        group = Group.objects.create(name="Administradores")
        user = User.objects.create_user(
            username="admin",
            email="admin@example.com",
            password="secret",
            first_name="Admin",
            last_name="User",
        )
        user.groups.add(group)

        self.assertQuerySetEqual(user.get_groups(), [group])
