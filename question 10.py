
cinema_seats = [[0 for _ in range(5)] for _ in range(5)]

def display_seats():
    print("\nCurrent Seat Layout (0 = Available, 1 = Booked):")
    for row_index, row in enumerate(cinema_seats):
        print(f"Row {row_index}:", row)
    print()

def book_seat():
    try:
        row = int(input("Enter the row number (0-4): "))
        col = int(input("Enter the seat number in the row (0-4): "))

        if 0 <= row < 5 and 0 <= col < 5:
            if cinema_seats[row][col] == 0:
                cinema_seats[row][col] = 1
                print(f"Seat at Row {row}, Column {col} booked successfully!")
            else:
                print("Oops! That seat is already booked.")
        else:
            print("Invalid row or column number. Try again.")
    except ValueError:
        print("Please enter valid numbers only.")


while True:
    print("\n--- Movie Theater Seat Booking ---")
    print("1. Book a Seat")
    print("2. Show Seats")
    print("3. Exit")

    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        book_seat()
    elif user_choice == "2":
        display_seats()
    elif user_choice == "3":
        print("Thank you for using the Seat Booker!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
