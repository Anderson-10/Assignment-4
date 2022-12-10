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