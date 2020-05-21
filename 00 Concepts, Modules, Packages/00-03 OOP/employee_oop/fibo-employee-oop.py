# %% Create an Employee Class
class employee():
    raise_amt = 1.04

    def __init__(self, firstname, lastname, pay):
        self.first = firstname
        self.last = lastname
        self.pay = pay
        self.email = self.first + '.' + self.last + '@gmail.com'

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        return round(self.pay*self.raise_amt)

# QA Process --------------------------------------------------------

employee_no1 = employee('Ed', 'Sattar', 1000)
print("\n-----  Return the email address")
print(employee_no1.email)

print("\n-----  Return Fullname ---  ")
print(employee_no1.fullname())

print("\n-----  Apply Raise Amout")
print(employee_no1.apply_raise())

# %% 2. Createa subClass Developer to inherent from employee

class Developer(employee):
    raise_amt = 1.10

    def __init__(self, f, l, p, language):
        employee.__init__(self, f, l, p)
        self.proglang = language

# QA Process --------------------------------------------------------

dev1 = Developer('Shujaat', 'Ali', 100, 'php')
dev2 = Developer('Saqib', 'Sharafaz', 150, 'html')

print("\n\n ============ 2. DEVELOPER CLASS ========================")
#print(Developer.fullname())
print(dev1.first)
print(dev1.fullname())
print(dev1.proglang)
print(dev1.apply_raise())

# %% 3. Create a Manager subClass

class Manager(employee):

    def __init__(self, fi, la, pay, members = None):
        super().__init__(fi, la, pay)

        if members == None:
            self.members = []
        else:
            self.members = members


    def print_emps(self):
        if self.members is not None:
            for mem in self.members:
                print(" ---> " + mem.fullname())

    def add_emps(self, mem):
        self.members.append(mem)

    def remove_emps(self, mem):
        if mem in self.members:
            self.members.remove(mem)
        

# QA Process --------------------------------------------------------

mgr1 = Manager('James', 'Maningo', 500, members = [dev1, dev2])
# mgr1 = Manager('James', 'Maningo', 500)

dev3 = Developer('Mark', 'Hambunan', 200, 'powerbi')


print("\n\n ============ 3. DEVELOPER CLASS ========================")
print(mgr1.fullname())
mgr1.print_emps()

print("\n --- Print After Adding new Dev ")
mgr1.add_emps(dev3)
mgr1.print_emps()

print("\n --- Remove Dev")
mgr1.remove_emps(dev2)
mgr1.print_emps()
