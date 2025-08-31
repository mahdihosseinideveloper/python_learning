import math
print(2+2)

count = 10
score = 9.5
finished = True  # True | False
full_name = "Mahdi \" \' \\ \n next line Hosseini"
line_by_line_text = """ 
this is first line
this is second line
this is third line
"""
formulla = 1 + 2j
print(count)
count = count + 5
print(count)
print(line_by_line_text)
print(len(line_by_line_text))
print(full_name[0])
print(full_name[-1])
print(full_name[0:6])
print(full_name[6:])
print(full_name[:6])


print(type(formulla))

name = "mahdi"
last_name = "hosseini"

my_full_name = name + " " + last_name
print(my_full_name)
my_full_name_fs = f"{name} hahahah {last_name} -- {2+2}"  # formating string
print(my_full_name_fs)


# method
print(name.upper())
print(name.lower())
print(name.title())  # capitalize the first letter

random_text = "   test empty space    "
print(random_text.strip())  # remove empty space
print(random_text.rstrip())
print(random_text.lstrip())

# find
print(random_text.find("tes"))
print("test" in random_text)  # True false
print("test" not in random_text)  # True false

# replace
print(random_text.replace("test", "jest"))  # jest empty space


# numbers
a = 1
b = 20
print(b//4)  # عدد صحیح
print(4**22.8)  # به توان رسوندن
print(round(4**22.8))
print(math.pi)
print(math.sin(90))


first = "1"
second = 0
print(int(first) + second)
print(str(second) + first)
print(float(first))
print(bool(second))
