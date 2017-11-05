import requests
import json
from Keys import key as apiKey

class Customer:
    def __init__(self, ID):
        if(ID == ""):
            return
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
        for person in json_data:
            newPerson = Customer("");
            newPerson.parse_dict(person)
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

    def json(self):
        return '{ "_id": "' + self.ID + '", "first_name": "' + self.first_name + '", "last_name": "' + self.last_name + '", "address": { "street_number": "' + self.street_number + '", "street_name": "' + self.street_name + '", "city": "' + self.city + '", "state": "' + self.state + '", "zip": "' + self.zip + '" } }'

class Account:
    def __init__(self, accID):
        if(accID == ""):
            return
        url = "http://api.reimaginebanking.com/accounts/{}?key={}".format(accID, apiKey)
        person = requests.get(url)
        self.good = True
        if(person.status_code // 100 == 4):
            self.good = False
            return
        json_data = json.loads(person.text);
        self.parse_dict(json_data)

    @staticmethod
    def get_all():
        accounts = []
        url = "http://api.reimaginebanking.com/accounts?key={}".format(apiKey)
        people = requests.get(url)
        if(people.status_code // 400 == 4):
            return []
        json_data = json.loads(people.text)
        for person in json_data:
            newPerson = Account("");
            self.parse_dict(person)
            accounts.append(newPerson)
        return accounts

    def parse_dict(self, d):
        self.ID = d["_id"]
        self.type = d["type"]
        self.balance = d["balance"]
        self.nickname = d["nickname"]
        self.rewards = d["rewards"]
        self.customer_id = d["customer_id"]

    @staticmethod
    def get_by_custID(cID):
        if(cID == ""):
            return []
        url = "http://api.reimaginebanking.com/customers/{}/accounts?key={}".format(cID, apiKey)
        person = requests.get(url)
        if(person.status_code // 100 == 4):
            return []
        json_data = json.loads(person.text);
        rtn = []
        for d in json_data:
            newAccount = Account("")
            newAccount.parse_dict(d)
            rtn.append(newAccount)
        return rtn

    def json(self):
        return '{ "_id": "' + self.ID + '", "type": "' + self.type + '", "balance": '+str(self.balance)+ ', "nickname": "' + self.nickname + '", "rewards": ' + str(self.rewards) + ', "customer_id": "' + self.customer_id + '" }'

accID = "5828d214360f81f104553cc7" # valid for kelseys API key
custID = "58278805360f81f10454851a" # valid for kelseys API key
class Transfer:
    def __init__(self, ID):
        if(ID == ""):
            return
        url = "http://api.reimaginebanking.com/accounts/{}/transfers?key={}".format(ID, apiKey)
        transfer = requests.get(url)
        if(transfer.status_code // 100 == 4):
            self.good = False
            return
        json_data = json.loads(transfer.text)
        parse_dict(json_data)

    def parse_dict(self, d):
        self.ID = d["_id"]
        self.type = d["type"]
        self.transaction_date = d["transaction_date"]
        self.status = d["status"]
        self.medium = d["medium"]
        self.payer_id = d["payer_id"]
        self.payee_id = d["payee_id"]
        self.amount = d["amount"]
        self.description = d["description"]
        self.description = "" if self.description is None else self.description

    @staticmethod
    def get_by_account(custID):
        print(custID)
        url = "http://api.reimaginebanking.com/accounts/{}/transfers?key={}".format(custID, apiKey)
        transfers = requests.get(url)
        if(transfers.status_code // 100 == 4):
            return []
        rtn = []
        json_data = json.loads(transfers.text)
        for d in json_data:
            newTransfer = Transfer("")
            newTransfer.parse_dict(d)
            rtn.append(newTransfer)
        return rtn

    @staticmethod
    def get_by_custID(custID):
        accounts = Account.get_by_custID(custID)
        rtn = []
        for account in accounts:
            rtn += Transfer.get_by_account(account.ID)
        return rtn


    def json(self):
        return '{ "_id": "'+self.ID+'", "type": "'+self.type+'", "transaction_date": "'+self.transaction_date+'", "status": "'+self.status+'", "medium": "'+self.medium+'", "payer_id": "'+self.payer_id+'", "payee_id": "'+self.payee_id+'", "amount": '+str(self.amount)+', "description": "'+self.description+'" }'

