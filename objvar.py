class Robot:
        '''Present robot with name'''
        # var of class, include value of robots
        population = 0

        def __init__(self, name):
            '''Initializing data'''
            self.name = name
            print('(initialize {0}'.format(self.name))

            # when robots create, he adds to var 'population'
            Robot.population += 1
        
        def __del__(self):
            '''Im dying'''
            print('{0} deleting!'.format(self.name))
            Robot.population -= 1

            if Robot.population == 0:
                print('{0} was a last robot'.format(self.name))
            else:
                print('Value of robots {0:d}'.format(Robot.population))
        def sayHi(self):
            '''Hello robot
            Yes, they can'''
            print('Hello! I am {0}'.format(self.name))
        def howMany():
            '''value of robots'''
            print('We have {0:d} robots'.format(Robot.population))
        howMany = staticmethod(howMany)
droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()
droid2 = Robot('C3PO')
droid2.sayHi()
Robot.howMany()
print("\nHere robots can do something\n")
print("robots success they works. Lets destroy them")
del droid1
del droid2

Robot.howMany()