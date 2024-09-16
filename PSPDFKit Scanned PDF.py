# PSPDFKit API

import requests
import json

file_name = input("Please enter the file name: ")

instructions = {
  'parts': [
    {
      'file': 'scanned'
    }
  ],
  'actions': [
    {
      'type': 'ocr',
      'language': 'english'
    }
  ]
}

response = requests.request(
  'POST',
  'https://api.pspdfkit.com/build',
  headers = {
    'Authorization': 'Bearer pdf_live_3SxUghOiq0V2rWYUrBJuk6UPRCCCW8Tfjy4Yr7pLylu'
  },
  files = {
    'scanned': open(file_name, 'rb')
  },
  data = {
    'instructions': json.dumps(instructions)
  },
  stream = True
)

if response.ok:
  with open('result-scanned.pdf', 'wb') as fd:
    for chunk in response.iter_content(chunk_size=8096):
      fd.write(chunk)
else:
  print(response.text)
  exit()