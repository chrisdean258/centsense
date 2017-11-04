import requests
import json

apiKey = '1312ae9bf58b2fd71f6632fa9c23996e'



class Account:
    def __init__(self, ID):
        url = 'http://api.reimaginebanking.com/customers/{}?key={}'.format(ID,apiKey)
        person = requests.get(url)
        if(person.status_code == 404):
            self.good = False
            return;
        json_data = json.loads(person.text);
        self.ID = json_data["_id"]
        self.first_name = jason_data["first_name"]
        self.last_name = jason_data["last_name"]
        self.zip = jason_data["address"]["zip"]
        self.street_number = jason_data["address"]["street_number"]
        self.state = jason_data["address"]["state"]
        self.city = jason_data["address"]["city"]
        self.street_name = jason_data["address"]["street_name"]



ID = "59fe1e3cb390353c953a1c2c"
Account(ID)
