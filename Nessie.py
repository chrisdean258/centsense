import requests
import json
from Keys import key as apiKey


class Customer:
    def __init__(self, ID):
        url = 'http://api.reimaginebanking.com/customers/{}?key={}'.format(ID,apiKey)
        person = requests.get(url)
        if(person.status_code == 404):
            self.good = False
            return;
        json_data = json.loads(person.text);
        self.ID = json_data["_id"]
        self.first_name = json_data["first_name"]
        self.last_name = json_data["last_name"]
        self.zip = json_data["address"]["zip"]
        self.street_number = json_data["address"]["street_number"]
        self.state = json_data["address"]["state"]
        self.city = json_data["address"]["city"]
        self.street_name = json_data["address"]["street_name"]



ID = "59fe1e3cb390353c953a1c2c"
Customer(ID)
