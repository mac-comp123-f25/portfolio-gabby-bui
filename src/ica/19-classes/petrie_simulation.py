import random

class Employee:
    """
    For this simulation, we only focus on the gender of an employee, and on
    whether this employee is likely to make negative statements
    towards the other gender.
    """
    def __init__(self, gender, will_comment):
        """
        Takes in the employee's gender and whether they comment, and it
        saves those values to instance variables. It also initializes the
        """
        self.gender = gender
        self.will_comment = bool(will_comment)
        self.comments_received = 0


    def set_commenter_status(self, status):
        self.will_comment = bool(status)


    def receive_sexist_comment(self):
        self.comments_received += 1


    def get_gender(self):
        return self.gender


    def get_commenter_status(self):
        return self.will_comment


    def get_comments_received(self):
        return self.comments_received


    def receive_comments(self):
        self.comments_received += 1


    def comment_on(self, other):
        if self.will_comment and other is not self and other.gender != self.gender:
            self.comments_made += 1
            other.receive_comment()


    def reset(self):
        self.comments_received = 0
        self.comments_made = 0


    def __str__(self):
        """Return a readable string about this employee."""
        comment_status = "commenter" if self.will_comment else "non-commenter"
        return (f"{self.gender} ({comment_status}): "
                f"{self.comments_received} sexist comments received")


def print_employee_list(lst):
    for emp in lst:
        print(emp)


def create_employees(n):
    num_men = (n*80) // 100
    num_women = n - num_men
    employees = []
    for _ in range(num_men):
        employees.append(Employee('Man', False))
    for _ in range(num_women):
        employees.append(Employee('Woman', False))
    return employees


def create_commenters(lst):
    for emp in lst:
        if random.random() < 0.2:
            emp.set_commenter_status(True)


def generate_comments(lst):
    male_employees = []
    female_employees = []
    for emp in lst:
        if emp.gender == 'male':
            male_employees.append(emp)
        else:
            female_employees.append(emp)

    for emp in male_employees:
        if emp.get_commenter_status():
            target = random.choice(female_employees)
            target.receive_sexist_comment()

    for emp in female_employees:
        if emp.get_commenter_status():
            target = random.choice(male_employees)
            target.receive_sexist_comment()

def average_comment(lst):
    comments_male_employees = []
    comments_female_employees = []
    for emp in lst:
        if emp.gender == 'Man' and emp.get_commenter_status():
            comments_male_employees.append(emp)
        else:
            if emp.gender == 'Woman' and emp.get_commenter_status():
                comments_female_employees.append(emp)

    comments_male_employees_average = sum(comments_male_employees) / len(comments_male_employees) if comments_male_employees else 0
    comments_female_employees_average = sum(comments_female_employees) / len(comments_female_employees) if comments_female_employees else 0

    return (comments_male_employees_average, comments_female_employees_average)


lst = [Employee('Man', True),
       Employee('Man', False),
       Employee('Woman', True),
       Employee('Woman', False)]

employees = create_employees(10)
print_employee_list(employees)

