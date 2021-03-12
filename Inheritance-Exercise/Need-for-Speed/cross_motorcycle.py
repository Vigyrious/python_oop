from Restaurant.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = super().DEFAULT_FUEL_CONSUMPTION
