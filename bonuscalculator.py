salary = int(input("Enter your salary"))
time = int(input("How much time you have spent in this company?"))


if time>10:
    print("you are eligible for 10% bonus and your net bonus amount is", salary+(10/100)*salary)
elif time>6 and time<=10:
    print("you are eligible for 8% bonus and your net bonus amount is", salary+(8/100)*salary)
elif time>0 and time<=6:
    print("you are eligible for 5% bonus and your net bonus amount is", salary+(6/100)*salary)
else:
    print("You are not eligible for bonus, better luck next time")
    