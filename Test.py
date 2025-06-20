
class NagNumError(ValueError):
    """Custom exception raised when a negative number is entered."""
    def returnError(ValueError):
        print(ValueError)

def get_positive_number():
    """Ask the user for a number and raise a negative number error if needed."""

    while True:
         try:
             num_str = input("Please Enter zpositive Number: ")
             number= float(num_str)

             if number<0:
                 raise NagNumError("Number Must be Positive")
             return number
         except ValueError:
             print("Invalid input. Please enter a valid number.")
         except NagNumError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    try:
        positive_Num = get_positive_number()
        print(f"You entered a positive number: {positive_Num}")
    except NagNumError as e:
        print(f"Caught an error in the main script: {e}")
    except Exception as e:
        print("An unexpected error occurred.")


