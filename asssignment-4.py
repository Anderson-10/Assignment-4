#Os We will allow access to the operative system and their functionalities 
import os


class Employee:
    def __init__(self, id_employee, name,position,quantity = 0,overtime = 0,salary=0.0 ):
        self.id_employee = id_employee
        self.name = name
        self.position = position
        self.quantity = quantity
        self.overtime = overtime
        self.salary = salary

class Area:
    def __init__(self, id_area, area,position,value_hour,value_overtime):
        self.id_area = id_area
        self.area = area
        self.position = position
        self.value_hour = value_hour
        self.value_overtime = value_overtime

employees = {}
areas = {}
hst = 13.0

human_resources_manager = Area(1,'Human Resources','manager',42.0,63.0)
human_resources_assistant = Area(2,'Human Resources','assistant',18.0,27.0)
finance_assistant = Area(3,'Finance','assistant',24.0,36.0)
finance_Analyst = Area(4,'Finance','Analyst',38.0,57.0)
IT_support = Area(5,'IT','IT Support',28.0,42.0)
IT_devepoler = Area(6,'IT','Developer',40.0,60.0)

areas[human_resources_manager.id_area] = human_resources_manager
areas[human_resources_assistant.id_area] = human_resources_assistant
areas[finance_assistant.id_area] = finance_assistant
areas[finance_Analyst.id_area] = finance_Analyst
areas[IT_support.id_area] = IT_support
areas[IT_devepoler.id_area] = IT_devepoler

def isInt (message, isValidateArea, isValidateEmployee):
    while True:
        num = input(message)
         
        try:
            numInt = int(num)
            if isValidateArea == False and isValidateEmployee == False:
                return numInt
            if(isValidateArea == True and numInt >= 1 and numInt <=len(areas)):
                return numInt
            if(isValidateEmployee == True and numInt >= 1 and numInt <=len(employees)):
                return numInt
            if(isValidateArea == True):
                print("Please select a range between 1 - "+str(len(areas)))
            if(isValidateEmployee == True):
                print("Please select a range between 1 - "+str(len(employees)))
             
        except ValueError:
            print("Please add a correct value ")

def newEmployee():
    id = int(len(employees) + 1) 
    name = input("Write the name of the employee:")          
    print("Show the company current Areas")
    print("%-30s %-15s %-15s " %('id_area','area','position'))
    for i in areas:
             print("%-30s %-15s %-15s " %(str(areas[i].id_area), str(areas[i].area), str(areas[i].position)))
    position = isInt("Select the position where you want to add the user Please select the ID:",True,False)
    employees[id] = Employee(id, name, position )

def isIntOption (message):
    while True:
        num = input(message)
        try:

            numInt = int(num)
            return numInt
        
        except ValueError:
            showMenu()
            print("Please select a valid option in the Menu ")

def showMenu():
    os.system('cls')
    MenuSelection = ["Add a New Employee ","Show Company Areas ","Add hours worked for the employee","show payment information","Upload information to the system","Save Changes ", "Exit Program"]

    i = 0
    for option in MenuSelection:
        i = i + 1
        print ("{}- {}".format(i,option))


def employeeInfoMenu():
    print("%-30s %-15s %-15s %-15s %-15s %-15s %-15s" %('id_employee','name','area','position','quantity','overtime','salary'))
    for j in employees:
        data = employees[j]
        print("%-30s %-15s %-15s %-15s %-15s %-15s %-15s" %(str(data.id_employee), str(data.name),str(areas[int(data.position)].area), str(areas[int(data.position)].position), str(data.quantity) ,str(data.overtime), str(data.salary)))

def employeeInfo():
    print("%-30s %-15s %-15s %-15s %-15s %-15s %-15s" %('id_employee','name','area','position','quantity','overtime','salary'))
    for j in employees:
        data = employees[j]
        print("%-30s %-15s %-15s %-15s %-15s %-15s %-15s" %(str(data.id_employee), str(data.name),str(areas[int(data.position)].area), str(areas[int(data.position)].position), str(data.quantity) ,str(data.overtime), str(data.salary)))
    input("Press enter to continue")


def addWorkedHours():
    print(" Please select a user to add the time in hours ")
    employeeInfoMenu()
    id_employee = int(isInt("Select employee id:",False,True))
    employee = employees[id_employee]
    employee.quantity = int(isInt ("Enter the hours worked by the user: ",False,False))
    employee.overtime = int(isInt("Write the overtime of the employee: ",False,False))
    employee.salary = (areas[int(employee.position)].value_hour * float(employee.quantity)) + (areas[int(employee.position)].value_overtime * float(employee.overtime))
    employees[id_employee] = employee

def showEmployeTicket():
    print(" Select an user to see the payment information")
    employeeInfoMenu()
    id_employee = int(isInt("Press the number ID to see the total:",False,True))
    employee = employees[id_employee]
    hstValue = hst * employee.salary / 100
    total = employee.salary - hstValue
    print("%-30s %-15s %-15s %-15s %-15s %-15s %-15s" %('name','position','quantity','overtime','salary','hstValue','Total'))
    print("%-30s %-15s %-15s %-15s %-15s %-15s %-15s" %(employee.name,employee.position,str(employee.quantity),str(employee.overtime),str(employee.salary),str(hstValue),str(total)))


def saveDB():

    demoFile = 'C:/Users/dario/Documents/tarea 4/data.txt'
    myFile = open(demoFile, 'w') 
    for j in employees:
        data = employees[j]
        myFile.write("\n{},{},{},{},{},{}".format(data.id_employee, data.name,data.position, data.quantity,data.overtime, data.salary))
        myFile.close
    return


def loadDB():
              
    demoFile = 'C:/Users/Ander/Documents/Assignment4/data.txt'
    isFile = os.path.isfile(demoFile)
    if isFile:
        myFile = open(demoFile)
        for line in myFile:
            data = line.split(",")
            
            if (len(data)== 6):
                employees[int(data[0])] = Employee(int(data[0]), data[1], int(data[2]),int(data[3]),int(data[4]),float(data[5]))
        myFile.close
    return

menuAction = 0
#variable to check the kind of data 
isValidOption = True
while True:
    showMenu()

    if (isValidOption == False):
        print("Please select a valid option")
    menuAction = isIntOption("Enter menu selection:")

    if ( menuAction == 1):
        newEmployee()
        isValidOption = True

    elif ( menuAction == 2):
        employeeInfo()
       
        isValidOption = True
    elif ( menuAction == 3):
        addWorkedHours()
        
        isValidOption = True
    elif ( menuAction == 4):
        showEmployeTicket()
        isValidOption = True
        input("Press enter to continue")
    elif ( menuAction == 5):
        loadDB()       
        isValidOption = True
    elif (menuAction == 6):
        saveDB()
        isValidOption = True
        input("File has been saved. Press Enter to continue")
    elif(menuAction == 7):
        break
    else:
        isValidOption = False
