##var ={}
##print(var)
##print(type(var))

##var = {"name":"dhoni","age":33}
##print(var)
##print(type(var))

#var = {"name":"dhoni","age":33}
##print(var[0])  #no index based direct data retrival in dictionary

##var = {"name":"dhoni","age":33}
##print(var["age"])

##var = {"name":"dhoni","age":33}
##var["name"]="kohli"
##print(var)

#in dictionary datas are manipulated or used via key
#dictionary is called key value pair
#because each data we use needs to be stored with specific key
#storing data with key is generally called "Hashing"or "HashTable"
# Keys are unique
#Dictionary is called as "Un ordered collection"

##var = {"name":"dhoni",9:33,98.9:"arjun",("a","B"):"veena",True:"rahul"}
##var["name"]="kohli"
##print(var)

##var ={"name":"dhoni","team":"csk"}
##var1 ={"age":33}
##var2 ={"lan":"eng"}
##output = {**var,**var1,**var2} ##important
##print(output)

#var = {"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
#print(var)


#var = {"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
#var["name"][1]="rohit"
#print(var)

#var = {"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
#output = var["country"]
#print(output)

#var = {"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
#output = var.get("country")
#print(output)
#print("welcome")

var = {"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
output = var.get("country","key not found")
print(output)
print("welcome")










































