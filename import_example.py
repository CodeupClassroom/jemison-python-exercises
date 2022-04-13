def add(a, b):
    """takes in two numbers and returns the sum"""
    return a + b


def multiply(a, b):
    """multiplies two numbers"""
    return a * b


# Only run the following code if I specifically run the script from the terminal
if __name__ == '__main__':
    # Setting up manual tests
    user_number1 = int(input("Please input a number"))
    user_number2 = int(input("Please input another number"))

    print(f"{user_number1} * {user_number2} is {multiply(user_number1, user_number2)}")

    print("Thanks for running my code!")

    # More automated tests
    assert add(2, 3) == 5
    assert multiply(2, 3) == 6
    print("Automated tests ran appropriately")



