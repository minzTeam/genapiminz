# REST API | TOKEN GENERATOR

### APIKEY REQUIRED
You need <a href="https://api.minzteam.xyz">apikey</a> to get the response

### EXAMPLE REQUEST
Use genapiminz.py
```python
from genapiminz import *

api = GenTokenMachine("YOUR APIKEY")

result = api.generateNumber(number="087xxxxxxx", name="Minz Team", password="Minzteam123_")
'''Note:
- You Must Use Indonesian Number
- Password Must Include Item Below
  > Minimal 8 Charachter
  > Use Capitals, Number, And Symbol
'''
if result["STATUS"] == "OK":
  api_result = api.generateToken(id=result["id"], pincode="123456")
  api.print_result(api_result)
```

### CONTACT US
<a href="https://line.me/ti/p/~visss.">CREATOR</a>

### SUPPORTED BY
* Alm. ZeroCool
* Phantom Coder
* Superline Project
* Vnyll Teambot
* Talk Exception
