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
IT_support = Area(5,'Finance','Analyst',28.0,42.0)
IT_devepoler = Area(5,'Finance','Analyst',40.0,60.0)

areas[human_resources_manager.id_area] = human_resources_manager
areas[human_resources_assistant.id_area] = human_resources_assistant
areas[finance_assistant.id_area] = finance_assistant
areas[finance_Analyst.id_area] = finance_Analyst
areas[IT_support.id_area] = IT_support
areas[IT_devepoler.id_area] = IT_devepoler



def newEmployee():
    id = int(len(employees) + 1) 
    name = input("Write the name of the employee:")          
    print("Show the current areas")
    print('id_area','area','position','value_hour','value_overtime')
    for i in areas:
             print("{}{}{}{}".formatid_area, areas[i].area, areas[i].position,  areas[i].value_hour, areas[i].value_overtime)

    employees[id] = Employee(id, name )

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
    MenuSelection = ["Add a new Employee ","Show Current Employees ","Add worked hours to Employe","Show Employe ticket ","Load Employees from data file ","Save Changes ", "Exit Program"]

    i = 0
    for option in MenuSelection:
        i = i + 1
        print ("{}- {}".format(i,option))


def employeeInfoMenu():
    print('id_employee','name','area','position','quantity','overtime','salary')
    for j in employees:
        data = employees[j]
        print("{}{}{}{}{}{}{}" .format(data.id_employee, data.name, areas[int(data.position)].area, areas[int(data.position)].position, data.quantity, data.overtime,data.salary))

def employeeInfo():
    print('id_employee','name','area','position','quantity','overtime','salary')
    for j in employees:
        data = employees[j]
        print("{}{}{}{}{}{}{}" .format(data.id_employee, data.name,areas[int(data.position)].area, areas[int(data.position)].position, data.quantity ,data.overtime, data.salary))
    input("Press enter to continue")


def addWorkedHours():
    print(" Which employee do yo want to add hours?")
    employeeInfoMenu()
    id_employee = int(input("Select employee id:"))
    employee = employees[id_employee]
    employee.quantity = int(input("Write the quantity of the employee:",))
    employee.overtime = int(input("Write the overtime of the employee:",))
    employee.salary = (areas[int(employee.position)].value_hour * float(employee.quantity)) + (areas[int(employee.position)].value_overtime * float(employee.overtime))
    employees[id_employee] = employee

def showEmployeTicket():
    print(" Which employee do yo want to show ticket?")
    employeeInfoMenu()
    id_employee = int(input("Select employee id to see the total:"))
    employee = employees[id_employee]
    hstValue = hst * employee.salary / 100
    total = employee.salary - hstValue
    print("{}{}{}{}{}{}{}" .format('name','position','quantity','overtime','salary','hstValue','Total'))
    print("{}{}{}{}{}{}{}" .format(employee.name,employee.position,employee.quantity,employee.overtime,employee.salary,hstValue,total))



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
       
        isValidOption = True
    elif ( menuAction == 3):
        
        isValidOption = True
    elif ( menuAction == 4):
        
        isValidOption = True
        input("Press enter to continue")
    elif ( menuAction == 5):
       
        isValidOption = True
    elif (menuAction == 6):
        
        isValidOption = True
        input("File has been saved. Press Enter to continue")
    elif(menuAction == 7):
        break
    else:
        isValidOption = False
