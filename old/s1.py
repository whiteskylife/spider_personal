#!/usr/bin/env python
# -*-coding:utf-8 -*-

# import redis
# pool = redis.ConnectionPool(host='192.168.1.110', port=6379, password='redis-pass')
# conn = redis.Redis(connection_pool=pool)
# conn.publish('fm104.5', '1111')
import json

# html='''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.__class__.__class__.__class__.__class__)
# ret = soup.find_all('ul')
# for i in ret:
#     print(i.find_all('li'))
#     for m in i.find_all('li'):
#         print(m.find('li'))
# import logging
#
# # logging.basicConfig(level=logging.DEBUG)
#
# logger = logging.getLogger('spider1')
# logger.setLevel(logging.INFO)
#
# handler = logging.FileHandler('hello.log', encoding='utf-8')
# handler.setLevel(logging.INFO)
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
#
# # add the handlers to the logger
#
# logger.addHandler(handler)
#
# logger.info('Hello baby')
# logger.error('error-- 中文')
#
# import os
# logging.basicConfig(filename=os.path.join(os.getcwd(),'log.txt'),level=logging.DEBUG)
# logging.debug('this is a message')
# import os
# if not os.path.exists('stat_log'):
#     os.mkdir('stat_log')
# with open('stat_log/log.txt', 'a') as f:
#     f.write('asd')
#
# import logging

# a = logging.error('asd')
# import threading
#
# class Foo:
#     # def __call__(self, *args, **kwargs):
#     #     print('asasdasdasd')
#
#     def __new__(cls, *args, **kwargs):
#         print('=============')
#         return type.__new__(cls, *args, **kwargs)
#
#
#     def test(self):
#         print('in the test')
#
#
# obj = Foo()
# obj.test()




import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance


class Foo(Singleton):
    def test(self):
        print('1111111111111111')


# a = Foo()
# b = Foo()
# print(a)
# print(b)
#
#


# obj1 = Singleton()
# obj2 = Singleton()
# print(obj1,obj2)



