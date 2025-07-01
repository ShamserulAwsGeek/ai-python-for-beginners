from employee import Employee

class Company:
    def __init__(self):
        self.employee = []

    
    def add_employee(self,new_employee):
        self.employees.append(new_employee)

    def display_employess(self):
        print("current employees:")
        for i in self.employees:
            print(i.fname, i.lname)

        print('---------------------')


    def pay_employees(self):
        print('paying employees:')
        for i in self.employees:
            print('paycheck for:', i.fname, i.lname)
            print(f'amount:, ${i.calculate_paycheck():,.2f}')
            print('----------------------')
        


def main():
    my_company = Company()
    
    employee1 = Employee('Shamserul', 'Haque', 110000)
    my_company.add_employee(employee1)

    employee2 = Employee('Ashriti', 'Prakash', 80000)
    my_company.add_employee(employee2)

    employee3 = Employee('Maheen', 'Afroz', 40000)
    my_company.add_employee(employee3)
    
    my_company.display_employess()
    my_company.pay_employees()


main()