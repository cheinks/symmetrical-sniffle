def test_conjecture(given):
    value = int(given)
    running = True
    print("Given: " + given)
    print()
    i = 0
    while running:
        if value % 2 == 0:
            value = int(value / 2)
        else:
            value *= 3
            value += 1
        print(value)
        if value == 1:
            running = False
        i += 1
    print()
    print("True")
    print("Iterations: " + str(i))
    print()


testing = True
while testing:
    number = input("Enter a whole number: ")
    if number == 'q':
        testing = False
    else:
        test_conjecture(number)
