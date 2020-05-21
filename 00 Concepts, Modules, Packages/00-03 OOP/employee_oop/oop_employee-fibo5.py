# %% Createa a programe with base class of Employee



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
        return self.pay*self.raise_amt


# %% Test File, Instantiation process

employee_no1 = Employee('Ed', 'Sattar', 1000)

# %%
employee_no1.fullname()
employee_no1.email
employee_no1.apply_raise()


# %% Create a Developer subClass


class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, firstname_dev, lastname_dev, pay_dev, proglang):
        Employee.__init__(self, firstname_dev, lastname_dev, pay_dev)
        self.lang = proglang

# %% QA: Instantiation process

dev1 = Developer('Shujaat', 'Ali', 100, 'php')
dev2 = Developer('Saqib', 'Sharafaz', 150, 'html')

# %% Run

dev1.first
dev1.last


# %%

dev2.email
dev2.fullname()
dev2.apply_raise()
employee_no1.apply_raise()


# %% Define anohter subclass Manager that will take same attirbutes and method as Employee


class Manager(Employee):

    def __init__(self, firstname_lead, lastname_lead, pay_lead, members = None):
        super().__init__(firstname_lead, lastname_lead, pay_lead)

        if members is None:
            self.team = []
        else:
            self.team = members

    def print_emps(self):
        if self.team is not None:
            for i in self.team:
                print(" --> " + i.fullname())

    def add_emps(self, new_emp):
        if new_emp not in self.team:
            self.team.append(new_emp)

    def remove_emps(self, rev_emp):
        if rev_emp in self.team:
            self.team.remove(rev_emp)
            print("{} is sucessfully removed.".format(rev_emp.fullname()))


# %% 


mgr1 = Manager('James', 'Maningo', 500, members= [dev1, dev2])

dev3 = Developer('Mark', 'Hambunan', 200, 'powerbi')


# %%

mgr1.email
mgr1.fullname()
mgr1.apply_raise()
mgr1.print_emps()
mgr1.add_emps(dev3)
print("\n*********  Added new Employee  **********")
mgr1.print_emps()


# %%
mgr1.remove_emps(dev2)

# %%
mgr1.print_emps()
