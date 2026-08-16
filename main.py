import patients
import doctors
import appointments
import billings
import time
import random
import importlib
from tabulate import tabulate

def type_animation(text , delay = 0.1):
    for char in text:
        print(char,end="", flush=True)
        time.sleep(delay)
    print()


def Design(Text):
    print('='*50)
    print(" "*15,end="")
    print(Text)
    print(" "*15,end="")
    print("")
    print('='*50)
    

def main():
    while(True):
        try : 
            Design("CLINIC MANAGEMENT SYSTEM")
            print('''
1. Patients
2. Doctors
3. Appointments
4. Billing
5. Reports
6. Save Data
7. Load Data
8. Exit            

                      ''')
            choise = int(input("Enter Yout Choise : "))
            if choise == 1 :
                type_animation("Entering the Pentients Menu...") 
                while(True):
                    time.sleep(1)
                    Design("PENTIENTS MENU ")
                    print('''
1. Add Patients
2. view patients
3. search patient
4. delete patient
5. Exit                                     
                                              ''')
                    ch1  = int(input("Enter Yout Choise : "))
                    if(ch1 == 1):
                        usr_id  =  input("Enter Pentient ID : ")
                        usr_Name =  input("Enter Pentient NAME : ")
                        usr_Age  =  int(input("Enter Pentient Age : "))
                        usr_Phone_no =  int(input("Enter Pentient Phone : "))
                        
                        re  = patients.add_patient(usr_id,usr_Name,str(usr_Age),str(usr_Phone_no))
                        if(re ==True):
                            type_animation("data Added Successfully...",0.12)
                        else:
                            type_animation(f"Error Occurr -- Message : {re}")
                    
                    elif(ch1 == 2):
                        type_animation("Viewing Petients ALL data ...\n",0.05)
                        datas = patients.view_patients()
                        print(tabulate(datas, headers="keys", tablefmt="grid"))
                        type_animation("Press 'Enter' Key If You done Viewing data.." )
                        input()

                        
                    elif(ch1 == 3):
                        choiseID = input("Enter the Petient ID(eg.P001) : ")
                        type_animation("Searching...")
                        data = patients.search_patient(choiseID.upper())
                        if(data[0]):
                            table_data = list(data[1].items())
                            print(tabulate(table_data, headers=["Key", "Value"], tablefmt="grid"))
                            
                        else:
                            type_animation(f"NO Petient Found With ID {choiseID} ")
                                   
                    elif(ch1 == 4):
                        type_animation("Warning .........")
                        type_animation("carefull Using this Function...")
                        
                        choiseID = input("Enter the Petient ID Which You want to Del (eg.P001) : ")
                        reEnterchoiseID  = input("ReEnter(Above): ")
                        
                        if(choiseID == reEnterchoiseID):
                            type_animation("DELETING....")
                            Ret = patients.delete_patient(reEnterchoiseID.upper())
                            if(Ret):
                                type_animation(f"Deleted SuccessFully With ID {reEnterchoiseID}")
                            else:
                                type_animation(f"NO Petient Found With ID {choiseID} ")
                        else:
                             type_animation("Check Carefully ")                         
                    elif(ch1 == 5):   
                        type_animation("Exiting TO Main Menu...")
                        
                        break
                    else:
                        print("enter the Vaild Input")
                        
                        
            
            elif(choise == 2):
                type_animation("Entering the Doctors Menu...") 
                while(True):
                    time.sleep(1)
                    Design("DOCTORS MENU")
                    print('''
1. Add Doctors
2. view Dctors
3. search Dctors
4. Exit                                     
                                                              ''')
                    ch2  = int(input("Enter Yout Choise : "))
                    if(ch2 == 1):
                        dr_id  =  input("Enter Doctor ID :(Eg.D001) ")
                        dr_Name =  "Dr. " + input("Enter Doctor Name (Without Dr.) : ")
                        dr_Specification  =  input("Enter specialization : ")
                        dr_fees = int(input("Enter Fees (eg.500): "))
                                                
                        re  = doctors.add_doctor(dr_id.upper(), dr_Name,dr_Specification, str('₹'+(str(dr_fees))))
                        
                        if(re ==True):
                            type_animation("data Added Successfully...",0.12)
                        else:
                            type_animation(f"Error Occurr -- Message : {re}")
                            
                    elif(ch2 == 2):
                        type_animation("Viewing Doctors ALL data ...\n",0.05)
                        datas = doctors.view_doctors()
                        print(tabulate(datas, headers="keys", tablefmt="grid"))
                        type_animation("Press 'Enter' Key If You done Viewing data.." )
                        input()
                        
                    elif(ch2 == 3):
                        choiseID = input("Enter the Doctor ID(eg.D001) : ")
                        type_animation("Searching...")
                        data = doctors.search_doctor(choiseID.upper())
                        if(data[0]):
                            table_data = list(data[1].items())
                            print(tabulate(table_data, headers=["Key", "Value"], tablefmt="grid"))
                                                    
                        else:
                            type_animation(f"NO Doctor Found With ID {choiseID} ")
                        pass
                    elif(ch2 == 4):
                        type_animation("Exiting TO Main Menu...")
                        break
                    else:
                        print("enter the Vaild Input")

            elif(choise == 3):
                type_animation("Entering the Appointments Menu...")
                while(True):
                    time.sleep(1)
                    Design("APPOINTMENTS MENU")
                    print('''
1. Add Appointment
2. view Appointments
3. cancel Appointment
4. Exit                                     
                                                              ''')
                    ch3  = int(input("Enter Yout Choise : "))
                    if(ch3 == 1):
                        appt_id     =  input("Enter Appointment ID :(Eg.A001) ")
                        patient_id  =  input("Enter Petient ID :(Eg.P001) ")
                        doctor_id   =  input("Enter Doctor ID :(Eg.D001) ")
                        appt_date   =  input("Enter Date (eg.2026-08-10) : ")
                        appt_time   =  input("Enter Time (eg.10:30) : ")

                        re  = appointments.create_appointment(appt_id.upper(), patient_id.upper(), doctor_id.upper(), appt_date, appt_time)

                        if(re ==True):
                            type_animation("data Added Successfully...",0.12)
                        else:
                            type_animation(f"Error Occurr -- Message : {re}")

                    elif(ch3 == 2):
                        type_animation("Viewing Appointments ALL data ...\n",0.05)
                        datas = appointments.view_appointments()
                        print(tabulate(datas, headers="keys", tablefmt="grid"))
                        type_animation("Press 'Enter' Key If You done Viewing data.." )
                        input()

                    elif(ch3 == 3):
                        type_animation("Warning .........")
                        type_animation("carefull Using this Function...")

                        choiseID = input("Enter the Appointment ID Which You want to Cancel (eg.A001) : ")
                        reEnterchoiseID  = input("ReEnter(Above): ")

                        if(choiseID == reEnterchoiseID):
                            type_animation("CANCELLING....")
                            Ret = appointments.cancel_appointment(reEnterchoiseID.upper())
                            if(Ret):
                                type_animation(f"Cancelled SuccessFully With ID {reEnterchoiseID}")
                            else:
                                type_animation(f"NO Appointment Found With ID {choiseID} ")
                        else:
                             type_animation("Check Carefully ")
                    elif(ch3 == 4):
                        type_animation("Exiting TO Main Menu...")
                        break
                    else:
                        print("enter the Vaild Input")

            elif(choise == 4):
                type_animation("Entering the Billing Menu...")
                while(True):
                    time.sleep(1)
                    Design("BILLING MENU")
                    print('''
1. Add Bill
2. view Bills
3. Exit                                     
                                                              ''')
                    ch4  = int(input("Enter Yout Choise : "))
                    if(ch4 == 1):
                        bill_id     =  input("Enter Bill ID :(Eg.B001) ")
                        patient_id  =  input("Enter Petient ID :(Eg.P001) ")
                        doctor_fee  =  int(input("Enter Doctor Fee (eg.800): "))
                        medicine    =  int(input("Enter Medicine Cost (eg.450): "))
                        test        =  int(input("Enter Test Cost (eg.300): "))

                        re  = billings.create_bill(bill_id.upper(), patient_id.upper(), doctor_fee, medicine, test)

                        if(re ==True):
                            type_animation("data Added Successfully...",0.12)
                        else:
                            type_animation(f"Error Occurr -- Message : {re}")

                    elif(ch4 == 2):
                        type_animation("Viewing Bills ALL data ...\n",0.05)
                        datas = billings.view_bills()
                        print(tabulate(datas, headers="keys", tablefmt="grid"))
                        type_animation("Press 'Enter' Key If You done Viewing data.." )
                        input()

                    elif(ch4 == 3):
                        type_animation("Exiting TO Main Menu...")
                        break
                    else:
                        print("enter the Vaild Input")

            elif(choise == 5):
                type_animation("Generating Report...",0.05)

                total_patients      = len(patients.view_patients())
                total_doctors       = len(doctors.view_doctors())
                total_appointments  = len(appointments.view_appointments())
                all_bills           = billings.view_bills()
                total_bills         = len(all_bills)

                total_revenue = 0
                for bill in all_bills:
                    total_revenue += bill.get("Total Bill :", 0)

                Design("REPORT")
                print(f'''
Patients       : {total_patients}
Doctors        : {total_doctors}
Appointments   : {total_appointments}
Bills          : {total_bills}

Total Revenue  : ₹{total_revenue}
                          ''')
                type_animation("Press 'Enter' Key If You done Viewing Report..")
                input()

            elif(choise == 6):
                type_animation("Saving Data...",0.08)
                type_animation("Data Is Already Auto-Saved After Every Add/Delete/Create Operation..")
                type_animation("Nothing Extra To Save...")

            elif(choise == 7):
                type_animation("Loading Data From Files...",0.08)
                importlib.reload(patients)
                importlib.reload(doctors)
                importlib.reload(appointments)
                importlib.reload(billings)
                type_animation("Data Loaded Successfully...")

            elif(choise == 8):
                type_animation("THANK YOU For Using this Tool \n-------------------Created By MITESH/AYUSH..")
                break

            else:
                print("enter the Vaild Input")
        
        except ValueError :
            print("Plx enter vaild Input")
            for i in range(0,random.randint(1,6)):
                time.sleep(1)
                print("Wait System Is Working...")
        
            
    


if __name__ == "__main__":
    main()