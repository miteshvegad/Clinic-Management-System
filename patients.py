patients = []

def add_patient():

    add_id =   input("Enter a parients ID : ")
    for patient in patients : 
        if patient["id"] == add_id :
            print("this id is alredy exist")
            return
        
    add_name = input("Enter a patients Name :")
    add_phone = input("Enter a patients Mobile NUm :")
    add_age = input("Enter a patients Age :")

    patient = {
        "id" : add_id,
        "name" : add_name,
        "age" : add_age, 
        "phone" : add_phone
    }
    patients.append(patient)

    print("patient Details add succsesfully")




def view_patients():

    if not patients:
        print("no more patients")
        return

    for patient in patients:
        print("patient detaild : " )
        print("patient id =", patient["id"])
        print("patient name =", patient["name"])
        print("patient age =", patient["age"])
        print("patient phone=", patient["phone"])

def search_patient():

    serach_id = input("enter a patients id ")


    found = False
    
    for patient in patients:

        if patient["id"] == serach_id:
            print("patient id =", patient["id"])
            print("patient name =", patient["name"])
            print("patient age =", patient["age"])
            print("patient phone=", patient["phone"])
            found = True
    if found == False :
        print("patient not found")

def delete_patient():

    delete_id = input("enter patirnts id for delete :")
    found = False

    for patient in patients:
       if  patient["id"]==delete_id:
           patients.remove(patient)
           print("patient detaild delete sucssefully")
           found=True
           break
       if found==False:
           print("patient id not found" )

        

add_patient()
add_patient()
view_patients()
search_patient()
delete_patient()
