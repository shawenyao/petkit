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
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;'
}
response_login = s.get(f'https://api.petkt.com/latest/user/login?username={username}&password={password}', headers=headers)

# get device info
headers['X-Session'] = response_login.json()['result']['session']['id']
response_device = s.get('https://api.petkt.com/latest/discovery/device_roster', headers=headers)

# feed
device_id = response_device.json()['result']['devices'][0]['data']['id']
day = datetime.datetime.today().strftime('%Y%m%d')
amount = 5 # smallest amount
response_feed = s.get(
    f"http://api.petkt.com/latest/feedermini/save_dailyfeed?deviceId={device_id}&day={day}&time=-1&amount={amount}",
    headers=headers
)

# close session
s.close()
