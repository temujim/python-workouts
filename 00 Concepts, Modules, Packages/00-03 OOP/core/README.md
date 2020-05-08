# Basic OOP Execise  
Sourced from DataCamp


19. [OOP: Instance and Class Variables](#OOP:-Instance-and-Class-Attributes)
    1. Create a class called DataShell.
    2. Declare a class variable called family and assign it the value of "ShellLane".
    3. Initialize the class with the self, identifier, and data arguments. Set identifier and data to be instance variables.
    4. Create an instance of DataShell called my_data_shell passing x and y to the constructor function.  
        x = 100   
        y = list(range(1, 6))
    5. Print the my_data_shell.identifier and my_data_shell.data and explore their contents.
    6. Print the my_data_shell.family to explore its contents.
    7. Override the class variable my_data_shell.family by assigning it the value "PearlyShells" to explore its contents.
20. [OOP: Methods](#OOP:-Methods)
    1. Create a class called DataShell with its initialization method, taking self and dataList as arguments. Declare data as an instance variable and assign it the value of the input argument dataList.
    2. Define show() as a class method, taking self as an argument. Inside of the method's body, print the instance variable data.
    3. Define avg() as a class method, taking self as an argument. Inside of the method's body, declare the variable avg and assign it the value of the average of the instance variable data. Then print it out.
    4. Instantiate DataShell as my_data_shell passing integer_list as an argument to the constructor. Then call your object's show() and avg() methods and explore their output.
    5. NOW, try using return under the methods instead of print, and see the difference
