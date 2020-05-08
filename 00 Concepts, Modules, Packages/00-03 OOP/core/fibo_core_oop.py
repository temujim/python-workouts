class Shell:
    family = "Shellane"

    def __init__(self, identifier, data):
        self.identifier = identifier
        self.data = data

x = 100
y = list(range(1,10))

my_data_shell = Shell(x, y)

print(my_data_shell.identifier)
print(my_data_shell.family)
print("\n----------")
my_data_shell.family='PearlyShells'
print(my_data_shell.family)


# %% OOP Methods

class DataShell2():

    def __init__(self, data):
        self.dataList = data

    def show(self):
        return self.dataList

    def avg(self):
        sum = 0

        for i in self.dataList:
            sum += i

        return float(sum/len(self.dataList))


my_data_shell2 = DataShell2(y)
# print(my_data_shell2.show())
print("\n --------- List of Numbers  -----")
print(my_data_shell2.show())

print("\n --------- Avg of the numlist  -----")
print(my_data_shell2.avg())


