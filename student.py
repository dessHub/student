class Student(Object):

    def __init__(self, first_name, last_name,adm_no):
        """Create a student account with personal details."""
        self.first_name = first_name
        self.last_name = last_name
        self.adm_no = adm_no

    def remove_student(self,adm_no):
        if adm_no == self.adm_no:
            del student(adm_no)
        else:
            print "Student id not found"
       return 0;

class Student_accnt(Student):

    def fee_balance(self,total_fee_paid):
        fee_target = 20000
        self.total_fee_paid = fee_deposit(amount)
        self.balance = fee_target - total_fee_paid
        return balance

    def fee_deposit(self,amount):
        self.total_fee_paid = total_fee_paid + amount
        return total_fee_paid

class Student_records(Student):
    """docstring forStudent_records"""
    def perfomance(self, cat_one,cat_two,exams):
        self.marks = cat_one + cat_two + exams
        average = marks // 3
        return average
