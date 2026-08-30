def get_numbers():
    """
    Reads numbers from the user until 'done' is entered.
    Returns the total, count, and average of the numbers entered.
    """
    total = 0
    count = 0

    while True:
        user_input = input("Enter a number (or 'done' to finish): ")

        if user_input == 'done':
            break

        try:
            number = float(user_input)
            total += number
            count += 1
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    if count > 0:
        average = total / count
        return total, count, average
    else:
        return None

result = get_numbers()

if result:
    total, count, average = result
    print("Total:", total)
    print("Count:", count)
    print("Average:", average)
else:
    print("No numbers entered.")
