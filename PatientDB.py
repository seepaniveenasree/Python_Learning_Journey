all_patients=[]

def insert_details(name,age,disease,status,roomno):
    patient={'Name':name,'Age':age,'Disease':disease,'Status':status,'Roomno':roomno}
    all_patients.append(patient)
    print("Patient Details added successfully")

def view_all_patients():
    return all_patients

def search_patient(name):
    for patient in all_patients:
        if (patient['Name']==name):
            return patient
    else:
        return None

def diseased_patients(disease):
    patients_dis=[]
    for patient in all_patients:
        if (patient['Disease']==disease):
            patients_dis.append(patient['Name'])
    return patients_dis
     
        
def update_status(name,upd_status):
    patient=search_patient(name)
    if patient:
        patient['Status']=upd_status
        print("Patient Status updated successfully")
    else:
        print("Patient no found")

def cured_patients():
    patients_cure=[]
    for patient in all_patients:
        if ( patient['Status']=='cured'):
            patients_cure.append(patient['Name'])
    return patients_cure

def uncured_patients():
    patients_uncured=[]
    for patient in all_patients:
        if ( patient['Status']=='uncured'):
            patients_uncured.append(patient['Name'])
    return patients_uncured
    
def delete_patient(name):
    for patient in all_patients:
        if (patient['Name']==name):
            all_patients.remove(patient)
            print("Patient Deleted Successfully")
            return
    else:
         print("Patient not found")
