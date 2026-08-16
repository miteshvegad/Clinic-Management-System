import json

file_path = "./data/Doctors.json"
try:
    with open(file_path, 'r') as R_Docs:
        data = json.load(R_Docs)
except json.decoder.JSONDecodeError:
        # Triggered if the file has text, but isn't valid JSON
        data = []
        
doctors = data

def add_doctor(doctor_id,doctor_name,specialization,fees):

    for doctor in doctors:
        if doctor["id"]==doctor_id:
            return False
    
    doctor = {
        "id" : doctor_id,
        "name" : doctor_name,
        "specialization" : specialization,
        "fee": fees,
    }

    doctors.append(doctor)
    with open(file_path, 'w') as W_Docs:
        data = json.dump(doctors, W_Docs, indent=4)
        
    return True

def view_doctors():
    return doctors

def search_doctor(search_id):
    Doctor_data  =None
    found = False
    for doctor in doctors:
         if doctor["id"]== search_id :
            Doctor_data =  doctor
            found=True
    
    return found,Doctor_data        
    
# Sample Data 
# add_doctor("D001","Dr. Sharma","Cardiology",800)
# add_doctor("D002","DR. Rock ","Cardiology",800)
# add_doctor("D003","DR. Gigaman ","Cardiology",800)

# print(view_doctors())
# print(search_doctor("D004"))
    

