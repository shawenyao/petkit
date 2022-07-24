import requests
import datetime
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()
username = os.environ.get('username')
password = os.environ.get('password')

# new session
s = requests.Session()

# login
headers = {
    'User-Agent': 'okhttp/3.12.1',
    'X-Api-Version': '7.29.1',
    'X-Client': 'Android(7.1.1;Xiaomi)',
    'Accept-Language': 'en-US,en;'
}
response_login = s.get(f'https://api.petkt.com/latest/user/login?username={username}&password={password}', headers=headers)

# get device info
headers['X-Session'] = response_login.json()['result']['session']['id']
response_device = s.get('https://api.petkt.com/latest/discovery/device_roster', headers=headers)

# feed
response_feed = s.get(
    f"http://api.petkt.com/latest/feedermini/save_dailyfeed?deviceId={response_device.json()['result']['devices'][0]['data']['id']}&day={datetime.datetime.today().strftime('%Y%m%d')}&time=-1&amount=5",
     headers=headers
)

# close session
s.close()
