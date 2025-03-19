import os
import django
import requests

# Manually set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from django.conf import settings  # Now settings can be accessed

# Aidbox Credentials
AIDBOX_URL = settings.AIDBOX_URL
AIDBOX_USERNAME = settings.AIDBOX_USERNAME
AIDBOX_PASSWORD = settings.AIDBOX_PASSWORD

# Test Aidbox Connection
def test_aidbox():
    response = requests.get(AIDBOX_URL, auth=(AIDBOX_USERNAME, AIDBOX_PASSWORD))
    
    if response.status_code == 200:
        print("✅ Aidbox is running successfully!")
    else:
        print(f"❌ Failed to connect to Aidbox: {response.status_code} - {response.text}")

test_aidbox()
