class SchoolMember:
    '''Presents any member'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(School member {0} was created)'.format(self.name))
    def tell(self):
        '''Info print'''
        print('name: {0}, age: {1}'.format(self.name, self.age), end=" ")
class Teacher (SchoolMember):
    '''Presents teachers'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Teacher {0} was created'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Salary :{0:d}'.format(self.salary))
class Student(SchoolMember):
    '''Present student'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Student {0} was created'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('eval: {0:d}'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()

members = [t, s]
for member in members:
    member.tell()