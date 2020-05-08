# class DataShell:
#
#     family = 'Shellane'
#
#     def __init__(self, identifier, data):
#         self.identifier = identifier
#         self.data = data
#
#
# x = 100
y = list(range(0, 11))


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
