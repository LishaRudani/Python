#scoping

##var = 100 #outside variable(Global)
##def fun():
##    var = 10 #local variable
##    print(var)
##
##print(var)
##fun()
##print(var)

##var = 100 
##def fun():
##    global var
##    var = 10
##    print(var)
##print(var)
##fun()
##print(var)

##counter = 0
##def fun():
##    global counter
##    print("hello",counter)
##    counter = counter+1
##    if counter==101:
##        return
##    fun()
##
##fun()

##while loop
##counter = 0
##def fun():
##    global counter
##    print("hello",counter)
##    counter = counter+1
##    while counter < 101:
##       fun()
##
##fun()

##counter = 0
##def fun():
##    global counter
##    print("hello",counter)
##    counter = counter+1
##    if counter < 101:
##        fun()
##fun()


    
