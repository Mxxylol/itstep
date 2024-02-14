class Student:
    print("Hi")

    def __init__(self, height = 160):
        self.height = height

nick = Student()
kate = Student(height=160)
bbb = Student(height=99)
print(nick.height)
print(kate.height)
print(bbb.height)