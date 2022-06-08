import csv
class Owner:
    def __init__(self,owner_id,last_name,first_name,street_address,city,state):
        self.owner_id = owner_id
        self.last_name = last_name
        self.first_name = first_name
        self.street_address = street_address
        self.city = city
        self.state = state
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def all_owners():
        owners=[]
        with open("/Users/huntermcreynolds/code/exercises/Week3/oop-bank-accounts/support/owners.csv") as f :     
            student_reader = csv.DictReader(f,skipinitialspace=True)
            for row in student_reader:
                owners.append(Owner(int(row["owner_id"]),row["last_name"],row["first_name"],row["street_address"],row["city"],row["state"]))
        return owners   