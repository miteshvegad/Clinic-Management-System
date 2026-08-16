doctors = []

def add_doctor():

    doctor_id = input("enter doctor id :")
    for doctor in doctors:

        if doctor["id"]==doctor_id:
            print("doctors id already exist")
            return
    
    doctor_name= input("Enetr a doctor name  :")
    specialization=  input("Enter a doctor Specialization : ")
    fees = input("Enter a doctor fees :")

    doctor = {
        "id" : doctor_id,
        "name" : doctor_name,
        "specialization" : specialization,
        "fee": fees,
    }

    doctors.append(doctor)

    print("doctor add successfully")

def view_doctors():

    if not doctors :
        print("No Doctor")
        return

    for doctor in doctors :

        print("Doctor_id =",doctor["id"])
        print("doctor_name =",doctor["name"])
        print("specialization =",doctor["specialization"])
        print("fees =",doctor["fee"])

def search_doctor():

    search_id = input("enter a doctor id :")
    found = False

    for doctor in doctors:
         if doctor["id"]== search_id :
            print("Doctor_id =",doctor["id"])
            print("doctor_name =",doctor["name"])
            print("specialization =",doctor["specialization"])
            print("fees =",doctor["fee"])
            found=True
         if found==False:
             print("doctor not found")

add_doctor()
add_doctor()
view_doctors()
search_doctor()
    

