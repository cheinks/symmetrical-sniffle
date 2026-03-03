import math

loop = True
while loop:
    # Setup
    prompt = "\nEnter a decimal value. Then specify the number of trailing digits that repeat."
    # user_input = [""] * 2
    repeat = 0  # The number of digits that repeat, counting from the right
    no_repeat = 0  # The number of digits between the decimal point and the repeated portion
    valid = True

    # Process the user input
    user_input = [input(prompt + "\n> "), input("> ")]
    # user_input[0] = input(prompt + "\n> ")
    if "q" in user_input:
        quit(0)
    # First value must be a decimal
    try:
        x = float(user_input[0])
    except ValueError:
        print("First value must be a decimal!")
        valid = False
    # Second value must be a positive integer
    try:
        repeat = int(user_input[1])
    except ValueError:
        print("Second value must be a positive integer!")
        valid = False

    # Determine the first scale factor
    [whole, decimal] = ["", ""]
    try:
        [whole, decimal] = user_input[0].split(".", 1)
    except ValueError:
        print("Decimal places insufficient!")
        valid = False

    if valid:
        scale_1 = len(decimal)  # Move one period of the repeating part in front of the decimal point
        scale_1 = 10 ** scale_1

        # Determine the second scale factor
        no_repeat = len(decimal) - repeat
        scale_2 = 10 ** no_repeat

        # Perform the algebra
        top = int(whole + decimal)
        top -= int(whole + decimal[:no_repeat])
        bottom = scale_1 - scale_2

        # Simplify the fraction
        gcd = math.gcd(top, bottom)
        top = int(top / gcd)
        bottom = int(bottom / gcd)

        # Display result
        print("\nYour number is " + whole + "." + decimal + ". The equivalent fraction is " +
              str(top) + " / " + str(bottom) + ".")
        print(float(top) / bottom)