# Create a list of elements using dict
data = [
    {
        "firstname": "Mark Nicholas",
        "middlename": "Limpin",
        "lastname": "Razon",
        "pin": 8607,
        "balance": 15000,
        "status": "verified",
    },
    {
        "firstname": "Lawrence",
        "middlename": "",
        "lastname": "Amparo",
        "pin": 1974,
        "balance": 20000,
        "status": "verified",
    },
    {
        "firstname": "Jocelyn",
        "middlename": "Dikoalam",
        "lastname": "Padallan",
        "pin": 2849,
        "balance": 25000,
        "status": "not verified",
    }
]

# Create a function for validating 4 digit pin
def validatePin(x):
    # Check if the pin is digit
    if x.isdigit():
        # Check if the length of the pin is 4
        if len(x) == 4:
            # Display all the data from the dict
            for user in data:
                # Check if the input pin is existing in the data
                if user["pin"] == int(x):
                    #print the specific information that contains the input pin
                    print(user["firstname"])
                    print(user["middlename"])
                    print(user["lastname"])
                    print(user["pin"])
                    print(user["balance"])
                    print(user["status"])
                    return
            print("No user found with that pin")
        else:
            print("It's not a 4 digit pin")
    else: 
        print("This is not a number")


# Ask user what is their 4 digit pin
pin = input("Put your 4 digit pin: ")
validatePin(pin)
