from django.conf import settings
from django.test.runner import DiscoverRunner


class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


class NoMigrationsTestRunner(DiscoverRunner):
    def setup_test_environment(self, **kwargs):
        super().setup_test_environment(**kwargs)
        self._old_migration_modules = getattr(settings, 'MIGRATION_MODULES', {})
        settings.MIGRATION_MODULES = DisableMigrations()

    def teardown_test_environment(self, **kwargs):
        settings.MIGRATION_MODULES = self._old_migration_modules
        super().teardown_test_environment(**kwargs)
