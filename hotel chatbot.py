def hotel_chatbot():
    print("Welcome to our hotel!")

    while True:
        print("\nHow can I assist you today?")
        print("Please select from the following options:")
        print("1. Room booking")
        print("2. Dining services")
        print("3. Spa and wellness")
        print("4. Other facilities")
        print("5. Contact customer service")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print("\nOur hotel offers the following room types:")
            print("- Standard room")
            print("- Deluxe room")
            print("- Suite")

            room_type = input("Please select the room type you are interested in: ")
            print(f"Great! Let me help you with booking a {room_type}.")

            check_in_date = input("Enter your check-in date (MM/DD/YYYY): ")
            check_out_date = input("Enter your check-out date (MM/DD/YYYY): ")
            num_guests = input("How many guests will be staying? ")

            print("\nThank you for providing the booking details.")
            print(f"I have noted your request for a {room_type} from {check_in_date} to {check_out_date} for {num_guests} guests.")
            print("One of our customer service representatives will be in touch with you shortly to confirm the booking.")

            while True:
                another_request = input("\nDo you need anything else? (yes/no) ")
                if another_request.lower() == "yes":
                    break
                elif another_request.lower() == "no":
                    print("\nThank you for visiting our hotel. Have a wonderful day!")
                    return
                else:
                    print("Invalid input. Please try again.")

        elif choice == "2":
            print("\nOur dining services include:")
            print("- Restaurant")
            print("- Bar")
            print("- Room service")

            dining_service = input("Please select the dining service you are interested in: ")
            print(f"Wonderful! Let me provide you with more details about our {dining_service}.")
            # Add code to handle dining services

        elif choice == "3":
            print("\nOur spa and wellness facilities include:")
            print("- Spa treatments")
            print("- Fitness center")
            print("- Swimming pool")

            spa_service = input("Please select the spa or wellness service you are interested in: ")
            print(f"Excellent! Let me assist you with booking your {spa_service}.")
            # Add code to handle spa and wellness services

        elif choice == "4":
            print("\nOther facilities at our hotel include:")
            print("- Conference rooms")
            print("- Business center")
            print("- Concierge services")

            other_service = input("Please select the other facility you are interested in: ")
            print(f"Great! Let me provide you with more information about our {other_service}.")
            # Add code to handle other hotel services

        elif choice == "5":
            print("\nPlease contact our customer service team at the following number: 555-555-5555")
            print("One of our representatives will be happy to assist you.")

        elif choice == "6":
            print("\nThank you for visiting our hotel. Have a wonderful day!")
            break

        else:
            print("Invalid choice. Please try again.")

hotel_chatbot()
