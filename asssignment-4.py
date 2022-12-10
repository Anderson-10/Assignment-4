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