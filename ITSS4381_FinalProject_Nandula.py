#Methods
class ScooterRental():
    def __init__(self, num_scooters, hourly_price, daily_price, weekly_price, discount):
        self.num_scooters = num_scooters
        self.hourly_price = hourly_price
        self.daily_price = daily_price
        self.weekly_price = weekly_price
        self.discount = discount


    def hourlyrent(self, num_scooters, hourly_price, discount):
        if self.num_scooters < 0:
            print("Invalid")
        elif (self.num_scooters == 1 or self.num_scooters == 2) or (self.num_scooters >= 6 and self.num_scooters <= 10):
            return self.num_scooters * hourly_price
        elif self.num_scooters >= 3 and self.num_scooters <= 5:
            return (self.num_scooters * hourly_price) * discount
        elif self.num_scooters > 10: 
            print("Error")

    def dailyrent(self, num_scooters, daily_price, discount):
        if self.num_scooters < 0:
            print("Invalid")
        elif (self.num_scooters == 1 or self.num_scooters == 2) or (self.num_scooters >= 6 and self.num_scooters <= 10):
            return self.num_scooters * daily_price
        elif self.num_scooters >= 3 and num_scooters <= 5:
            return (self.num_scooters * daily_price) * discount
        elif self.num_scooters > 10: 
            print("Error")
        
    def weeklyrent(self, num_scooters, weekly_price, discount):
        if self.num_scooters < 0:
            print("Invalid")
        elif (self.num_scooters == 1 or self.num_scooters == 2) or (self.num_scooters >= 6 and self.num_scooters <= 10):
            return self.num_scooters * weekly_price
        elif self.num_scooters >= 3 and self.num_scooters <= 5:
            return (self.num_scooters * weekly_price) * discount
        elif self.num_scooters > 10: 
            print("Error")

class ScooterReturn(ScooterRental):
    def __init__(self, num_scooters, hourly_price, daily_price, weekly_price, discount):
        super().__init__(num_scooters, hourly_price, daily_price, weekly_price, discount)
    def hourlyrent(self, num_scooters, hourly_price, discount):
        if (self.num_scooters == 1 or self.num_scooters == 2) or (self.num_scooters >= 6 and self.num_scooters <= 10):
            return self.num_scooters * hourly_price
        elif self.num_scooters > 10: 
            return self.num_scooters * hourly_price
        elif self.num_scooters >= 3 and self.num_scooters <= 5:
            return (self.num_scooters * hourly_price) * discount
        else:
            return 0
    def dailyrent(self, num_scooters, daily_price, discount):
        if (self.num_scooters == 1 or self.num_scooters == 2) or (self.num_scooters >= 6 and self.num_scooters <= 10):
            return self.num_scooters * daily_price
        elif self.num_scooters > 10: 
            return self.num_scooters * daily_price
        elif self.num_scooters >= 3 and self.num_scooters <= 5:
            return (self.num_scooters * daily_price) * discount
        else:
            return 0
    def weeklyrent(self, num_scooters, weekly_price, discount):
        if (self.num_scooters == 1 or self.num_scooters == 2) or (self.num_scooters >= 6 and self.num_scooters <= 10):
            return self.num_scooters * weekly_price
        elif self.num_scooters > 10: 
            return self.num_scooters * weekly_price
        elif self.num_scooters >= 3 and self.num_scooters <= 5:
            return (self.num_scooters * weekly_price) * discount
        else:
            return 0


#Results
if __name__ == "__main__":
    hourly_price = 10
    daily_price = 20
    weekly_price = 50
    discount = 0.85

    customer_name = input("Welcome to the Scooter Rental Shop! What is your name?\n")
    user_selection = eval(input(f"Hello {customer_name}, what would you like to do today?\n\t1. Rent a Scooter\n\t2. Return a Scooter\nPlease select '1' or '2' from the above options to continue: "))

    if user_selection == 1:
        num_scooters = eval(input("How many scooters would you like to rent? Please enter a whole number between 1 and 10.\n"))
        scooter_rental = ScooterRental(num_scooters, hourly_price, daily_price, weekly_price, discount)
        rental_type = input("Would you like to rent per hour, per day, or per week?\n")

        if rental_type in ("hour", "Hour", "per hour", "Per Hour"):
            time_amount = eval(input("How many hours?\n"))
            final_price = scooter_rental.hourlyrent(num_scooters, hourly_price, discount)

            if type(final_price) is str:
                print("Invalid number of scooters. Please enter at least one scooter and no more than ten scooters.")
            else:
                print(f"Your total is ${final_price * time_amount} for {num_scooters} scooters for {time_amount} hours. Thanks for your purchase!")

        elif rental_type in ("day", "Day", "per day", "Per Day"):
            time_amount = eval(input("How many days?\n"))
            final_price = scooter_rental.dailyrent(num_scooters, daily_price, discount)

            if type(final_price) is str:
                print("Invalid number of scooters. Please enter at least one scooter and no more than ten scooters.")
            else:
                print(f"Your total is ${final_price * time_amount} for {num_scooters} scooters for {time_amount} days. Thanks for your purchase!")


        elif rental_type in ("week", "Week", "per week", "Per Week"):
            time_amount = eval(input("How many weeks?\n"))
            final_price = scooter_rental.weeklyrent(num_scooters, weekly_price, discount)

            if type(final_price) is str:
                print("Invalid number of scooters. Please enter at least one scooter and no more than ten scooters.")
            else:
                print(f"Your total is ${final_price * time_amount} for {num_scooters} scooters for {time_amount} weeks. Thanks for your purchase!")

        else:
            print("Error: Invalid input. Please enter in the format 'hour', 'Hour', 'per hour' or 'Per Hour'")

    elif user_selection == 2:

        num_scooters = eval(input("How many scooters are you returning?\n"))
        scooter_return = ScooterReturn(num_scooters, hourly_price, daily_price, weekly_price, discount)
        rental_type = input("Did you rent by hour, day, or week?\n")
        
        if rental_type in ("hour", "Hour", "per hour", "Per Hour"):
            time_amount = eval(input("How many hours?\n"))
            final_price = scooter_return.hourlyrent(num_scooters, hourly_price, discount)
            print(f"Your total is ${final_price * time_amount} for {num_scooters} scooters for {time_amount} hours. Thanks for your purchase!")
        elif rental_type in ("day", "Day", "per day", "Per Day"):
            time_amount = eval(input("How many days?\n"))
            final_price = scooter_return.dailyrent(num_scooters, daily_price, discount)
            print(f"Your total is ${final_price * time_amount} for {num_scooters} scooters for {time_amount} days. Thanks for your purchase!")
        elif rental_type in ("week", "Week", "per week", "Per Week"):
            time_amount = eval(input("How many weeks?\n"))
            final_price = scooter_return.weeklyrent(num_scooters, weekly_price, discount)
            print(f"Your total is ${final_price * time_amount} for {num_scooters} scooters for {time_amount} weeks. Thanks for your purchase!")
        else:
            print("Error: Invalid input. Please enter in the format 'hour', 'Hour', 'per hour' or 'Per Hour'")
    else:
        print("Invalid input. Please enter either '1' or '2'.")
        
















        