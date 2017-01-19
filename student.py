
class Student():

class Student(Object):


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
        balance = self.fee_target - total_fee_paid
        print "remaining balance is = " + str(balance)

class Student_records(Student):
    """docstring forStudent_records"""
    def __init__(self, cat_one=0,cat_two=0,exams=0):
        self.cat_one = cat_one
        self.cat_two = cat_two
        self.exams = exams

    def perfomance(self):
        marks = 0
        average = 0
        marks = self.cat_one + self.cat_two + self.exams
        average = marks // 3
        print "average marks = " + str(average)

#angela = Student("angela","assa", "2e2e")
angela = Student_accnt()
#angela.display_name()

angela.fee_balance(10000)
dan = Student_records(123,131,322)
dan.perfomance()
