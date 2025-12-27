class LotFullException(Exception):
    """Raised when parking lot is full"""
    pass


class Vehicle:
    def __init__(self, id_plate, parked_hours):
        self.id_plate = id_plate
        self.parked_hours = parked_hours


class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass


class ParkingLot:
    def __init__(self, total_slots=5):
        self.total_slots = total_slots
        self.active_slots = {}  # slot_number: Vehicle

    def park_vehicle(self, vehicle):
        if len(self.active_slots) >= self.total_slots:
            raise LotFullException("Sorry! Parking lot is full.")

        for slot_num in range(1, self.total_slots + 1):
            if slot_num not in self.active_slots:
                self.active_slots[slot_num] = vehicle
                print(f"{vehicle.id_plate} parked at slot {slot_num}")
                return

    def remove_vehicle(self, id_plate):
        for slot_num, vehicle in self.active_slots.items():
            if vehicle.id_plate == id_plate:
                fee = vehicle.parked_hours * 2
                del self.active_slots[slot_num]
                print(f"Vehicle {id_plate} removed from slot {slot_num}")
                print(f"Parking Fee: ${fee}")
                return
        print(f"Vehicle {id_plate} not found in the lot.")


# -------- Example Usage --------
if __name__ == "__main__":
    lot = ParkingLot(5)

    try:
        lot.park_vehicle(Car("CAR001", 4))
        lot.park_vehicle(Bike("BIKE99", 3))
    except LotFullException as e:
        print(e)

    lot.remove_vehicle("CAR001")
    lot.remove_vehicle("BIKE99")
