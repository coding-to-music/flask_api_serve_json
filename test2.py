#!/usr/bin/env python3

import requests
import pandas as pd
response = requests.get("http://localhost:5000/holidays")
df = pd.DataFrame(response.json())
print(df)
