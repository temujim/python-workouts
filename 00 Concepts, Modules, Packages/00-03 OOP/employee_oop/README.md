# OOP Workout - Employee  
Taken from Corey Shafers YT Tutorial


1. [O] Create a program with a base class of Employee that can do the following:   
    * [X] set static variable of employee raise_amt to 1.04
    * [X] Accept first name, last name, and pay
    * [X] Provides instance variables of first, last and email
    * [X] Returns a function to provide the full name
    * [ ] Returns a fucntion to appy raise
    * [X] QA THE SCRIPT:
        * [X] Create instance variable employee_no1 = Ed Sattar, 1000
        * [X] get the first name, get the last name, get the email
        * [X] get the fullname
        * [X] get the return value for applied raise 
5. [X] Create a subclass "Developer" that will take the same arguments as Employee but adds programming language
    * [X] Call the base class init method using the class name (first method)
    * [X] Declar static variable raise_amt to 1.10
    * [X] Declare the class and instance variables for programming language
    * [X] QA THE SCRIPT
        * [X] Create instance variables dev1 & dev2 under Developer subclass
            * [X] dev1 = Shujaat Ali, 100, html
            * [X] dev2 = Saqib Sharafaz, 150, php
        * [X] For the dev1, get the first name, get the last name
        * [X] for the dev2, get the fullname and get the apply_raise 
        * [X] Get the value of apply_raise value of employee number 1
6. [O] Define another subclass Manager that will take same attributes and method as Employee but adds Employee
    * [X] Set default argument of employee to None
    * [X] Use super in calling the subclasiks
    * [X] Declare the class and instance variables for employees
        * [X] use proper coding for default mutable arugments
    * [O] Define the class methods:
        * [X] print_emps - takes self as an argument
        * [X] add_emps - use list as an argument
        * [ ] remove_emp - use list as an argument
      * [X] QA the Script:
          * [X] Create instance variable mgr1 for Manager: James Maningo, 1000, employee = dev1, dev
          * [X] print the Manager first name, manager last name, manager email
              * [X] manager full name and apply raise of manager
          * [X] add employee dev3: Mark Hambunan, 1500, power bi,
          * [X] print dev 3 & dev 1 details:
              * [X] dev3 full name, pay raise, email
          * [X] print employees under mgr1
          * [X] remove dev1
          * [X] print employees
7. [X] Create 2 developers, 1 manager:

