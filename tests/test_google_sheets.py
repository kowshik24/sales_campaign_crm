import os
import sys

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.google_sheets import get_google_sheet

def test_google_sheet():
    sheet = get_google_sheet()
    assert sheet is not None, "Google Sheet connection failed!"
    print("Google Sheet connection successful!")

test_google_sheet()