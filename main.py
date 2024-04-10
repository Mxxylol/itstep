# class Student():
#     amount_of_students = 0
#
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_students+=10
#
# nick = Student()
# kate = Student(height=170)
# chiril = Student()
# print(Student.amount_of_students)
# print(kate.height)
#
# class Students:
#     height = 160
#
#     def __init__(self):
#         print(self.height)
#         self.height += 0
#
# nick = Students()
# kate = Students()
#
#
# class Students():
#
#     def __init__(self):
#         self.height = 170
#     height = 160
#
#     def printer(self):
#         print(self.height)
#
# nick = Students()
# nick.printer()
#
#
# x = 10
#
# class Locker:
#     print(x)
#
#     def func_1(self):
#         x = 20
#         print(x)
#
#         def func_2():
#             x = 30
#             print(x)
#
#         func_2()
#
# some_object = Locker()
# some_object.func_1()
#
#
# class Students:
#     amount_of_students = 0
#
#     def __init__(self, height = 260):
#         self.height = height
#         Students.amount_of_students+=1
#
#     def grow(self, height = 1):
#         self.height+=height
#
# nick = Students()
# kate = Students(height=170)
# nick.grow(height = 15)
# print(kate.height)
# print(nick.height)
# print(Students.amount_of_students)
# jora = Students()
# print(Students.amount_of_students)
#
#
# class Students:
#
#     def __init__(self, name=None):
#         self.name = name
#
#     def __str__(self):
#         if self.name:
#             return f"I am a student. My name is {self.name}"
#         else:
#             return "I am a student. I dont have a name."
#
# alice = Students(name = "Alice")
# print(alice)
# jora = Students()
# print(jora)
#
# import random
#
# class Student:
#
#     def __init__(self, name):
#         self.name = name
#         self.gladness = 50
#         self.progress = 0
#         self.alive = True
#
#     def to_study(self):
#         print("Este timpul sa invat")
#         self.progress += 0.12
#         self.gladness -= 5
#
#     def to_sleep(self):
#         print("Voi dormi")
#         self.gladness += 3
#
#     def to_chill(self):
#         print("Timpul de odihna")
#         self.gladness += 5
#         self.progress -= 0.1
#
#
#     def is_alive(self):
#         if self.progress < -0.5:
#             print("DEAD...")
#             self.alive = False
#         elif self.gladness <= 0:
#             print("Depresie...")
#             self.alive = False
#         elif self.progress > 5:
#             print("O murit de fericire")
#             self.alive = False
#
#
#     def end_of_day(self):
#         print(f"Fericire = {self.gladness}")
#         print(f"Progres = {round(self.progress, 2)}")
#
#
#     def live(self, day):
#         day = " Ziua " + str(day) + "din viata lui " + self.name + " "
#         print(f"{day:=^50}")
#         live_cube = random.randint(1, 3)
#         if live_cube == 1:
#             self.to_study()
#         elif live_cube == 2:
#             self.to_sleep()
#         elif live_cube == 3:
#             self.to_chill()
#         self.end_of_day()
#         self.is_alive()
#
# nick = Student(name="Vlad")
#
# for day in range(365):
#     if nick.alive == False:
#         break
#     nick.live(day)

# class Grandparent:
#
#     def about(self):
#         print("I am grandParent")
#     def about_myself(self):
#         print("I am a grandparent")
#
#
#
#
# class Parent(Grandparent):
#
#     def about_myself(self):
#         print("I am parent")
#
# class Child(Parent):
#
#     def __init__(self):
#         super().about()
#         super().about_myself()
#
# nick = Child()
#
#
# class Computer:
#
#     def calculate(self):
#         print("Calculating...")
#
# class Display:
#     def display(self):
#         print("I display the image on the screen")
#
# class smartPhone(Display, Computer):
#     pass
#
# class SmartPhone(Display, Computer):
#     pass
#
# iphone = SmartPhone()
# iphone.calculate()
# iphone.display()
#
# class Computer:
#     def __init__(self):
#         super().__init__()
#         self.memory = 128
#
# class Display:
#     def __init__(self):
#         super().__init__()
#         self.resolution = "4k"
#
# class SmartPhone(Display, Computer):
#
#     def print_info(self):
#         print(self.resolution)
#         print(self.memory)
#
# iphone = SmartPhone()
# iphone.print_info()
#
# class Computer:
#
#     def __init__(self, model, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.model = model
#         self.memory = 128
#
# class Display:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.resolution = "4k"
#
# class SmartPhone(Display, Computer):
#     def print_info(self):
#         print(self.model)
#         print(self.resolution)
#         print(self.memory)

#
# iphone = SmartPhone(model = "Last")
# iphone.print_info()


# try:
#     print("Start code")
#     print(error)
#     print("No errors")
#
# except:
#     print("We have an error")
#
# print("Code after capsule")



# try:
#     print("Start code")
#     print(error)
#     print("No errors")
#
# except NameError:
#     print("We have an NameError")
#
# except ZeroDivisionError:
#     print("We have an ZeroDivisionEror")
#

#
# try:
#     print("start code")
#     print(10/0)
#     print("No errors")
# except (NameError, ZeroDivisionError):
#     print("We have an eror")
#

