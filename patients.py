# All Thing Has Been Fixed this File Has been Completly Ready
# core Logic and code of Patients.py by Ayush  
# adding json Functionality by mitesh

import json

file_path = "./data/Patients.json"
try:
    with open(file_path, 'r') as R_Pentient:
        data = json.load(R_Pentient)
except json.decoder.JSONDecodeError:
        # Triggered if the file has text, but isn't valid JSON
        data = []
        
patients = data

def add_patient(add_id,add_name,add_age,add_phone ):
    for patient in patients : 
        if patient["id"] == add_id :
            return False,"Pentient Already Exists.."
        

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
    patient_data = None
    for patient in patients:
        if patient["id"] == serach_id:
            found = True
            patient_data = patient
            
            
    return found,patient_data

def delete_patient(delete_id):
    for patient in patients:
       if  patient["id"]==delete_id.upper():
           patients.remove(patient)
           
           with open(file_path, 'w') as W_Petients:
                data = json.dump(patients, W_Petients, indent=4)
           return True
       
    return False
        
        
        
# Sample data 
# add_patient("P001","Rahul","24", "9876543210")


# add_patient()
# print(view_patients())
# print(search_patient("P001"))
# print(delete_patient("P001"))
# print(view_patients())
