class Student():

    def __init__(self, first_name, last_name,adm_no):
        """Create a student account with personal details."""
        self.first_name = first_name
        self.last_name = last_name
        self.adm_no = adm_no

    def display_recors(self):
        std_details = {}
        if self.adm_no is not None:
            std_details.update({"first_name" : self.first_name})
            std_details.update({"last_name" : self.last_name})
            std_details.update({"adm_no" : self.adm_no})
            print std_details

class Student_accnt(Student):

    def __init__(self, balance=0, fee_target = 20000):
        self.balance = balance
        self.fee_target = fee_target

    def fee_balance(self,total_fee_paid):
        fee_target = 20000
        balance = 0
        #total_fee_paid = fee_deposit(amount)
        balance = fee_target - total_fee_paid
        print balance

    def fee_deposit(self,amount):
        self.total_fee_paid = total_fee_paid + amount
        return total_fee_paid

class Student_records(Student):
    """docstring forStudent_records"""
    def perfomance(self, cat_one,cat_two,exams):
        self.marks = cat_one + cat_two + exams
        average = marks // 3
        return average

#angela = Student("angela","assa", "2e2e")
angela = Student_accnt()
#angela.display_name()
ange
angela.fee_balance(10000)
