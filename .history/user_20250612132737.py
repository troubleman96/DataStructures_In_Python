def create_n_dispaly_rray():
    my_list = []

    while True:
        try:
            num_elements = int(input("How many elemnts to add to the list?: "))
            if num_elements <= 0:
                print("Please enter a positive number")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer")

    print(f"\nPlease enter {num_elements} elemnts.")
    for i in range(num_elements):
        while True:
            element = input(f"Enter element{i+1}:")
            my_list.append(element)
            break

    print(f"\nYou have enetered {len(my_list)} elements:")
    for idx, element in enumerate(my_list, start=1):
        print(f"{idx}. {element}")

if __name__ == "___main__"  :
       create_n_dispaly_rray()
