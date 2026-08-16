'''
it just Taking Raw data of the 

in main file do for this :  Formate the Data and Time  for create_appointment

'''
import json
import patients 
import doctors

file_path = "./data/Appoinments.json"

# Check if file exists and has content

try:
    with open(file_path, 'r') as R_Appointment:
        data = json.load(R_Appointment)
except json.decoder.JSONDecodeError:
        # Triggered if the file has text, but isn't valid JSON
        data = []



 

Appoinments =  data


def create_appointment(id,patient_id, doctor_id, date, time ) : 
    # sample data for check if the pentiate and Doctors are exists 
    # logic for pentiate already exits
        
    is_Patient = patients.search_patient(patient_id)[0]   

    if(not is_Patient):
        return is_Patient,"Petient Not Exits !"
    
    # logic doctor already exitst
            
    is_doc = doctors.search_doctor(doctor_id)[0]  
    
    if(not is_doc):
        return is_doc,"Doctor Not Exits !"
    
    
    Appoinment = {}
    # logic to check if it already exits 
    if  len(Appoinments) > 0:  #if Appinments if not empty list then 
        for Apnmt in Appoinments :
            if Apnmt.get("id") == id :
                return True, "Appoinment, Already Created" # means alreadt exits the appointment  
            
    Appoinment["id"] = id
    Appoinment["patient_id"] = patient_id
    Appoinment["doctor_id"] = doctor_id
    Appoinment["date"] = date
    Appoinment["time"] = time
    
    Appoinments.append(Appoinment)
    with open(file_path, 'w') as W_Appointment:
        data = json.dump(Appoinments, W_Appointment, indent=4)
        
    return True
    # done method is working 
    

def view_appointments():
    return Appoinments

def cancel_appointment(Appoingment_id):
    if(len(Appoinments) == 0):
        return False
    
    for apmt in Appoinments:
        if(apmt.get("id") == Appoingment_id):
            # remove from list 
            Appoinments.remove(apmt)
            with open(file_path, 'w') as W_Appointment:
                    data = json.dump(Appoinments, W_Appointment, indent=4)
            return True
            
    
    return False
        
# print(create_appointment("A001", "P001", "D001",  "2026-08-10",  "10:30"))
# print(create_appointment("A003", "P003", "D003",  "2026-08-10",  "10:12"))

# print(Appoinments)
# cancel_appointment("A001")  
# print(Appoinments,"\n")

# cancel_appointment("A002")  
# print(Appoinments,"\n")

# cancel_appointment("A003")  
# print(Appoinments,"\n")
  
# print(view_appointments())



# this FIle Has been Complted now 