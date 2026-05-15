#!/usr/bin/env python3

import requests

url = "http://domain_name.com/uploads"

# Keys are the name of the form fields && values are in bytes.

test_files =  {
  "file_1" : open("file_name1.txt", "rb"),
  "file_2" : open("file_name2.txt", "rb"),
  "file_3" : open("file_name3.txt", "rb")
}

response = requests.post(url, files = test_files)

if response.ok:
  print("File Uploaded Successfully")
  print(response.text)
else:
  print("There was an problem uploading the file.")
 
