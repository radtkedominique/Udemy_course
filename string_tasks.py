#function that casts a string to lower
x = "Hai"

def string_to_lower_case (input_string: str):
    lower_case_string = input_string.lower()
    return lower_case_string

print (string_to_lower_case(x))

#print out second character of a string
print(x[1])

#loop through all characters of a string
for a in x:
    print (a)

#length of a string
len(x)

#make upper or lower case
x.upper()
x.lower()

#check if in text
check = "H" in x
print(check)

#check if not
check2 = "H" not in x
print(check2)

#slicing
#characters from start to position 5
b = "Slice this"
print(b[:5])
#from position 2 on
print(b[2:])

#negative indexing
print(b[-4:])

#remove white spaces
b.strip()

#replace string
b.replace("S", "J")

#split string at " "
b.split(" ")

a=b
a=print(b)

#format
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Display with two decimals
{price:.2f}

