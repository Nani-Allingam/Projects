import json

# ----------- Patient Class -----------
class Patient:
    def __init__(self, pid, name, age, problem):
        self.pid = pid
        self.name = name
        self.age = age
        self.problem = problem

    def to_dict(self):
        return self.__dict__


# ----------- Doctor Class -----------
class Doctor:
    def __init__(self, did, name, specialization):
        self.did = did
        self.name = name
        self.specialization = specialization

    def to_dict(self):
        return self.__dict__


# -------- Load / Save Functions ----------
def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


# ----------- Patient Functions ----------
def add_patient():
    data = load_data("patients.json")
    pid = input("Enter Patient ID: ")
    name = input("Name: ")
    age = input("Age: ")
    problem = input("Problem: ")

    patient = Patient(pid, name, age, problem)
    data.append(patient.to_dict())

    save_data("patients.json", data)
    print("✅ Patient Added Successfully!")


def view_patients():
    data = load_data("patients.json")
    print("\n--- Patients List ---")
    for p in data:
        print(p)


# ----------- Doctor Functions ----------
def add_doctor():
    data = load_data("doctors.json")
    did = input("Doctor ID: ")
    name = input("Name: ")
    spec = input("Specialization: ")

    doctor = Doctor(did, name, spec)
    data.append(doctor.to_dict())

    save_data("doctors.json", data)
    print("✅ Doctor Added Successfully!")


def view_doctors():
    data = load_data("doctors.json")
    print("\n--- Doctors List ---")
    for d in data:
        print(d)


# ----------- Appointment ----------
def book_appointment():
    data = load_data("appointments.json")
    pid = input("Patient ID: ")
    did = input("Doctor ID: ")
    date = input("Date: ")

    appt = {"patient_id": pid, "doctor_id": did, "date": date}
    data.append(appt)

    save_data("appointments.json", data)
    print("✅ Appointment Booked!")


# ----------- Billing ----------
def generate_bill():
    pid = input("Enter Patient ID: ")
    amount = input("Enter Amount: ")

    bill = f"\nPatient ID: {pid}\nBill Amount: {amount}\n"
    with open("bills.txt", "a") as f:
        f.write(bill)

    print("✅ Bill Generated!")


# ----------- Main Menu ----------
def main():
    while True:
        print("\n===== Hospital Management System =====")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Add Doctor")
        print("4. View Doctors")
        print("5. Book Appointment")
        print("6. Generate Bill")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            add_doctor()
        elif choice == "4":
            view_doctors()
        elif choice == "5":
            book_appointment()
        elif choice == "6":
            generate_bill()
        elif choice == "7":
            print("Exiting Program...")
            break
        else:
            print("Invalid choice!")

main()