#
# try:
#     print("start code")
#     print(10/0)
#     print("No errors")
# except (NameError, ZeroDivisionError) as error:
#     print(error)
#
# print("code after capsule")

# try:
#     try:
#         print("start code")
#         print (error)
#         print ("No errors")
#     except SyntaxError:
#         print("Wrong syntax")
# except NameError as error:
#     print (error)

# try:
#     print("Hello")
# except:
#     print("we have a problem")
# else:
#     print("No problem")

#
# try:
#     print("start code")
#     print(error)
#     print("No errors")
# except NameError as error:
#     print(error)
# else:
#     print("I am ELSE!")
# finally:
#     print("Finally code")

#
# def checker(var_1):
#     if type(var_1)!= str:
#         raise TypeError(f"Sorry we cant work with {type(var_1)}, " f"we need class str")
#     else:
#         return var_1
#
# first_var = "Hello"
# # first_var = 10
# checker(first_var)

# class BuildingError(Exception):
#     def __str__(self):
#         return f"With so much material the house cannot be built!"
#
# def check_material(amout_of_material, limit_value):
#     if amout_of_material > limit_value:
#         return "Enough material"
#     else:
#         raise BuildingError(amout_of_material)
#
# materials = 209
# check_material(materials, 300)







# import warnings
#
# warnings.warn("warning, no code here", SyntaxWarning)




# numbers = [1, 2, 3, 4, 5]
# cacat = iter(numbers)
# print(next(cacat))
# print(next(cacat))
# print(next(cacat))
# print(next(cacat))
# print(next(cacat))
# print(next(cacat))

# for num in cacat:
#     print(num)
# for num in cacat:
#     print(num)

# class Counter:
#     def __init__(self, max_number):
#         self.i = 10
#         self.max_number = max_number
#
#     def __iter__(self):
#         self.i = 10
#
#         return self
#
#     def __next__(self):
#         self.i = 0
#
#         return self
#     def elem(self):
#         self.i += 1
#         if self.i > self.max_number:
#
#             raise StopIteration
#
#         return self.i
# count = Counter(5)
# # for elem in count:
# #     print(elem)
#
# print(count.__next__())
# print(count.__next__())
# print(count.__next__())
# print(count.__next__())
# print(count.__iter__())
# print(next(count))
# print(next(count))
# print(next(count))

# def numere_pare(maxim):
#     numar = 0
#     while numar < maxim:
#         yield numar
#
#         numar += 2
#
# for numar in numere_pare(10):
#     print(numar)


# def raise_to_the_degrees(number, max_degree):
#     i=0
#     for A in range(max_degree):
#         yield number**i
#         i+=1
#
# res = raise_to_the_degrees(1222345, 10)
# print(res)
# for A in res:
#     print(A)


# class Helper:
#     def __init__(self, work):
#         self.work = work
#
#     def __call__(self, work):
#         return f"I will help with your {self.work}. Afterwards I will help you with {work}"
# helper = Helper("homework")
# print(helper("cleaning"))
#
# def helper(work):
#     work_in_memory = work
#
#     def asd(work):
#         return f"I will help you with your {work_in_memory}. Afterwards I will help you with {work}"
#     return asd
# helper = helper("homework")
# print(helper("cleaning"))
# print(helper("driving"))

# def checker(function, *args, **kwargs):
#     try:
#         result = function(*args, **kwargs)
#     except Exception as exc:
#         print(f"We have problems {exc}")
#     else:
#         print(f"No problems. Result - {result}")
#
# def calculate(expression):
#     return eval(expression)
#
# checker(calculate, 2+2



#
# import logging

# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")



# logging.basicConfig(level=logging.DEBUG,
#                     filename="logs.log",
#                     filemode="w")
# logging.info("info")
# logging.debug("debug")
# logging.debug("debug")


# logging.basicConfig(level=logging.DEBUG,
#                     filename="logs.log",
#                     filemode="w",
#                     format="We have next logging message:%(asctime)s:%(levelname)s -%(message)s")
# logging.info("info")
# logging.debug("debug")

# import logging
#
# logging.basicConfig(level=logging.DEBUG,
#                     filename="logs.log",
#                     filemode="w",
#                     format="We have next logging message:%(asctime)s:%(levelname)s -%(message)s")
#
# try:
#     print("10/0")
# except Exception:
#     logging.exception("Exception")


# if 2+2==4:
#     print("Its Reel!")
#
# assert 2+2==5, "Its fake!"


# def divide(a, b):
#     assert b != 0, "Division by zero is not allowed!"
#     return a / b
#
# print(divide(10, 2))
# print(divide(10, 0))


# x = 1
# assert x > 10, "x should be positive"
# print(x)




def adder(*args, **kwargs):
    result = 0
    for _ in args:
        if type(_) == int or type(_) == bool or type(_) == float:
            result += _
        else:
            try:
                result+=float(_)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result+=int(_)
                continue
            except (ValueError, TypeError):
                pass
    for _ in kwargs.values():
        if type(_) == int or type(_) == bool or type(_) == float:
            result += _
        else:
            try:
                result += float(_)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(_)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(_)
                continue
            except (ValueError, TypeError):
                pass
    return result