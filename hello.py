#!/usr/bin/env python3
"""
CMPUT404 Winter2021 Lab3
Gengyuan Huang

This program is written by Zoe Riell
"""


import os
import json


# print env variables as json
print("Content-Type: application/json")
print()
print(json.dumps(dict(os.environ), indent=2))

# # print query parameter data in html
# print("Content-Type: text/html")
# print()
# print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")



