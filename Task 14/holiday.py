#For this task, we need to create a user-defined function that asks user for 3 inputs (city_flight, num-nights
#and rental_days). With this information, we will determine the total budget needed for this holiday trip.
#Paramenters to calculate include: hotel_costs, plane_cost and car_rental.
#Final price calculation will be made with these three parameters, calculated via user-defined function, and 
#the final cost will be calculated via holiday_cost function at the end.

#=====================================================CODE=====================================================#

country_list = ["MANHATTAN", "MADRID", "PARIS", "BERLIN", "EGYPT", "TOKYO", "SYDNEY", "ONTARIO"]
country_hotel_dic = {"MANHATTAN": 260,
                      "MADRID": 82, 
                      "PARIS": 111, 
                      "BERLIN": 95, 
                      "EGYPT": 146, 
                      "TOKYO": 188, 
                      "SYDNEY": 222, 
                      "ONTARIO": 210
                      }
country_flight_dic = {"MANHATTAN": 600,
                      "MADRID": 120, 
                      "PARIS": 150, 
                      "BERLIN": 140, 
                      "EGYPT": 300, 
                      "TOKYO": 800, 
                      "SYDNEY": 1200, 
                      "ONTARIO": 470
                      }
country_rental_dic = {"MANHATTAN": 60,
                      "MADRID": 15, 
                      "PARIS": 20, 
                      "BERLIN": 17, 
                      "EGYPT": 28, 
                      "TOKYO": 37, 
                      "SYDNEY": 55, 
                      "ONTARIO": 42
                      }

city_flight = ""
num_nights = 0
rental_days = 0
total_hotel_cost = 0
total_plane_cost = 0
total_rental_cost = 0
total_holiday_cost = 0

class NegativeNumberException(Exception):
    def __init__(self, value_type, value):
        self.value_type = value_type
        self.value = value
        super().__init__(f"Error: {value} is not a valid entry. {value_type} should be a positive number")

class InvalidEntryError(Exception):
    def __init__(self, incorrect_entry, valid_entries):
        self.incorrect_entry = incorrect_entry
        self.valid_entries = valid_entries
        super().__init__(f"Invalid entry: {incorrect_entry}. Valid entries are {valid_entries}.")

def select_destination():
    while True:
        try:
            city_flight = str(input("\nPlease enter your holiday destination from the given list: ")).upper()
            if not city_flight.isalpha():
                raise ValueError("Please enter the name of your destination")
            
            if city_flight not in country_list:
                raise InvalidEntryError (city_flight, country_list)
            
            break

        except ValueError as ve:
            print(f"Error: {ve}")
        except InvalidEntryError as ie:
            print(ie)

    return city_flight

def trip_duration():
    while True:
        try:
            num_nights = int(input("\nPlease enter how many nights your plan to stay: "))
            if num_nights <0:
                raise NegativeNumberException("Number of nights", num_nights)
            
            break

        except ValueError:
            print("Error: Please enter a number for the duration of your trip")
        except NegativeNumberException as ne:
            print(ne)

    return num_nights

def rental_plan():
    while True:
        try:
            rental_days = int(input("\nPlease enter the number of days you are plan to rent a car, if any: "))
            if rental_days <0:
                raise NegativeNumberException("Number of rental days", rental_days)
            
            break

        except ValueError:
            print("Error: Please enter a number for how many days you want to rent a car")
        except NegativeNumberException as ne:
            print(ne)

    return rental_days

def hotel_cost(nights, destination):
    total_hotel_cost = nights*country_hotel_dic[destination]
    print(f"\nTotal cost for the hotel will be {total_hotel_cost}")

    return total_hotel_cost

def plane_cost(destination):
    total_plane_cost = country_flight_dic[destination]
    print(f"\nTotal cost for the flight will be {total_plane_cost}")

    return total_plane_cost

def car_rental(rental, destination):
    total_rental_cost = rental*country_rental_dic[destination]
    print(f"\nTotal cost for the car rental will be {total_rental_cost}")

    return total_rental_cost

def holiday_cost(x, y, z):
    total_holiday_cost = x + y + z
    print(f"\nIn total, this holiday trip will cost a total of {total_holiday_cost}")

    return total_holiday_cost


print(f"""Hi and welcome to your trip calculator! This program will ask you to enter a destination from our list, 
the number of nights you plan to stay and the number of days you plan to rent a car, if any. Once we have this 
information, we will calculate the and display all the costs of your planned trip.
\nThis is the list of available destinations: {country_list}""")

city_flight = select_destination()
num_nights = trip_duration()
rental_days = rental_plan()
total_hotel_cost = hotel_cost(num_nights, city_flight)
total_plane_cost = plane_cost(city_flight)
total_rental_cost = car_rental(rental_days, city_flight)
total_holiday_cost = holiday_cost(total_hotel_cost, total_plane_cost, total_rental_cost)