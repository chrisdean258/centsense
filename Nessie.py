import requests
import json
from Keys import key as apiKey


class Customer:
    def __init__(self, ID):
        url = 'http://api.reimaginebanking.com/customers/{}?key={}'.format(ID,apiKey)
        person = requests.get(url)
        self.good = True;
        if(person.status_code // 100 == 4):
            self.good = False
            return;
        json_data = json.loads(person.text);
        self.parse_dict(json_data)

    def __init(self):
        self.good = True

    @staticmethod
    def get_all():
        customers = []
        url = "http://api.reimaginebanking.com/customers?key={}".format(apiKey)
        people = requests.get(url)
        if(people.status_code // 400 == 4):
            return []
        json_data = json.loads(people.text)
        for i, person in enumerate(json_data):
            newPerson = Customer;
            self.parse_dict(person)
            customers.append(newPerson)
        return customers

    def parse_dict(self, d):
        self.ID = d["_id"]
        self.first_name = d["first_name"]
        self.last_name = d["last_name"]
        self.zip = d["address"]["zip"]
        self.street_number = d["address"]["street_number"]
        self.state = d["address"]["state"]
        self.city = d["address"]["city"]
        self.street_name = d["address"]["street_name"]

class Account:
    def __init__(self, accID):
        url = "http://api.reimaginebanking.com/accounts/{}?key={}".format(accID, apiKey)
        person = requests.get(url)
        self.good = True
        if(person.status_code == 404):
            self.good = False
            return
        json_data = json.loads(person.text);
        self.accID = json_data["_id"]
        self.type = json_data["type"]
        self.balance = json_data["balance"]
        self.nickname = json_data["nickname"]
        self.rewards = json_data["rewards"]
        self.custID = json_data["customer_id"]



accID = "5828d214360f81f104553cd0"
Account(accID)



class Transfer:
    def __init__(self, ID):
        url = "http://api.reimaginebanking.com/accounts/{}/transfers?key={}".format(ID, apiKey)
        transfer = requests.get(url)
        if(transfer.status_code // 100 == 4):
            self.goof = False
            return
        json_data = json.loads(transfer.text)
        parse_dict(json_data)

    def parse_dict(self, d):
        self.id = d["_id"]
        self.type = d["type"]
        self.transaction_date = d["transaction_date"]
        self.status = d["status"]
        self.medium = d["medium"]
        self.payer_id = d["payer_id"]
        self.payee_id = d["payee_id"]
        self.amount = d["amount"]
        self.description = d["description"]

