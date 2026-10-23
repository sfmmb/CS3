class Patient:
    __name:str
    _bill_amount:float
    def __init__(self, name, bill_amount):
        self.__name = name
        self._bill_amount = bill_amount
    def get_name(self):
        return f"Patient Name: {self.__name}"
    def set_name(self, name):
        self.__name = name
    def get_bill_amount(self):
        return f"Original Bill: P{self._bill_amount}"
    def set_bill_amount(self, bill_amount):
        self._bill_amount = bill_amount
    def calculate_bill(self):
        return f"Final Bill: P{self._bill_amount}"

class SeniorPatient(Patient):
    def calculate_bill(self):
        self._bill_amount *= 0.8
        return f"Final Bill: P{self._bill_amount}"

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        self._bill_amount *= 0.85
        return f"Final Bill: P{self._bill_amount}"