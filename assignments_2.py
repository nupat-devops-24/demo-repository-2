total = 0
count = 0

while True:
    num_input = input("Enter a number (or 'done' to finish): ")
    
    if num_input.lower() == 'done':
        break
    
    try:
        num = float(num_input)
    except ValueError:
        print("Error: Please enter a valid number or 'done'.")
        continue
    
    total += num
    count += 1

if count > 0:
    average = total / count
    print("Total:", total)
    print("Count:", count)
    print("Average:", average)
else:
    print("No numbers entered.")
