class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_bill_amount(self):
        return self.__bill_amount
    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount
    def calculate_bill(self):
        return self.__bill_amount
    def display_patient_type(self):
        print("Patient Type: Regular Patient")
class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80
    def display_patient_type(self):
        print("Patient Type: Senior Citizen")
class PhilhealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85
    def display_patient_type(self):
        print("Patient Type: Philhealth Member")

# ======
print("Hospital Billing System")
print("-" * 23)
#Patient 1 - Regular Patient
p1 = Patient("Juan Dela Cruz", 15000.00)
print(f"Patient Name: {p1.get_name()}")
p1.display_patient_type()
print(f"Original Bill: ₱{p1.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{p1.calculate_bill():,.2f}")
print("")
#Patient 2 - Senior Patient
p2 = SeniorPatient("Maria Santos", 15000.00)
print(f"Patient Name: {p2.get_name()}")
p2.display_patient_type()
print(f"Original Bill: ₱{p2.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{p2.calculate_bill():,.2f}")
print("")
#Patient 3 - Philhealth Patient
p3 = PhilhealthPatient("Pedro Reyes", 15000.00)
print(f"Patient Name: {p3.get_name()}")
p3.display_patient_type()
print(f"Original Bill: ₱{p3.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{p3.calculate_bill():,.2f}")