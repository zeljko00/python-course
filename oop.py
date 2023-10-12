class Test_class:
    class_prop=0
    def __init__(self,id, value):
        # leading underscore in attribute name is convention for attributes intended to be private
        self._id=id
        self.value=value
        Test_class.class_prop+=1
    def method(self):
        print("Test_class method call!")

        print("Accessing class' attribute from method ->",Test_class.class_prop)
        # accessing class' attribute via object reference is possible, but not recommended
        print("Accessing class' attribute from method via object reference ->",self.class_prop)

        print("Accessing static method from method ->")
        Test_class.helper_static_method()
        # accessing static methods via object reference is possible, but not recommended
        print("Accessing static method from method via object reference ->")
        self.helper_static_method()

        print("Accessing class method from method ->")
        Test_class.helper_class_method()
        # accessing class methods via object reference is possible, but not recommended
        print("Accessing class method from method via object reference ->")
        self.helper_class_method()

        print("Accessing object's attribute from method ->",self.value)
        # accessing object attribute via class name is not possible,
        # because object attribute is connected to specific class instance (object)
        # print("Accessing object's attribute from method via class name ->",Test_class.value)

        print("Accessing object's method from another method ->")
        self.helper_method()
        # accessing method via class name is not possible
        # print("Accessing object's method from another method via class name->")
        # Test_class.helper_method()

        print("Accessing object's property from method ->", self.helper_prop)
        # accessing property via class name return reference to the property function
        print("Accessing object's property from method via class name->", Test_class.helper_prop)


    def helper_method(self):
        print("Test_class helper_method call!")

    @staticmethod
    def static_method():
        print("Test_class static method call!")

        print("Accessing class' attribute from static method ->", Test_class.class_prop)

        print("Accessing static method from another static method ->")
        Test_class.helper_static_method()

        print("Accessing class method from static method ->")
        Test_class.helper_class_method()

        # self reference is not accessible from static method
        # print("Accessing class' attribute from static method via object reference ->", self.class_prop)
        # print("Accessing static method from another static method via object reference->")
        # self.helper_static_method()
        # print("Accessing class method from static method via object reference ->")
        # self.helper_class_method()
        # print("Accessing object's attribute from static method ->", self.value)
        # print("Accessing object' method from static method")
        # self.helper_method()
        # print("Accessing object's property from static method ->", self.helper_prop)

        # accessing object's attributes, properties and methods via class name is not possible from anywhere
        # print("Accessing object's attribute from static method ->", Test_class.value)
        # print("Accessing object' method from static method")
        # Test_class.helper_method()

        # accessing property via class name return reference to the property function
        print("Accessing object's property from static method via class name->", Test_class.helper_prop)

    @staticmethod
    def helper_static_method():
        print("Test_class helperstatic method call!")

    @classmethod
    def class_method(cls):
        print("Test_class class method call!")

        print("Accessing class' attribute from class method ->", Test_class.class_prop)

        print("Accessing static method from class static method ->")
        Test_class.helper_static_method()

        print("Accessing class method from another class method ->")
        Test_class.helper_class_method()

        # self reference is not accessible from class method
        # print("Accessing class' attribute from class method via object reference ->", self.class_prop)
        # print("Accessing static method from class method via object reference->")
        # self.helper_static_method()
        # print("Accessing class method from another class method via object reference ->")
        # self.helper_class_method()
        # print("Accessing object's attribute from class method ->", self.value)
        # print("Accessing object' method from class method")
        # self.helper_method()
        # print("Accessing object's property from class method ->", self.helper_prop)

        # accessing object's attributes, properties and methods via class name is not possible from anywhere
        # print("Accessing object's attribute from class method ->", Test_class.value)
        # print("Accessing object' method from class method")
        # Test_class.helper_method()

        # accessing property via class name return reference to the property function
        print("Accessing object's property from class method via class name->", Test_class.helper_prop)

    @classmethod
    def helper_class_method(cls):
        print("Test_class helper class method call!")

    @property
    def prop(self):
        print("Test_class property call!")

        print("Accessing class' attribute from property ->", Test_class.class_prop)
        # accessing class' attribute via object reference is possible, but not recommended
        print("Accessing class' attribute from property via object reference ->", self.class_prop)

        print("Accessing static method from property ->")
        Test_class.helper_static_method()
        # accessing static methods via object reference is possible, but not recommended
        print("Accessing static method from property via object reference ->")
        self.helper_static_method()

        print("Accessing class method from property ->")
        Test_class.helper_class_method()
        # accessing class methods via object reference is possible, but not recommended
        print("Accessing class method from property via object reference ->")
        self.helper_class_method()

        print("Accessing object's attribute from property ->", self.value)
        # accessing object attribute via class name is not possible,
        # because object attribute is connected to specific class instance (object)
        # print("Accessing object's attribute from property via class name ->", Test_class.value)

        print("Accessing object's method from property ->")
        self.helper_method()
        # accessing method via class name is not possible
        # print("Accessing object's method from property via class name->")
        # Test_class.helper_method()


        # accessing property via class name return reference to the property function
        print("Accessing object's property from property via class name->", Test_class.helper_prop)

        print("Accessing object's property from another property ->", self.helper_prop)
        return self.helper_prop  # property should return some value

    @property
    def helper_prop(self):
        print("Test_class helper property call!")
        return "#"+str(self.value)

    @property
    def id(self):
        print("Test_class id property call!")
        return self._id
    # setter must have same name as corresponding property
    @id.setter
    def id(self,value):
        print("Test_class id setter call!")
        self._id=value

# specifying str(object) behavior, equivalent to toString() method in Java
    def __str__(self):
        return str(self._id)+": value="+str(self.value)

from abc import ABCMeta, abstractmethod,abstractproperty
class Abstract_class:
    __metaclass__=ABCMeta
    @abstractmethod
    def f(self, arg):
        pass
    @abstractproperty
    def prop(self,velue):
        pass
class A(Abstract_class):
    def f(self, arg):
        print(arg)
    def prop(self,value):
        print(value)







test_object=Test_class(13,"VALUE")
Test_class.static_method()
# accessing static method via object reference is not recommended
test_object.static_method()
Test_class.class_method()
# accessing class method via object reference is not recommended
test_object.class_method()
print(Test_class.class_prop)
# accessing class attribute via object reference is not recommended
print(test_object.class_prop)
print(test_object.value)
# accessing object attribute via class name is not possible
# print(Test_class.value)
test_object.method()
# accessing method via class name is not possible
# Test_class.method()
print(test_object.prop)
print(test_object.id)
# using setter method
test_object.id=113
print(test_object.id)

# object is implemented as dictionary
print(test_object.__dict__)
# object is connected with its class via __class__ attribute
print(test_object.__class__)
# class is also implemented as dictionary
print(test_object.__class__.__bases__)

a=A()
print(a.prop)

print(isinstance(test_object,object))


