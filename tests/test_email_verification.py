import os
import sys

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.email_verification import verify_email

def test_email_verification():
    # Test valid emails
    assert verify_email("test@example.com"), "Valid email verification failed!"
    assert verify_email("user.name@domain.co.uk"), "Valid email verification failed!"
    
    # Test invalid emails
    assert not verify_email("invalid.email"), "Invalid email check failed!"
    assert not verify_email("@domain.com"), "Invalid email check failed!"
    
    print("All email verification tests passed!")

test_email_verification()