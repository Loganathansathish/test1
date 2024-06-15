# string handling
userName = 'sathish'
print(userName)

a="suresh"

b="sathish"
print("before-->",b)

print(b)

b=a

b="santhosh"
print("after-->",b)
print(b)
#indexing-getting the charactor in the given string based on the index number
name ="suresh"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

# negative indexing -indexing with negative numbers
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])

#slicing
print(name[0:4])
print(name[0:3])
print(name[0:2])
print(name[0:1])
print(name[0:5])

#name=suresh
print(name[-4:-1])
print(name[-4:-3])
print(name[-5:-1])

print(name[2:100])
print(name[-2:-100])
print(name[0:100])
print(name[0:30])
print(name[3:100])
print(name[3:15])
print(name[0:8])
#ranging -postive& negative we can use
print(name[1:])
print(name[4:])
print(name[-4:])
print(name[-2:])
print(name[-1:])
print(name[-3:])
print(name[-2:])

#string formatting..

#manual formatting
#automatic formatting

#concatation-adding two string with+ operator
name="suresh"
age= 23
email="suresh@gmail.com"

print("my name is" +name)

formatted= print("my name is" + name + "and age is"+"23"+"and gmail id is"+email)
formatted= "my name is" + " " +  name  + "" + "and age is" + "23" 
print(formatted)
#automatic formatting

formatter= "my name is {} and my age is {} and email id is {} ".format(name,age,email) 
print(formatter)

#manual formatting

formatter= "my name is {0} and my age is {1} and email id is{2} ".format(name,age,email)
print(formatter)

formatter="my name is %s and age is %s and email id is %s" % (name,age,email)
print(formatter)

formatting = f"may name is {name} and age is {age} and email is {email}"
print(formatting)





