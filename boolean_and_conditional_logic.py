#user input
age=input("How old are you: ")
if age:
    age = int(age)

    if age >= 18 and age < 21:
        print(f"You are {age} years old, you can enter.")

    elif age>=21:
        print(f"You are {age} years old, you can enter and drink.")

    elif age<18:
        print(f"You are {age} years old, you can not enter.")

else:
    print("Please enter a valid age.")

 