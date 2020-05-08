# OOP Workout - Employee  
Taken from Corey Shafers YT Tutorial


1. Create a program with a base class of Employee that can do the following:   
    * set static variable of employee raise_amt to 1.04
    * Accept first name, last name, and pay
    * Provides instance variables of first, last and email
    * Returns a function to provide the full name
    * Returns a fucntion to appy raise
    * QA THE SCRIPT:
        * Create instance variable employee_no1 = Ed Sattar, 1000
        * get the first name, get the last name, get the email
        * get the fullname
        * get the return value for applied raise
5. Create a subclass "Developer" that will take the same arguments as Employee but adds programming language
    * Call the base class init method using the class name (first method)
    * Declare the class and instance variables for programming language
    * Declar static variable raise_amt to 1.10
    * QA THE SCRIPT
        * Create instance variables dev1 & dev2 under Developer subclass
            * dev1 = Shujaat Ali, 100, html
            * dev2 = Saqib Sharafaz, 150, php
        * For the dev1, get the first name, get the last name
        * for the dev2, get the fullname and get the apply_raise 
        * Get the value of apply_raise value of employee number 1
6. Define another subclass Manager that will take same attributes and method as Employee but adds Employee
    * Set default argument of employee to None
    * Use super in calling the subclasiks
    * Declare the class and instance variables for employees
        * use proper coding for default mutable arugments
    * Define the class methods:
        * print_emps - takes self as an argument
        * add_emps - use list as an argument
        * remove_emp - use list as an argument
      * QA the Script:
          * Create instance variable mgr1 for Manager: James Maningo, 1000, employee = dev1, dev
          * print the Manager first name, manager last name, manager email
              * manager full name and apply raise of manager
          * add employee dev3: Mark Hambunan, 1500, power bi,
          * print dev 3 & dev 1 details:
              * dev3 full name, pay raise, email
          * print employees under mgr1
          * remove dev1
          * print employees
7. Create 2 developers, 1 manager:

