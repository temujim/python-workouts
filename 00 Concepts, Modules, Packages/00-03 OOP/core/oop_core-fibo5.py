# %% 19. OOP Instance and Class Variables
class DataShell:
    family = 'Shellane'

    def __init__(self, x, dataList):
        self.identifier = x
        self.data = dataList


x = 100
y = list(range(1, 6))

my_data_shell = DataShell(x, y)


print(my_data_shell.identifier)
print(my_data_shell.data)

print(my_data_shell.family)

my_data_shell.family = 'PearlyShells'

print(my_data_shell.family)


# %% 20. OOP Methods

class DataShell:

    def __init__(self, dataList):
        self.data = dataList

    def show(self):
        return self.data

    def avg(self):
        sum = 0

        for i in self.data:
            sum += i

        return sum/len(self.data)

my_data_shell2 = DataShell(y)

print(my_data_shell2.show())

print(my_data_shell2.avg())


# %% the difference between the pritn method is that you cannot further manipulate the print output
# since the dataype is basically nonetype
