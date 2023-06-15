import requests, json, threading

class GenTokenMachine(threading.Thread):
    def __init__(self, apikey):
        super(GenTokenMachine, self).__init__()
        self.base_url = "https://gen.minzteam.xyz"
        self.session = requests.Session()
        self.headers = apikey 

    def print_result(self, data):
        print(json.dumps(data, indent=4, sort_keys=True))

    def requestGet(self, path, params):
        main = self.session.get(self.base_url+path, params=params).json()
        return main

    def generateNumber(self, number="", name="", password=""):
        params = {"number": number, "name": name, "password": password , "apikey": self.headers}
        main = self.requestGet("/getnumber", params)
        return main
      
    def generateToken(self, id="", pincode=""):
        params = {"id": id, "pincode": pincode, "apikey": self.headers}
        main = self.requestGet("/getpincode", params)
        return main
