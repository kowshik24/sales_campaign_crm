import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

def get_google_sheet():
    """
    Initialize and return Google Sheet connection with better error handling
    """
    try:
        scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']
        
        credentials_path = '/home/kowshik/personal_work/interview/sales_campaign_crm/sales-campaign-crm-c80cf7b8db1e.json'
        
        # Verify credentials file exists and is readable
        try:
            with open(credentials_path, 'r') as f:
                json.load(f)  # Validate JSON format
        except FileNotFoundError:
            raise Exception(f"Credentials file not found at {credentials_path}")
        except json.JSONDecodeError:
            raise Exception("Invalid JSON in credentials file")
            
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
        client = gspread.authorize(creds)
        
        # Try to open the specific sheet
        try:
            sheet = client.open("SalesCampaignCRM").sheet1
            # Verify connection by making a simple request
            sheet.row_count  # This will fail if we can't access the sheet
            return sheet
        except gspread.exceptions.SpreadsheetNotFound:
            raise Exception("Could not find 'SalesCampaignCRM' spreadsheet. Make sure it's shared with the service account email.")
        except gspread.exceptions.APIError as e:
            raise Exception(f"Google Sheets API error: {str(e)}")
            
    except Exception as e:
        raise Exception(f"Failed to connect to Google Sheets: {str(e)}")

# supervisor_agent.py
from utils.google_sheets import get_google_sheet

def assign_tasks():
    sheet = get_google_sheet()
    leads = sheet.get_all_records()
    for i, lead in enumerate(leads):
        if not lead["Email Verified"]:
            print(f"Assigning Lead {lead['Lead Name']} to Agent A")
            sheet.update_cell(i+2, 6, "Pending")  # Mark as pending verification
        elif not lead["Response Status"]:
            print(f"Assigning Lead {lead['Lead Name']} to Agent B")
            sheet.update_cell(i+2, 7, "Pending")  # Mark as pending outreach