##file_obj = open("lavanya.txt","w")
##file_obj.write("indis is my country")
##file_obj.close()

##file_obj = open(r"C:\Users\91897\Documents\lavanya.txt","w")
##file_obj.write("indis is my country")
##file_obj.close()

##file_obj = open("lavanya.txt","w")
##file_obj.write("python programming")
##file_obj.close()

##file_obj = open("lavanya.txt","a")
##file_obj.write("\n")
##file_obj.write("today is tuesday")
##file_obj.close()

##file_obj = open("lavanya.txt","a")
##file_obj.write("\n")
##file_content = input("enter the file content")
##file_obj.write(file_content)
##file_obj.close()

##file_obj = open("lavanya1.txt","x")
##file_obj.write("\n")
##file_content = input("enter the file content")
##file_obj.write(file_content)
##file_obj.close()

##file_obj = open("lavanya.txt","a")
##file_obj.write("\n")
##file_content = input("enter the file content")
##file_obj.writen(file_content)
##file_obj.close()

#context manager

##with open("lavanya.txt","a") as file_obj:
##    file_obj.write("\n")
##    file_content = input("enter the file content")
##    file_obj.write(file_content)
   
##with open("lavanya.txt","r") as file_obj:
##    file_output = file_obj.read()
##    print(file_output)

##with open("lavanya.txt","r") as file_obj:
##    file_output = file_obj.read(5)
####    print(file_output)
##    file_output1 = file_obj.read()
##    print(file_output1)

with open("lavanya.txt","r") as file_obj:
    file_output = file_obj.readline()
    print(file_output)
    file_output1 = file_obj.readline()
    print(file_output1)






















