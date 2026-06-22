import os
import subprocess
import sys


def main():
    env = os.environ.copy()
    env.setdefault("DJANGO_SETTINGS_MODULE", "proy_sales.settings")

    command = [
        sys.executable,
        "manage.py",
        "test",
        "--verbosity=2",
    ]
    return subprocess.call(command, env=env)


if __name__ == "__main__":
    raise SystemExit(main())
