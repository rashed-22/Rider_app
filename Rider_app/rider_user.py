from abc import ABC, abstractmethod
from datetime import datetime

class Ride_sharing:
    def __init__(self, company) -> None:
        self.company = company
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f'{self.company} with riders: {len(self.rider)} and drivers: {len(self.driver)}'

class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.email = email
        #TODO: set user id dynamically
        self.__id = 0
        self.__nid = nid
        self.wallet = 0
        
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, email, nid, current_location, init_amount) -> None:
        self.current_ride = None
        self.wallet = init_amount
        self.current_location = current_location
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f'Rider: with name: {self.name} and email: {self.email}')

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
    
    def update_location(self, current_location):
        self.current_location = current_location

    def request_ride(self, destination):
        if not self.current_ride:
            # TODO: set ride properly
            # TODO: set current ride via ride match
            ride_request = Ride_request(self, destination)
            ride_matcher = Ride_matching()
            self.current_ride = ride_matcher.find_driver(ride_request)

class Driver(User):
    def __init__(self, name, email, nid, current_location) -> None:
        self.current_location = current_location
        self.wallet = 0
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f'Rider: with name: {self.name} and email: {self.email}')
    
    def accept_ride(self, ride):
        ride.set_driver(self)


class Ride:
    def __init__(self, s_loc, e_loc) -> None:
        self.s_loc = s_loc
        self.e_loc = e_loc
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None
        
    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self, rider, amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

class Ride_request:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location

class Ride_matching:
    def __init__(self) -> None:
        self.available_drivers = []

    def find_driver(self, ride_request):
        if len(self.available_drivers) > 0:
            #todo: find the closest driver of rider
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            return ride
        
class Vehicle(ABC):

    speed = {
        'car': 50,
        'bike': 60,
        'cng': 40
    }

    def __init__(self, type, licence, rate) -> None:
        self.type = type
        self.licence = licence
        self.rate = rate
        self.status = 'available'
        super().__init__()

    @abstractmethod
    def start_drive(self):
        pass

class Car(Vehicle):
    def __init__(self, type, licence, rate) -> None:
        super().__init__(type, licence, rate)

    def start_drive(self):
        self.status = 'unavailable'

class Bike(Vehicle):
    def __init__(self, type, licence, rate) -> None:
        super().__init__(type, licence, rate)

    def start_drive(self):
        self.status = 'unavailable'


# Check the class integration

niye_jao = Ride_sharing('Niye jao')
sakib = Rider('Sakib khan', 'sakib343@gmail.com', 3344, 'Mohakhali', 800)
niye_jao.add_rider(sakib)

kala_pakhi = Driver('Kala Pakhi', 'kalapakhi33@gmail.com', 333, 'Gulshan')
print(niye_jao)