name = "suresh"
age="28"
email="suresh@gmail.com"
company="daimler india "
designation= "engineer"


print("my name is " + name)
print("my age is " +age)
print("my companey is "+company)

formatter=print("my name is "+ name +"and age is "+"28"+"and eamil id is"+email +"and my company is"+company+"and my designation is"+designation)

print(formatter)

formatted="my name is {} and my age is {} and my company is {} and my designation is{}and email id is{}".format(name,age,company,designation,email)
print(formatted)

formatted="my name is {0} and my age is {1} and my company is {2} and my designation is{3}and email id is{4}".format(name,age,company,designation,email)
print(formatted)


formatted="my name is %s and my age is %s and my company is %s and my designation is %s and email id is %s" % (name,age,company,designation,email)
print(formatted)


formatted= f"my name is {name} and my age is {age} and my company is {company} and my designation is{designation}and email id is{email}"
print(formatted)

