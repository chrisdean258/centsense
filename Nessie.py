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
        self.ID = json_data["_id"]
        self.first_name = json_data["first_name"]
        self.last_name = json_data["last_name"]
        self.zip = json_data["address"]["zip"]
        self.street_number = json_data["address"]["street_number"]
        self.state = json_data["address"]["state"]
        self.city = json_data["address"]["city"]
        self.street_name = json_data["address"]["street_name"]

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
            newPerson.ID = json_data[i]["_id"]
            newPerson.first_name = json_data[i]["first_name"]
            newPerson.last_name = json_data[i]["last_name"]
            newPerson.zip = json_data[i]["address"]["zip"]
            newPerson.street_number = json_data[i]["address"]["street_number"]
            newPerson.state = json_data[i]["address"]["state"]
            newPerson.city = json_data[i]["address"]["city"]
            newPerson.street_name = json_data[i]["address"]["street_name"]
            customers.append(newPerson)
        print(customers)
        return customers





Customer.get_all()
