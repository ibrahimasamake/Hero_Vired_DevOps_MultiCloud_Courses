for i in range(5):
    print("Iteration:", i)


for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")


while True:
    user_input = input("Enter 'exit' to stop the loop: ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break
    else:
        print("You entered:", user_input)