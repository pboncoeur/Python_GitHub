# -*- coding: utf-8 -*-
"""Practical1_webscraping.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GdAHYeUU_nSote4c9m5z5lKwxGQRMKpB
"""

import requests
from bs4 import BeautifulSoup

url = "https://pythonscraping.com/linkedin/ietf.html"

response = requests.get(url)
print("Response from url: \n", response)

print("HTTP status code: ", response.status_code)

print("The extracted information: \n\n")
print(response.text) 
