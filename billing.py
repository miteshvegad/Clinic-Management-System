import json
import patients


'''

Bill structure:

{
    "bill_id": "B001",
    "patient_id": "B001",
    "doctor_fee": 800,
    "medicine": 450,
    "test": 300
}
'''

file_path = "./data/Bills.json"

# Check if file exists and has content

try:
    with open(file_path, 'r') as R_Appointment:
        data = json.load(R_Appointment)
except json.decoder.JSONDecodeError:
        # Triggered if the file has text, but isn't valid JSON
        data = []

bills  = data

def create_bill(bill_id, patient_id, doctor_fee, medicine, test): 
    is_Patient = patients.search_patient(patient_id)[0]   
    
    if(not is_Patient):
        return is_Patient,"Petient Not Exits !"
    subtotal  = doctor_fee + medicine + test
    
    
    if  len(bills) > 0:  #if Bill if not empty list then 
            for bill in bills :
                if bill.get("id") == id :
                    return True, "Bill, Already Created" 

    bill = {
            "bill_id" : bill_id,
            "patient_id" : patient_id,
            "doctor_fee" : doctor_fee,
            "medicine" : medicine,
            "test" : test,
            "Total Bill :" : subtotal
        }
    bills.append(bill)
    
    with open(file_path, 'w') as W_Bill:
            data = json.dump(bills, W_Bill, indent=4)
    return True


def view_bills():
    return bills

# print(create_bill("B001","P001",800,450,300)) Working : Done
# print(view_bills())  

  

