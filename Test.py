try:
    UserInput=input("Enter value: ")
    numerator = float(UserInput)
    devidedValue = input("Enter Divided value: ")
    denometor = float (devidedValue)

    result = numerator /denometor

    print (f"you entered: Numerator={numerator},denometor={denometor}")
    print(f"result is:{result}")

except ValueError:
    print(f"Invalid Input")
except ZeroDivisionError:
    print(f"Can't Divided by Zero")
except Exception as e:
    print(f"An unexpected Error:{e}")




    

