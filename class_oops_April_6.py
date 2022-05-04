##python is unstructured programming
##python can be made as structured programming if its follows "class" principles
##class is collection of object
##object is real world entity
##class is kind of template or wrapper to hold things
##object is anything which takes memory
##class is mainly to give the properly of inheritance or extensibility

##var ="dhoni"
##print(var)
##
##def fun():
##    print("welcome")
##    
##fun()

##class My_Class:
##
##     var = "dhoni"
##
##     def fun():
##         print("welcome")
##
##print(My_Class.var)
##My_Class.fun()

##class My_Class:
##
##     var = "dhoni"
##
##     def fun():
##         print("welcome")
##
##My = My_Class
##print(My_Class.var)
##My_Class.fun()

##My is called object referance of the "My_Class"
##class without constructor

##class My_Class:
##
##    def new(name):
##        print("hello")
##
##    def fun(name,age):
##        print("welcome")
##
##My = My_Class
##My.fun("dhoni",33)
##My.new("dhoni")

class My_Class:

     def __init__(self,name,age):

         self.name = name
         self.age = age

     def new(self):
          print(self.name)

     def fun(self):
          print(self.name,self.age)

My = My_Class("dhoni",33)
My.fun()
My.new()

##My_Class is called as constructor class
##My is called as object referance with single instant memory(single instant memory)
##My_Class() will have one hidden object inside
##whenever you create constructor , an atrribute called __init__ is created automatically
##we can ues that __init__ if we need to initialize the data inside the class
##attribute or magic method or dunder method is anything that contain double underscore on either side
##self is similar to My
##My is the object referance for external class
##self is the object referance for internal class
My.fun()
My.new()




























