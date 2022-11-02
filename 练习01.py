# a=open('zoutbrassicaceae_AT5G60390.3-2.txt', 'r')
# b=open('zoutbrassicaceae_AT5G60390.3-3.txt', 'w')
# seq={}
# #下面的这个for循环其实就是一个生成字典的过程，需要仔细品味，领悟
# for line in a:
#     if line.startswith('>'):    #判断字符串是否以‘>开始’
#         name=line.split()[0]    #以空格为分隔符，并取序列为0的项。
#         seq[name]=''
#     else:
#         seq[name]+=line.replace('\n', '')#str.replace(old, new[, max]);old -- 将被替换的子字符串;new -- 新字符串，用于替换old子字符串;max -- 可选字符串, 替换不超过 max 次
#         # print(name)
# # print(seq.keys())
# a.close()
#
# for i in seq.keys():
#     b.write(i+":")#注意windows上面需要用加上"\n",当在linux上运行时，不用加"\n"
#     # fw.write('\n')
#     b.write(seq[i]+"\n")
#     # fw.write('\n')
# # f.close()

#############################################
# a=open("002.txt","r")
# b=open("003.txt","r")
# # c=open("004.txt","w")
# a1=a.readlines()
# b1=b.readlines()
# c=a1+b1
# print("\n".join(c))
# print(c)
##########################
# 函数学习
# def describe_pet(animal_type,pet_name):
#     '''显示宠物的信息'''
#     print("I have a "+animal_type+".")
#     print("My "+animal_type+" 's name is "+pet_name.title()+".")
# describe_pet('dog','harry')

####
#调用函数多次是一种效率极高的工作方式
# def describe_pet(pet_name,animal_type='dog'):
#     print('I have a '+animal_type+'.')
#     print('My '+animal_type+" 's name is "+pet_name.title()+".")
# describe_pet(pet_name="tom",animal_type="cat")

#############
#接受名和姓并返回整洁的姓名
# def get_formatted_name(first_name,last_name):
#     full_name=first_name+' '+last_name
#     return full_name.title()
# musician=get_formatted_name('jim','tom')
# print(musician)

#让实参变得可选
# def get_formated_name(first_name,last_name,middle_name=''):
#     if middle_name:
#         full_name=first_name+' '+middle_name+' '+last_name
#     else:
#         full_name=first_name+''+last_name
#     return full_name.title()
# musician=get_formated_name('a','b',middle_name='c')
# print(musician)

########################
# def get_formated_name(first_name,last_name,middle_name=''):
#     if middle_name:
#         full_name=first_name+' '+middle_name+' '+last_name
#     else:
#         full_name=first_name+''+last_name
#     return full_name.title()
# while True:
#     print("Please tell me your name: ")
#     print("(enter 'q' at any time to quit it)")
#     f_name=input("first name: ")
#     if f_name=='q':
#         break
#     l_name=input("last name: ")
#     if l_name=='q':
#         break
#     formatted_name=get_formated_name(f_name,l_name)
#     print("Hello, "+formatted_name+"!")

######################################
# 为重新组织这些代码，我们可编写两个函数，每个都做一件具体的工作。大部分代码都与原来相同，只是效率更高。
# 第一个函数将负责处理打印设计的工作，而第二个将概述打印了哪些设计：

