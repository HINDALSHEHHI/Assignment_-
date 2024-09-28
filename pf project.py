# Customer class
class Customer:
    def __init__(self, customer_id, name, email, contact_number):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.contact_number = contact_number
        self.reservation_list = []  # A list to store customer reservations

    # Getter methods
    def get_customer_id(self):
        return self.customer_id

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_contact_number(self):
        return self.contact_number

    # Setter methods
    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_contact_number(self, contact_number):
        self.contact_number = contact_number

    def make_reservation(self, reservation):
        self.reservation_list.append(reservation)
        print(f"Reservation {reservation.reservation_id} made for {self.name}")

    def cancel_reservation(self, reservation):
        if reservation in self.reservation_list:
            self.reservation_list.remove(reservation)
            print(f"Reservation {reservation.reservation_id} canceled for {self.name}")

    def view_reservations(self):
        for reservation in self.reservation_list:
            print(f"Reservation ID: {reservation.reservation_id}, Room ID: {reservation.room.room_id}, Status: {reservation.status}")

    def view_room_details(self, room):
        print(room.view_details())


# Room class
class Room:
    def __init__(self, room_id, room_type, price_per_night, availability, features):
        self.room_id = room_id
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.availability = availability
        self.features = features

    # Getter methods
    def get_room_id(self):
        return self.room_id

    def get_room_type(self):
        return self.room_type

    def get_price_per_night(self):
        return self.price_per_night

    def get_availability(self):
        return self.availability

    def get_features(self):
        return self.features

    # Setter methods
    def set_room_id(self, room_id):
        self.room_id = room_id

    def set_room_type(self, room_type):
        self.room_type = room_type

    def set_price_per_night(self, price):
        self.price_per_night = price

    def set_availability(self, availability):
        self.availability = availability

    def set_features(self, features):
        self.features = features

    def update_availability(self, availability):
        self.availability = availability

    def view_details(self):
        return (f"Room {self.room_id}: {self.room_type}, "
                f"Price: ${self.price_per_night} per night, "
                f"Available: {self.availability}, Features: {self.features}")


# Reservation class
class Reservation:
    def __init__(self, reservation_id, check_in_date, check_out_date, room, status):
        self.reservation_id = reservation_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.room = room
        self.status = status

    # Getter methods
    def get_reservation_id(self):
        return self.reservation_id

    def get_check_in_date(self):
        return self.check_in_date

    def get_check_out_date(self):
        return self.check_out_date

    def get_room(self):
        return self.room

    def get_status(self):
        return self.status

    # Setter methods
    def set_reservation_id(self, reservation_id):
        self.reservation_id = reservation_id

    def set_check_in_date(self, check_in_date):
        self.check_in_date = check_in_date

    def set_check_out_date(self, check_out_date):
        self.check_out_date = check_out_date

    def set_room(self, room):
        self.room = room

    def set_status(self, status):
        self.status = status

    def confirm_reservation(self):
        self.status = "Confirmed"
        print(f"Reservation {self.reservation_id} confirmed.")

    def cancel_reservation(self):
        self.status = "Cancelled"
        print(f"Reservation {self.reservation_id} canceled.")


# Receptionist class
class Receptionist:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def check_in(self, reservation):
        print(f"Customer checked in with reservation ID: {reservation.reservation_id}.")



# Admin class
class Admin:
    def __init__(self, admin_id, name):
        self.admin_id = admin_id
        self.name = name

    def update_room_details(self, room, new_price, new_availability):
        room.update_price(new_price)
        room.update_availability(new_availability)
        print(f"Room {room.room_id} details updated: Price - {new_price}, Available - {new_availability}.")


# Payment class
class Payment:
    def __init__(self, payment_id, amount, payment_method, payment_date, status, reservation_id):
        self.payment_id = payment_id
        self.amount = amount
        self.payment_method = payment_method
        self.payment_date = payment_date
        self.status = status
        self.reservation_id = reservation_id

    # Getter and Setter methods
    def get_payment_id(self):
        return self.payment_id

    def set_payment_id(self, payment_id):
        self.payment_id = payment_id

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def process_payment(self):
        self.status = "Processed"
        print(f"Payment of ${self.amount} for reservation {self.reservation_id} processed successfully.")

    def generate_receipt(self):
        return f"Receipt for Payment ID {self.payment_id}: Amount: ${self.amount}, Status: {self.status}."

    def check_payment_status(self):
        return self.status
Section 2: Object Creation and Populating Information
def main():
   
    room1 = Room(101, "Single", 100, True, "WiFi, TV, AC")
    room2 = Room(102, "Double", 150, True, "WiFi, TV, AC, Mini-Bar")

    customer = Customer(1, "John Doe", "john@example.com", "123456789")
    receptionist = Receptionist(2001, "Alice")
    admin = Admin(3001, "Manager")

    while True:
        choice = display_menu()

        if choice == '1':
            reservation = Reservation(1001, "2024-09-20", "2024-09-25", room1, "Pending")
            customer.make_reservation(reservation)

        elif choice == '2':
            customer.view_room_details(room1)

        elif choice == '3':
            if customer.reservation_list:
                customer.cancel_reservation(customer.reservation_list[0])
            else:
                print("No reservation to cancel.")

        elif choice == '4':
            if customer.reservation_list:
                receptionist.check_in(customer.reservation_list[0])
            else:
                print("No reservation to check-in.")

        elif choice == '5':
            admin.update_room_details(room1, 120, False)

        elif choice == '6':
            if customer.reservation_list:
                payment = Payment(5001, 600, "Credit Card", "2024-09-19", "Pending", customer.reservation_list[0].reservation_id)
                payment.process_payment()
                print(payment.generate_receipt())
            else:
                print("No reservation to process payment for.")

        elif choice == '7':
            customer.view_reservations()

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