'''

# 私有方法
# 使用场景：第三方短信接口：
class Message:
    # 私有方法
    def __send_msg(self):
        print('--------正在发送短信---------')

    # 公有方法：
    def send_msg(self, new_money):
        if new_money > 10000:
            self.__send_msg()
        else:
            print('余额不足，请先充值，再发送短信')

obj = Message()
obj.send_msg(1000000)
# 小结：实际开发中如果一个类中的方法前面有两个下划线，表示这个方法比较重要，不想让它在外面直接被调用；
# 而是间接在类中调用私有方法
# 注意：私有方法、私有属性都不会被继承（父代的小秘密不会告诉传递给子代-  -！），但当私有属性、方法存在于父类的公有方法中时，则可以通过调用父类公有方法的方式来调用

# __del__方法：
class Dog:

    def __del__(self):              # 对象被回收之前调用
        print('------Game Over-----')

dog1 = Dog()
dog2 = dog1
del dog1
del dog2         # 对象引用计数为0时，python自动执行类中的__del__方法
print('=================')


# 多态：函数或类都可以当做变量传递
class Dog(object):
    def print_self(self):
        print('大家好，我是xxxx，多多关照')


class Xiaotq(Dog):
    def print_self(self):
        print('hello everybody, i am the boss')


def introduce(temp):  # temp可能调用基类的方法，也有可能调用子类的方法，introduce执行的时候才能确定调的哪个方法
    temp.print_self()


dog1 = Dog()
dog2 = Xiaotq()
introduce(dog2)

# 小结：定义一个函数的时候不知道调用的谁，可能存在多种调用情况，只有当程序执行的一刹那才知道调用谁


#  多继承：__mro__用法：多继承情况下可以查看类的对象搜索方法时的先后顺序
class base(object):
    def test(self):
        print('----base test----')
class A(base):
    def test(self):
        print('----A test----')

# 定义一个父类
class B(base):
    def test(self):
        print('----B test----')

# 定义一个子类，继承自A、B
class C(A,B):
    pass


obj_C = C()
obj_C.test()

print(C.__mro__) #可以查看C类的对象搜索方法时的先后顺序
#----A test----
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.base'>, <class 'object'>)





# 类属性，实例属性
class People(object):
    country = 'china'

    def get(self):
        return People.country
p = People()
print(p.get())
p.country = 'asdasdda'
p2 = People()
print(p2.country)
print(p.country)
# 小结：
# 如果需要在类外修改类属性，必须通过类对象去引用然后进行修改。如果通过实例对象去引用，会产生一个同名的实例属性，这种方式修改的是实例属性，不会影响到类属性，
# (对其他实例化对象无影响)，并且之后如果通过实例对象去引用该名称的属性，实例属性会强制屏蔽掉类属性，即引用的是实例属性，除非删除了该实例属性。


# 静态方法、类方法，区别：
class Game(object):

    #类属性
    num = 0

    #实例方法
    def __init__(self):
        #实例属性
        self.name = "laowang"

    #类方法，属于类，通过类调用，和实例对象关系不大，无需传递self，必须传递cls
    @classmethod
    def add_num(cls):
        cls.num = 100

    # 静态方法，可以通过类或实例对象调用，但和类、实例对象关系都不大，可以不传递任何参数（self,cls）
    @staticmethod
    def print_menu():
        print("----------------------")
        print("    穿越火线V11.1")
        print(" 1. 开始游戏")
        print(" 2. 结束游戏")
        print("----------------------")

game = Game()
#Game.add_num()#可以通过类的名字调用类方法
game.add_num()#还可以通过这个类创建出来的对象 去调用这个类方法
print(Game.num)

#Game.print_menu()#通过类 去调用静态方法
game.print_menu()#通过实例对象 去调用静态方法

# 小结：
# 开发中，类方法常用于修改类属性， 实例方法（__init__）常用于修改实例属性， 当需要在类中实现一个简单功能，和类、实例都没关系，这时候就用静态方法
# 类属性、类方法都是属于类的，尽量通过类去调用



# __new__ 方法的使用,python中对象由类的__new__方法创建, 在类中重写__new__方法时，一定要返回父类的__new__方法完成对象创建功能

class Dog(object):
    def __init__(self):
        print("----init方法-----")

    def __del__(self):
        print("----del方法-----")

    def __str__(self):
        print("----str方法-----")
        return "对象的描述信息"

    def __new__(cls):   # 重写父类的new方法，必须要返回父类的new方法完成对象的创建，cls此时是Dog指向的那个类对象

        #print(id(cls))
        print("----new方法-----")
        return object.__new__(cls)      # 调用父类的__new__完成对象创建

#print(id(Dog))

xtq = Dog()
# 经历的步骤：
# 1.寻找并调用__new__方法创建对象，找一个变量接收__new__的返回值，返回值表示创建出来的对象的引用
# 2 __init__(self),self表示刚刚创建出来的对象的引用

# 小结：
# __new__方法：创建，专门用来实例化创建对象，每一个对象被创建实例化都是通过类中的__new__方法
# 实例化对象的时候，调用__init__()初始化之前，先调用了__new__()方法
# __new__()方法：必须要有返回值，返回实例化出来的实例，需要注意的是，可以return父类__new__()出来的实例，也可以直接将object的__new__()出来的实例返回。
# __init__()有一个参数self，该self参数就是__new__()返回的实例，__init__()在__new__()的基础上可以完成一些其它初始化的动作




# __new__方法的应用：创建单例模式

# class Dog(object):
#
#     __instance = None
#
#     def __new__(cls):
#         if cls.__instance == None:
#             cls.__instance = object.__new__(cls)
#             return cls.__instance
#         else:
#             #return 上一次创建的对象的引用
#             return cls.__instance
#
# class Poo(Dog):
#
#     def test(self):
#         print('123')
#
# a = Poo()
# print(id(a))
# b = Poo()
# print(id(b))





# __call__方法的使用：
class Test(object):
    def __call__(self, *args, **kwargs):        # 有__call__的类对象可以直接被调用
        print('-----test-----')

t = Test()
t()


# ----------类装饰器--------
class Test(object):
    def __init__(self, func):
        print("---初始化---")
        print("func name is %s" % func.__name__)        # func.__name__ 表示函数名
        self.__func = func

    def __call__(self):
        print("---装饰器中的功能---")
        self.__func()


@Test           # 相当于 test = Test(test)， 执行test()相当于执行类装饰器中的__call__方法
def test():
    print("----test---")


test()          # 相当于调用Test(test)(),即执行类装饰器的call方法



# __metaclass__属性
# 你可以在定义一个类的时候为其添加__metaclass__属性。

# class Foo(object):
#     __metaclass__ = something…
    # ...省略...
# 如果你这么做了，Python就会用元类来创建类Foo。小心点，这里面有些技巧。你首先写下class Foo(object)，但是类Foo还没有在内存中创建。
# Python会在类的定义中寻找__metaclass__属性，如果找到了，Python就会用它来创建类Foo，如果没有找到，就会用内建的type来创建这个类。把下面这段话反复读几次。当你写如下代码时 :

# class Foo(Bar):
#     pass
# Python做了如下的操作：
#
# 1、Foo中有__metaclass__这个属性吗？如果是，Python会通过__metaclass__创建一个名字为Foo的类(对象)
# 2、如果Python没有找到__metaclass__，它会继续在Bar（父类）中寻找__metaclass__属性，并尝试做和前面同样的操作。
# 3、如果Python在任何父类中都找不到__metaclass__，它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作。
# 4、如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象。
# 现在的问题就是，你可以在__metaclass__中放置些什么代码呢？答案就是：可以创建一个类的东西。那么什么可以用来创建一个类呢？type，或者任何使用到type或者子类化type的东东都可以。



# 自定义元类
# 元类的主要目的就是为了当创建类时能够自动地改变类。通常，你会为API做这样的事情，你希望可以创建符合当前上下文的类。
# 假想一个很傻的例子，你决定在你的模块里所有的类的属性都应该是大写形式。有好几种方法可以办到，但其中一种就是通过在模块级别设定__metaclass__。采用这种方法，这个模块中的所有类都会通过这个元类来创建，我们只需要告诉元类把所有的属性都改成大写形式就万事大吉了。
# 幸运的是，__metaclass__实际上可以被任意调用，它并不需要是一个正式的类。所以，我们这里就先以一个简单的函数作为例子开始。

# python2中：__metaclass__
#-*- coding:utf-8 -*-
def upper_attr(future_class_name, future_class_parents, future_class_attr):

    #遍历属性字典，把不是__开头的属性名字变为大写
    newAttr = {}
    for name,value in future_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value

    #调用type来创建一个类
    return type(future_class_name, future_class_parents, newAttr)

class Foo(object):
    __metaclass__ = upper_attr #设置Foo类的元类为upper_attr
    bar = 'bip'

print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

f = Foo()
print(f.BAR)

# python3中 :metaclass代替__metaclass__
#-*- coding:utf-8 -*-
def upper_attr(future_class_name, future_class_parents, future_class_attr):

    #遍历属性字典，把不是__开头的属性名字变为大写
    newAttr = {}
    for name,value in future_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value

    #调用type来创建一个类
    return type(future_class_name, future_class_parents, newAttr)

class Foo(object, metaclass=upper_attr):
    bar = 'bip'

print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

f = Foo()
print(f.BAR)


# 现在让我们再做一次，这一次用一个真正的class来当做元类。

#coding=utf-8

class UpperAttrMetaClass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情
    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        #遍历属性字典，把不是__开头的属性名字变为大写
        newAttr = {}
        for name,value in future_class_attr.items():
            if not name.startswith("__"):
                newAttr[name.upper()] = value

        # 方法1：通过'type'来做类对象的创建
        # return type(future_class_name, future_class_parents, newAttr)

        # 方法2：复用type.__new__方法
        # 这就是基本的OOP编程，没什么魔法
        # return type.__new__(cls, future_class_name, future_class_parents, newAttr)

        # 方法3：使用super方法
        return super(UpperAttrMetaClass, cls).__new__(cls, future_class_name, future_class_parents, newAttr)

#python2的用法
class Foo(object):
    __metaclass__ = UpperAttrMetaClass
    bar = 'bip'

# python3的用法
# class Foo(object, metaclass = UpperAttrMetaClass):
#     bar = 'bip'

print(hasattr(Foo, 'bar'))
# 输出: False
print(hasattr(Foo, 'BAR'))
# 输出:True

f = Foo()
print(f.BAR)
# 输出:'bip'
#
# 就是这样，除此之外，关于元类真的没有别的可说的了。但就元类本身而言，它们其实是很简单的：
#
# 拦截类的创建
# 修改类
# 返回修改之后的类
# 究竟为什么要使用元类？
#
# 现在回到我们的大主题上来，究竟是为什么你会去使用这样一种容易出错且晦涩的特性？好吧，一般来说，你根本就用不上它：
#
# “元类就是深度的魔法，99%的用户应该根本不必为此操心。如果你想搞清楚究竟是否需要用到元类，那么你就不需要它。那些实际用到元类的人都非常清楚地知道他们需要做什么，而且根本不需要解释为什么要用元类。” —— Python界的领袖 Tim Peters




# python垃圾回收：
# ⼩整数[-5,257)共⽤对象，常驻内存
# 单个字符共⽤对象，常驻内存
# 单个单词，不可修改，默认开启intern机制，共⽤对象，引⽤计数为0，则销毁

# GC系统所承担的⼯作远⽐"垃圾回收"多得多。实际上，它们负责三个重要任务。它们为新⽣成的对象分配内存，识别那些垃圾对象，并且
# 从垃圾对象那回收内存

#  引⽤计数机制：
# python⾥每⼀个东⻄都是对象，当⼀个对象有新的引⽤时，它的计数就会增加，当引⽤它的对象被删除，它的引用计数就会减少，
# 当引⽤计数为0时，该对象⽣命就结束了

# 循环引⽤：
# list1 = []
# list2 = []
# list1.append(list2)
# list2.append(list1)
# list1与list2相互引⽤，如果不存在其他对象对它们的引⽤，list1与list2的引⽤计数也仍然为1，所占⽤的内存永远⽆法被回收，
# 这将是致命的。 对于如今# 的强⼤硬件，缺点1尚可接受，但是循环引⽤导致内存泄露，注定python还将引⼊新的回收机制。(分代收集)

# 引用计数为主，隔代回收为辅（解决引用计数的循环引用问题），完成所有对象的垃圾回收
'''
