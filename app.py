from det_eyes import det_eyes

if __name__ == "__main__":
    print("-------------------------------------------")
    print("Welcome to Drossiness Detection Application")
    print("-------------------------------------------")
    print(
        """
    Choose your options:
    1. Detect Eyes
    """
    )
    answer = input("Your option > ")
    if answer == "1":
        COUNTER = 0
        det_eyes()
    else:
        print("Update next season...")
