class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def open_seats():
        return self.capacity - len(self.passengers)

    def add_passenger(self, name):
        if Flight.open_seats == 0:
            return False
        self.passengers.append(name)
        return True
    
n=Flight(3)
passengers = ["Harry", "Rob", "Tibi"]
print(passengers[0])
print(passengers[1])
print(passengers[2])
for person in passengers:
    success = Flight.add_passenger(n,person)
    if success:
        print(f"Passenger {person} has an allocated seat.")
    else:
        print(f"No more seats available. Passenger {person} couldn't have been added")




