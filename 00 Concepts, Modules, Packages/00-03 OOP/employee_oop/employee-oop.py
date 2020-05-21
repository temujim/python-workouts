class Employee:

    raise_amt = 1.04

    def __init__(self, firstname, lastname, pay):
        self.first = firstname
        self.last = lastname
        self.pay = pay
        self.email = self.first + '.' + self.last + '@gmail.com'

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        return self.raise_amt*self.pay


class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, firstname, lastname, pay, language):
        Employee.__init__(self, firstname, lastname, pay)
        self.proglang = language


class Manager(Employee):

    def __init__(self, firstname, lastname, pay, members=None):
        super().__init__(firstname, lastname, pay)

        if members is None:
            self.members = []
        else:
            self.members = members

    def print_emps(self):
        if self.members is not None:
            for i in self.members:
                print(" ---> " + i.fullname())

    def remove_emps(self, emp):
        if emp in self.members:
            self.members.remove(emp)

        self.print_emps()

    def add_emps(self, new_emp):
        self.members.append(new_emp)


employee_no1 = Employee('Ed', 'Sattar', 1000)
dev1 = Developer('Shujaat', 'Ali', 100, 'php')
dev2 = Developer('Saqib', 'Sharafaz', 150, 'html')
mgr1 = Manager('James', 'Maningo', 500, [dev1, dev2])
dev3 = Developer('Mark', 'Hambunan', 200, 'powerbi')
dev4 = Developer('Tin', 'Vergara', 300, 'agileproj')

print(employee_no1.fullname())
print(mgr1.email)
print(sys.version_info)
