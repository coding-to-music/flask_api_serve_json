#!/usr/bin/env python3

import requests
import json
response = requests.get("https://calendarific.com/api/v2/holidays?&api_key=YOUR_KEY&country=CA&year=2020")
with open('myfile.json', 'w') as json_file:
   json.dump(response.json(), json_file)
