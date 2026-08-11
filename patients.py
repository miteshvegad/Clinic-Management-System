# All Thing Has Been Fixed this File Has been Completly Ready
# core Logic and code of Patients.py by Ayush  
# adding json Functionality by mitesh

import json

file_path = "./data/Patients.json"
try:
    with open(file_path, 'r') as R_Appointment:
        data = json.load(R_Appointment)
except json.decoder.JSONDecodeError:
        # Triggered if the file has text, but isn't valid JSON
        data = []
        
patients = data

def add_patient(add_id,add_name,add_phone,add_age ):
    for patient in patients : 
        if patient["id"] == add_id :
            return False
        

    patient = {
        "id" : add_id,
        "name" : add_name,
        "age" : add_age, 
        "phone" : add_phone
    }
    patients.append(patient)
    
    with open(file_path, 'w') as W_Petients:
        data = json.dump(patients, W_Petients, indent=4)

    return True




def view_patients():
    return patients


def search_patient(serach_id):

    found = False
    for patient in patients:
        if patient["id"] == serach_id:
            found = True
            
    return found

def delete_patient(delete_id):
    for patient in patients:
       if  patient["id"]==delete_id.upper():
           patients.remove(patient)
           
           with open(file_path, 'w') as W_Petients:
                data = json.dump(patients, W_Petients, indent=4)
           return True
       
    return False
        

add_patient("P001","Mitesh Vegad","718273081212", "19")


# add_patient()
# print(view_patients())
# print(search_patient("P001"))
# print(delete_patient("P001"))
# print(view_patients())
