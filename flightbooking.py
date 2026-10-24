from abc import ABC, abstractmethod


class Passenger(ABC):

    @abstractmethod
    def get_discount(self):
        pass


class RegularPassenger(Passenger):

    def get_discount(self):
        return 0


class StudentPassenger(Passenger):

    def get_discount(self):
        return 10


class Flight:

    def __init__(self, code, source, destination, seats, fare):
        self.code = code
        self.source = source
        self.destination = destination
        self.seats = seats
        self.fare = fare

    def display_flight(self):
        print(self.code, "|", self.source, "to", self.destination,
              "| Seats:", self.seats, "| Fare:", self.fare)


class Booking:

    def __init__(self, booking_id, flight, name, age, passenger_type,
                 tickets, subtotal, discount, total):
        self.booking_id = booking_id
        self.flight = flight
        self.name = name
        self.age = age
        self.passenger_type = passenger_type
        self.tickets = tickets
        self.subtotal = subtotal
        self.discount = discount
        self.total = total

    def display_summary(self):
        print("\n----- Booking Summary -----")
        print("Booking ID:", self.booking_id)
        print("Flight:", self.flight.code, "|",
              self.flight.source, "to", self.flight.destination)
        print("Passenger:", self.name)
        print("Age:", self.age)
        print("Passenger type:", self.passenger_type)
        print("Tickets:", self.tickets)
        print("Base fare per ticket:", self.flight.fare)
        print("Subtotal:", self.subtotal)
        print("Discount:", self.discount)
        print("Final amount:", self.total)


class FlightBookingSystem:

    def __init__(self):
        self.flights = [
            Flight("PN101", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Mumbai", "Bengaluru", 25, 3500),
            Flight("PH303", "Pune", "Hyderabad", 15, 3000)
        ]

        self.bookings = []
        self.booking_number = 1001

    def display_flights(self):

        print("\n----- Available Flights -----")

        for flight in self.flights:
            flight.display_flight()

    def find_flight(self, code):

        for flight in self.flights:

            if flight.code.upper() == code.upper():
                return flight

        return None

    def validate_booking(self, flight, name, age, tickets):

        if flight is None:
            print("Booking failed: Flight code does not exist.")
            return False

        if name.strip() == "":
            print("Booking failed: Passenger name cannot be blank.")
            return False

        if age <= 0:
            print("Booking failed: Age must be greater than 0.")
            return False

        if tickets <= 0:
            print("Booking failed: Ticket count must be greater than 0.")
            return False

        if tickets > flight.seats:
            print("Booking failed: Not enough seats available.")
            return False

        return True

    def calculate_fare(self, flight, tickets, passenger):

        subtotal = flight.fare * tickets

        discount_percent = passenger.get_discount()

        discount = subtotal * discount_percent / 100

        total = subtotal - discount

        return subtotal, discount, total

    def confirm_booking(self, flight, name, age, passenger_type,
                        tickets, passenger):

        subtotal, discount, total = self.calculate_fare(
            flight, tickets, passenger
        )

        flight.seats = flight.seats - tickets

        booking_id = "BK" + str(self.booking_number)

        self.booking_number = self.booking_number + 1

        booking = Booking(
            booking_id,
            flight,
            name,
            age,
            passenger_type,
            tickets,
            subtotal,
            discount,
            total
        )

        self.bookings.append(booking)

        print("\nBooking confirmed!")

        booking.display_summary()

    def book_flight(self):

        self.display_flights()

        code = input("\nEnter flight code: ")
        flight = self.find_flight(code)

        name = input("Enter passenger name: ")

        try:
            age = int(input("Enter age: "))
            tickets = int(input("Enter number of tickets: "))
        except ValueError:
            print("Please enter numbers for age and tickets.")
            return

        passenger_type = input(
            "Passenger type (Regular/Student): "
        )

        if passenger_type.lower() == "student":

            passenger = StudentPassenger()
            passenger_type = "Student"

        elif passenger_type.lower() == "regular":

            passenger = RegularPassenger()
            passenger_type = "Regular"

        else:
            print("Invalid passenger type.")
            return

        if self.validate_booking(flight, name, age, tickets):

            self.confirm_booking(
                flight,
                name,
                age,
                passenger_type,
                tickets,
                passenger
            )

    def view_bookings(self):

        if len(self.bookings) == 0:
            print("\nNo bookings available.")
        else:

            print("\n----- All Bookings -----")

            for booking in self.bookings:
                booking.display_summary()

    def start(self):

        while True:

            print("\n==============================")
            print("Welcome to Kiran Air Booking")
            print("==============================")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":

                self.display_flights()

            elif choice == "2":

                self.book_flight()

            elif choice == "3":

                self.view_bookings()

            elif choice == "4":

                print("\nThank you for using Kiran Air Booking!")
                break

            else:

                print("Invalid choice. Please try again.")


system = FlightBookingSystem()
system.start()