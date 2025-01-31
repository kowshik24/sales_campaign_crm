from utils.google_sheets import get_google_sheet
from utils.email_verification import verify_email
import time

def process_leads():
    try:
        print("Connecting to Google Sheet...")
        sheet = get_google_sheet()
        print("Successfully connected to Google Sheet")
        
        print("Fetching leads...")
        leads = sheet.get_all_records()
        print(f"Found {len(leads)} leads")
        
        for i, lead in enumerate(leads):
            print(f"\nProcessing lead {i+1}/{len(leads)}: {lead['Lead Name']}")
            if lead["Email Verified"] == "Pending":
                print(f"Verifying email: {lead['Email']}")
                is_valid = verify_email(lead["Email"])
                result = "Y" if is_valid else "N"
                print(f"Email verification result: {result}")
                
                # Add a small delay to avoid rate limiting
                time.sleep(1)
                
                # Update is made to row i+2 because row 1 is header
                sheet.update_cell(i+2, 6, result)
            else:
                print(f"Email already verified: {lead['Email Verified']}")

        print("\nAll leads processed!")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print("\nPlease verify:")
        print("1. The credentials file exists and is valid")
        print("2. The Google Sheet is shared with the service account email")
        print("3. The Google Sheet name 'Sales Campaign CRM' is correct")

if __name__ == "__main__":
    process_leads()