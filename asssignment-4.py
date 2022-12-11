#Name:                     assignment4.py
#Author:                   Anderson Hurtado
#Date Created:             December 08-2022
#Date Last Modified        December 10-2022

#Purpose
#
#Program that allows adding users to the system of a particular company to add them to the payment system. 
#It allows the assignment of a position from a list preloaded in the system to each user.
#Each position is assigned an hourly salary.
#When saving the user in a position, that person will have the salary of the assigned position. 
#The program will request the hours worked and overtime to show the amount earned by the user. 
#The program performs the tax deduction and displays the message of the total without taxes.
#The program can save the added information in a .txt file.

#Os We will allow access to the operative system and their functionalities 
import os

#The class Movies provide a way to package data and functionalities, The class tributes as id, name, position, salary overtime
class Employee:
    def __init__(self, id_employee, name,position,quantity = 0,overtime = 0,salary=0.0 ):
        self.id_employee = id_employee
        self.name = name
        self.position = position
        self.quantity = quantity
        self.overtime = overtime
        self.salary = salary

#The class Movies provide a way to package data and functionalities, The class tributes as id, area, position, value_hour overtime
class Area:
    def __init__(self, id_area, area,position,value_hour,value_overtime):
        self.id_area = id_area
        self.area = area
        self.position = position
        self.value_hour = value_hour
        self.value_overtime = value_overtime

#Variables for storing sorted collection of data from classes
employees = {}
areas = {}
#Variable to calculate the Taxes
hst = 13.0

# Area variables preloaded with company area values, job titles and salaries
human_resources_manager = Area(1,'Human Resources','manager',42.0,63.0)
human_resources_assistant = Area(2,'Human Resources','assistant',18.0,27.0)
finance_assistant = Area(3,'Finance','assistant',24.0,36.0)
finance_Analyst = Area(4,'Finance','Analyst',38.0,57.0)
IT_support = Area(5,'IT','IT Support',28.0,42.0)
IT_devepoler = Area(6,'IT','Developer',40.0,60.0)

#Uploading of preloaded charge information to the area option
areas[human_resources_manager.id_area] = human_resources_manager
areas[human_resources_assistant.id_area] = human_resources_assistant
areas[finance_assistant.id_area] = finance_assistant
areas[finance_Analyst.id_area] = finance_Analyst
areas[IT_support.id_area] = IT_support
areas[IT_devepoler.id_area] = IT_devepoler

#Variable to define the entrance of the int number 
def isInt (message, isValidateArea, isValidateEmployee):
    #loop while the condition keeps in true 
    while True:
        num = input(message)
        # The option Try, allows to catch errors to validate  
        try:
            numInt = int(num)
            if isValidateArea == False and isValidateEmployee == False:
                return numInt
            #Verify the amount of aggregated data and perform the condition of >= 1 on areas.
            if(isValidateArea == True and numInt >= 1 and numInt <=len(areas)):
                return numInt
            #Verify the amount of aggregated data and perform the condition of >= 1 on employees.
            if(isValidateEmployee == True and numInt >= 1 and numInt <=len(employees)):
                return numInt
            if(isValidateArea == True):
                #Checks the number of values in the list areas
                print("Please select a range between 1 - "+str(len(areas)))
            if(isValidateEmployee == True):
                #Checks the number of values in the list employees
                print("Please select a range between 1 - "+str(len(employees)))
        #If the condition is not correct, the assigned message is displayed.     
        except ValueError:
            print("Please add a correct value ")

#definition of employee function to add new user
def newEmployee():
    #It goes through the employees variable and adds one to add the following available id to the user. 
    id = int(len(employees) + 1) 
    #Variable name which requests the user's name 
    name = input("Write the name of the employee:")          
    print("Show the company current Areas")
    #Print area ID value, area and charge, and additional print values with coordinates to organize information.
    print("%-30s %-15s %-15s " %('id_area','area','position'))
    #For loop goes through the variable areas and displays the dictionary information. 
    for i in areas:
             print("%-30s %-15s %-15s " %(str(areas[i].id_area), str(areas[i].area), str(areas[i].position)))
    position = isInt("Select the position where you want to add the user Please select the ID:",True,False)
    employees[id] = Employee(id, name, position )

#Variable to define the entrance of the int number inside the option in the menu. 
def isIntOption (message):
    while True:
        num = input(message)
         # The option Try, allows to catch errors to validate
        try:

            numInt = int(num)
            return numInt
        # The code ask for a valid nange in the menu
        except ValueError:
            showMenu()
            # show the message to select a valid option
            print("Please select a valid option in the Menu ")

#The function for displaying the menu is defined
def showMenu():
    #clean the colsole since the operative system to show the menu
    os.system('cls')
    #Variable is defined that allows to see the menu options
    MenuSelection = ["Add a New Employee ","Show current Information","Add hours worked for the employee","show payment information","Upload information to the system","Save Changes ", "Exit Program"]
    
    i = 0
    #For loop goes through the variable menuselection and displays the information.
    for option in MenuSelection:
        i = i + 1
        print ("{}- {}".format(i,option))