# def print_models(unprinted_designs, completed_models):
#     """
#     模拟打印每个设计，直到没有未打印的设计为止
#     打印每个设计后，都将其移到列表completed_models中
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         # 模拟根据设计制作3D打印模型的过程
#         print("Printing model: "+current_design)
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     """显示打印好的所有模型"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

#######################################################

# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
# Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。

# 例如，如果前面的函数还需要一个表示比萨尺寸的实参，必须将该形参放在形参*toppings的前面：

# def make_pizza(size, *toppings):
#     """概述要制作的比萨"""
#     print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- "+topping)
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

###############################################################
# 有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。
# 在这种情况下，可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少。
# 一个这样的示例是创建用户简介：你知道你将收到有关用户的信息，但不确定会是什么样的信息。
# 在下面的示例中，函数build_profile()接受名和姓，同时还接受任意数量的关键字实参：
# def build_profile(first, last, **user_info):
#     """创建一个字典，其中包含我们知道的有关用户的一切"""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# print(user_profile)

##################################################################
# 接下来，我们在pizza.py所在的目录中创建另一个名为making_pizzas.py的文件，
# 这个文件导入刚创建的模块，再调用make_pizza()两次：
# import pizza
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#####################################################################
# 下面来编写一个表示汽车的类，它存储了有关汽车的信息，还有一个汇总这些信息的方法：

# class Car():
#     """一次模拟汽车的简单尝试"""
#     def __init__(self, make, model, year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_name = str(self.year)+' '+self.make+' '+self.model
#         return long_name.title()
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())

# 下面来添加一个名为odometer_reading的属性，其初始值总是为0。
# 我们还添加了一个名为read_odometer()的方法，用于读取汽车的里程表：

# class Car():
#     def __init__(self, make, model, year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#             """返回整洁的描述性信息"""
#             long_name = str(self.year)+' '+self.make+' '+self.model
#             return long_name.title()
#     def read_odometer(self):
#         """打印一条指出汽车里程的消息"""
#         print("This car has "+str(self.odometer_reading)+" miles on it.")
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading=23
# my_new_car.read_odometer()

####################################################################
# 如果有替你更新属性的方法，将大有裨益。这样，你就无需直接访问属性，而可将值传递给一个方法，由它在内部进行更新。
# 下面的示例演示了一个名为update_odometer()的方法：

# class Car():
#     def __init__(self, make, model, year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#             """返回整洁的描述性信息"""
#             long_name = str(self.year)+' '+self.make+' '+self.model
#             return long_name.title()
#     def read_odometer(self):
#         """打印一条指出汽车里程的消息"""
#         print("This car has "+str(self.odometer_reading)+" miles on it.")
#         # odometer="This car has " + str(self.odometer_reading) + " miles on it."
#         # return odometer
#     def update_odometer(self, mileage):
#         """将里程表读数设置为指定的值"""
#         self.odometer_reading = mileage
# my_new_car = Car('audi', 'a4', 2016)
# # print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

##################################################
# 可对方法update_odometer()进行扩展，使其在修改里程表读数时做些额外的工作。下面来添加一些逻辑，禁止任何人将里程表读数往回调：

# class Car():
#     def __init__(self, make, model, year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#             """返回整洁的描述性信息"""
#             long_name = str(self.year)+' '+self.make+' '+self.model
#             return long_name.title()
#     def read_odometer(self):
#         """打印一条指出汽车里程的消息"""
#         print("This car has "+str(self.odometer_reading)+" miles on it.")
#         # odometer="This car has " + str(self.odometer_reading) + " miles on it."
#         # return odometer
#     def update_odometer(self, mileage):
#         """
#         将里程表读数设置为指定的值
#         禁止将里程表读数往回调
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         """将里程表读数增加指定的量"""
#         self.odometer_reading+=miles
#
#
# my_used_car = Car('subaru', 'outback', 2013)
# print(my_used_car.get_descriptive_name())
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

############################################################

# 下面来创建一个简单的ElectricCar类版本，它具备Car类的所有功能：
# electric_car.py

# class Car():
#     """一次模拟汽车的简单尝试"""
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         long_name = str(self.year)+' '+self.make+' '+self.model
#         return long_name.title()
#     def read_odometer(self):
#         print("This car has "+str(self.odometer_reading)+" miles on it.")
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#     def increment_odometer(self, miles):
#         self.odometer_reading+= miles
# class ElectricCar(Car):
#     """电动汽车的独特之处"""
#     def __init__(self, make, model, year):
#         """初始化父类的属性"""
#         super().__init__(make, model, year)
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())

#######################################################
# 下面来添加一个电动汽车特有的属性（电瓶），以及一个描述该属性的方法。
# 我们将存储电瓶容量，并编写一个打印电瓶描述的方法：

# class Car():
#     """一次模拟汽车的简单尝试"""
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         long_name = str(self.year)+' '+self.make+' '+self.model
#         return long_name.title()
#         # print(long_name.title())
#     def read_odometer(self):
#         print("This car has "+str(self.odometer_reading)+" miles on it.")
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#     def increment_odometer(self, miles):
#         self.odometer_reading+= miles
# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         """
#         电动汽车的独特之处
#         初始化父类的属性，再初始化电动汽车特有的属性
#         """
#         super().__init__(make, model, year)
#         self.battery_size = 70
#     def describe_battery(self):
#         """打印一条描述电瓶容量的消息"""
#         print("This car has a "+str(self.battery_size)+"-kWh battery.")
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# # my_tesla.get_descriptive_name()
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()

####################################################
# 例如，不断给ElectricCar类添加细节时，我们可能会发现其中包含很多专门针对汽车电瓶的属性和方法。
# 在这种情况下，我们可将这些属性和方法提取出来，放到另一个名为Battery的类中，
# 并将一个Battery实例用作ElectricCar类的一个属性：

# class Car():
#     """一次模拟汽车的简单尝试"""
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         long_name = str(self.year)+' '+self.make+' '+self.model
#         return long_name.title()
#         # print(long_name.title())
#     def read_odometer(self):
#         print("This car has "+str(self.odometer_reading)+" miles on it.")
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#     def increment_odometer(self, miles):
#         self.odometer_reading+= miles
# class Battery():
#     """一次模拟电动汽车电瓶的简单尝试"""
#     def __init__(self, battery_size=70):
#         """初始化电瓶的属性"""
#         self.battery_size = battery_size
#     def describe_battery(self):
#         """打印一条描述电瓶容量的消息"""
#         print("This car has a "+str(self.battery_size)+"-kWh battery.")
#
# class ElectricCar(Car):
#     """电动汽车的独特之处"""
#     def __init__(self, make, model, year):
#         """
#         初始化父类的属性，再初始化电动汽车特有的属性
#         """
#         super().__init__(make, model, year)
#         self.battery = Battery()
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()

##################################################
# 下面再给Battery类添加一个方法，它根据电瓶容量报告汽车的续航里程：

class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
        # print(long_name.title())
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading+= miles
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a "+str(self.battery_size)+"-kWh battery.")
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately "+str(range)
        message+= " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()