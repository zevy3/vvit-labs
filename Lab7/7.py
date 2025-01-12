class Employee:
    def __init__(self,name,eid):
        self.name=name
        self.eid=eid

    def get_info(self):
        return f'Имя - {self.name}; ID - {self.eid}'

class Manager(Employee):
    def __init__(self,name,eid,department):
        super().__init__(name,eid)
        self.department=department

    def manage_project(self,project):
        return f'{self.name} управляет проектом {project}'

class Technician(Employee):
    def __init__(self,name,eid,specialization):
        super().__init__(name,eid)
        self.specialization=specialization
    def perform_maintenance(self):
        return f'{self.name} выполняет техническое обслуживание {self.specialization}'

class TechManager(Manager, Technician):
    def __init__(self, name, eid, department, specialization):
        Employee.__init__(self, name, eid)
        self.department = department
        self.specialization = specialization
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        info = f"Команда {self.name} (ID - {self.eid}):\n"
        for employee in self.team:
            info = info + employee.get_info() + '\n'
        return info
        # info = f"Команда {self.name} (ID - {self.eid}):\n"
        # info += "\n".join(emp.get_info() for emp in self.team)
        # return info

employee1= Employee('Artem',1)
manager1= Manager('Andrey',2,'Разработка')
technician1= Technician('Igor',3,'Мобильные приложения')
tech_manager1= TechManager('Maksim',4,'Главный','Веб-сайты')
print(employee1.get_info())
print(manager1.manage_project('TikTok'))
print(technician1.perform_maintenance())
tech_manager1.add_employee(employee1)
tech_manager1.add_employee(manager1)
tech_manager1.add_employee(technician1)
print(tech_manager1.get_team_info())
print(TechManager.__mro__)