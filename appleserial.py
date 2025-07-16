# Apple Product Serial Lookup using *magic*
#
# Made by Sean Gustavson 2025
# MIT Lisense

import sys
import requests
testing = False

def debug(text):
    if testing:
        print(f"[debug] {text}")

if len(sys.argv) < 2:
    print("Usage: python appleserial.py <serial number>")
    debug(sys.argv)
    raise ValueError # it's cause u didn't give a serial number

serial_number = str(sys.argv[1]).upper()
if ' ' in serial_number:
    debug(serial_number)
    raise ValueError # why are there spaces here?

print(f"Serial Number: {serial_number}")

# curl 'https://www.apple.com/shop/tradein-module?sno=XXXXXXXXXX&cat=computer&bid=1&pid=133442&module=verify'

url = 'https://www.apple.com/shop/tradein-module'
params = {
    'sno': serial_number,
    'cat': 'computer',
    'bid': 1,
    'pid': -1,
    'module': 'verify'
}
try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")


