while True:
    print("CAB BOOKING CHATBOT")
    print("1.book a cab")
    print("2.exit")

    choice=int(input("enter your choice:"))

    if choice == 2:
        print("thank you for using cab booking chatbot.")

        break
    if choice != 1:
        print("invalid choice. please try again.")
        continue

    print("\n----select route----")
    print("1.pune to shivajinagar-5km")
    print("2.pune to kothure-8km")
    print("3.pune to wakad-10km")

    route=int(input("enter route choice:"))
    if route == 1:
        distance=5
        route_name="pune to shivajinagar"
    elif route == 2:
        distance=8
        route_name="pune to kothure"
    elif route == 3:
        distance=10
        route_name="pune to wakad"
    else:
        print("invalid route choice.")
        continue

    print("\n----select cab----")
    print("1.auto - rs.12/km")
    print("2.sedan - rs.18/km")
    print("3.suv - rs..25/km")

    cab=int(input("enter cab choice:"))
    if cab == 1:
        rate = 12
        cab_name = "auto"
    elif cab == 2:
        rate = 18
        cab_name = "sedan"
    elif cab == 3:
        rate = 25
        cab_name = "suv"
    else:
        print("invalid cab choice.")
        continue

    fare = distance*rate
    print("\n----booking details----")
    print("route:",route_name)
    print("cab:",cab_name)
    print("distance:",distance,"km")
    print("fare:rs.",fare)

    cancel=input("\n do you want to cancel the booking(yes/no):")
    if cancel.lower() == "yes":
        print("booking cancelled successfully.")
        continue

    otp = 1234
    print("\n otp has been shared.")
    print("your otp is:",otp)
    entered_otp = int(input("enter otp:"))
    if entered_otp == otp:
        print("\n otp verified successfully.")
        print("cab booked successfully!")
        print("final fare:rs.",fare)
    else:
        print("\n invalid otp.")
        print("booking failed.")
        
print("cancellation is not allowed after otp sharing.")
again=input("\n do you want to continue(yes/no):")
if again.lower() == "no":
    print("thank you for using cab booking chatbot.")
    