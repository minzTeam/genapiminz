# REST API | TOKEN GENERATOR

### APIKEY REQUIRED
You need <a href="https://gen.minzteam.xyz">apikey</a> to get the response

### EXAMPLE REQUEST
Use genapiminz.py
```python
from genapiminz import *

api = GenTokenMachine("YOUR APIKEY")

result = api.generateNumber(number="+91xxxxxxx", name="Minz Team")
'''Note:
- You Must Use India Number
- 1 Request Generate Token Balance: 2000
'''
if result["STATUS"] == "OK":
  api_result = api.generateToken(id=result["message"]["id"], pincode="123456")
  api.print_result(api_result)
```
Python Language
```python
import requests, json

params = {
  "apikey": "YOUR APIKEY",
  "number": "+91xxxxxxx",
  "name": "Minz Team"
}
api = requests.get("https://gen.minzteam.xyz/getnumber", params=params).json()

if api["STATUS"] == "OK":
  params = {
    "apikey": "YOUR APIKEY",
    "id": api["message"]["id"],
    "pincode": "123456"
  }
  result = requests.get("https://gen.minzteam.xyz/getpincode", params=params).json()
  print(result)
```

### CONTACT US
<a href="https://line.me/ti/p/~visss.">CREATOR</a>

### SUPPORTED BY
* Alm. ZeroCool
* Phantom Coder
* Superline Project
* Vnyll Teambot
* Talk Exception
