from utils.google_sheets import get_google_sheet
from utils.email_sender import send_email
import time
from datetime import datetime

def outreach_leads():
    try:
        print("Connecting to Google Sheet...")
        sheet = get_google_sheet()
        print("Successfully connected to Google Sheet")
        
        print("Fetching leads...")
        leads = sheet.get_all_records()
        stats = {"sent": 0, "skipped": 0, "failed": 0}
        print(f"Found {len(leads)} leads")
        
        for i, lead in enumerate(leads):
            print(f"\nProcessing lead {i+1}/{len(leads)}: {lead['Lead Name']}")
            
            # Modify conditions to handle more cases
            should_send = (
                lead["Email Verified"] == "Y" and 
                lead["Response Status"] not in ["Converted", "Not Interested", "Sent", "Awaiting Response"]
            )
            
            if should_send:
                try:
                    print(f"Sending email to: {lead['Email']}")
                    response = send_email(lead["Email"], lead["Lead Name"], lead["Company"])
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    if response == "Sent":
                        stats["sent"] += 1
                        sheet.update_cell(i+2, 7, "Awaiting Response")
                        sheet.update_cell(i+2, 8, f"Email sent on {timestamp}")
                        print(f"✓ Email successfully sent to {lead['Email']}")
                    else:
                        stats["failed"] += 1
                        sheet.update_cell(i+2, 7, "Failed")
                        sheet.update_cell(i+2, 8, f"Failed to send email on {timestamp}")
                        print(f"✗ Failed to send email to {lead['Email']}")
                    
                    time.sleep(2)  # Rate limiting
                    
                except Exception as e:
                    print(f"Error processing lead {lead['Email']}: {str(e)}")
                    stats["failed"] += 1
            else:
                stats["skipped"] += 1
                skip_reason = "unverified email" if lead["Email Verified"] != "Y" else (
                    f"status is '{lead['Response Status']}'"
                )
                print(f"Skipping lead - {skip_reason}")
    
        print("\nCampaign Summary:")
        print(f"Total Leads: {len(leads)}")
        print(f"Emails Sent: {stats['sent']}")
        print(f"Leads Skipped: {stats['skipped']}")
        print(f"Failures: {stats['failed']}")
        
        if stats["sent"] == 0:
            print("\nNo emails were sent because:")
            print("1. Leads must have Email Verified = 'Y'")
            print("2. Response Status must not be 'Converted', 'Not Interested', 'Sent', or 'Awaiting Response'")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    outreach_leads()