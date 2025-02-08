class Employee:
    def __init__(self, name, employee_id, salary, department):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.department = department

    def display_employee_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")
        print(f"Department: {self.department}")

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department, team_size=0):
        super().__init__(name, employee_id, salary, department)
        self.team_size = team_size
        self.team_members = []

    def display_manager_info(self):
        self.display_employee_info()
        print(f"Team Size: {self.team_size}")
        print("Team Members:", ", ".join(self.team_members) if self.team_members else "No team members yet")

    def add_team_member(self, name):
        self.team_members.append(name)
        self.team_size += 1
        print(f"{name} has been added to your team.")

    def remove_team_member(self, name):
        if name in self.team_members:
            self.team_members.remove(name)
            self.team_size -= 1
            print(f"{name} has been removed from your team.")
        else:
            print(f"{name} is not in your team.")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"{self.name}'s salary has been updated to ${new_salary}.")

employee1 = Employee("Alice Johnson", "E123", 50000, "Finance")
employee1.display_employee_info()
print()

manager1 = Manager("Bob Smith", "M456", 80000, "Engineering")
manager1.display_manager_info()
print()

manager1.add_team_member("Charlie Brown")
manager1.add_team_member("David Green")
print()
manager1.display_manager_info()
print()

manager1.remove_team_member("Charlie Brown")
manager1.update_salary(85000)
print()
manager1.display_manager_info()