#Defined employeeInfoMenu function that allows you to view the employee information in the menu
def employeeInfoMenu():
    print("%-30s %-15s %-15s %-15s %-15s %-15s %-15s" %('id_employee','name','area','position','quantity','overtime','salary'))
    #For loop goes through the variable employees and displays the information.
    for j in employees:
        data = employees[j]
        print("%-30s %-15s %-15s %-15s %-15s %-15s %-15s" %(str(data.id_employee), str(data.name),str(areas[int(data.position)].area), str(areas[int(data.position)].position), str(data.quantity) ,str(data.overtime), str(data.salary)))

#Defined employeeInfo function that allows you to view the employee information
def employeeInfo():
    print("%-30s %-15s %-15s %-15s %-15s %-15s %-15s" %('id_employee','name','area','position','quantity','overtime','salary'))
    #For loop goes through the variable employees and displays the information.
    for j in employees:
        data = employees[j]
        print("%-30s %-15s %-15s %-15s %-15s %-15s %-15s" %(str(data.id_employee), str(data.name),str(areas[int(data.position)].area), str(areas[int(data.position)].position), str(data.quantity) ,str(data.overtime), str(data.salary)))
    input("Press enter to continue")

#Function is defined to add the number of hours worked.
def addWorkedHours():
    print(" Please select a user to add the time in hours ")
    employeeInfoMenu()
    #Muestra la informacion que se ha cargado para los usuarios
    id_employee = int(isInt("Select employee id:",False,True))
    employee = employees[id_employee]
    #Requests the number of hours worked by the user. 
    employee.quantity = int(isInt ("Enter the hours worked by the user: ",False,False))
    #Asks if the user has taken extra time to add to the system.
    employee.overtime = int(isInt("Write the overtime of the employee: ",False,False))
    employee.salary = (areas[int(employee.position)].value_hour * float(employee.quantity)) + (areas[int(employee.position)].value_overtime * float(employee.overtime))
    employees[id_employee] = employee

#function to display payment information
def showEmployeTicket():

    print(" Select an user to see the payment information")
    employeeInfoMenu()
    #Request to enter one of the users to see the payment receipt with the discount information.
    id_employee = int(isInt("Press the number ID to see the total:",False,True))
    employee = employees[id_employee]
    #operation for calculating taxes
    hstValue = hst * employee.salary / 100
    #Total results of operations - taxes
    total = employee.salary - hstValue
    #Printout of the total result after deduction of taxes
    print("%-30s %-15s %-15s %-15s %-15s %-15s %-15s" %('name','position','quantity','overtime','salary','hstValue','Total'))
    print("%-30s %-15s %-15s %-15s %-15s %-15s %-15s" %(employee.name,employee.position,str(employee.quantity),str(employee.overtime),str(employee.salary),str(hstValue),str(total)))


def saveDB():
    #Path where the file with the preloaded information is stored. 
    demoFile = 'C:/Users/Ander/Documents/Assignment4/data.txt'
    myFile = open(demoFile, 'w') # - w is to start in 0 and a add to the end of the file
    for j in employees:
        data = employees[j]
        #save the information added since keyboard for all the parameters inside the option data.
        myFile.write("\n{},{},{},{},{},{}".format(data.id_employee, data.name,data.position, data.quantity,data.overtime, data.salary))
        myFile.close
    return

#Load all the information related to the process in the .txt file.
def loadDB():
    #Path where the file with the preloaded information is stored.          
    demoFile = 'C:/Users/Ander/Documents/Assignment4/data.txt'
    isFile = os.path.isfile(demoFile) # - check whether the path is an existing file or not
    if isFile:
        myFile = open(demoFile)
        for line in myFile:
            data = line.split(",")
            #validate if the quantity of parameters is 6 and save tha information in the .txt file.
            if (len(data)== 6):
                # save the information about the parameter data inside the class employees
                employees[int(data[0])] = Employee(int(data[0]), data[1], int(data[2]),int(data[3]),int(data[4]),float(data[5]))
        myFile.close
    return

menuAction = 0
#variable to check the kind of data 
isValidOption = True
while True:
    showMenu()
    #Check the info, if is false appear a warning message
    if (isValidOption == False):
        print("Please select a valid option")
    #variable to check the number in the menu and the selection
    menuAction = isIntOption("Enter menu selection:")
    #If the option is 1 the program allows to add a new user
    if ( menuAction == 1):
        newEmployee()
        isValidOption = True
    #If the opction is 2 the program allows see the info that we already have in the system.
    elif ( menuAction == 2):
        employeeInfo()
        isValidOption = True
    #Menu option that allows to add hours worked for each user. 
    elif ( menuAction == 3):
        addWorkedHours()
        isValidOption = True
    #Menu option that allows you to view the payment for the user.
    elif ( menuAction == 4):
        showEmployeTicket()
        isValidOption = True
        input("Press enter to continue")
    #Menu option to load the information to the .txt file
    elif ( menuAction == 5):
        loadDB()       
        isValidOption = True
        #Menu option to save the information to the .txt file
    elif (menuAction == 6):
        saveDB()
        isValidOption = True
        input("File has been saved. Press Enter to continue")
    #Program exit message
    elif(menuAction == 7):
        break
    else:
        isValidOption = False
