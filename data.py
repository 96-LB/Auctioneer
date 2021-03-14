import gspread, base64, os

sizes = {}

with open('auth.json', 'w', encoding='utf-8') as f: 
    f.write(base64.b64decode(os.getenv('AUTH')).decode('utf-8'))
client = gspread.service_account('auth.json')
os.remove('auth.json')
sheet = client.open_by_key(os.getenv('SHEET')).worksheet(os.getenv('WORKSHEET'))

def get():
    return sheet.get_all_values()

def set(value):
    return sheet.update('B1', [[value]])