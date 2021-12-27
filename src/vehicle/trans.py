from dataclasses import dataclass
from vehicle.vehicle import VehicleChild

@dataclass
class TransmissionInfo:
    """Common Transmission information"""
    model: str
    # Forward gear count, 4-10 common
    gear_count: int
    # list of gears in order of highest ratio to lowest (1st to 6th in a 6 speed)
    gear_ratios: list
    # Gear ratio in reverse: 5.0
    gear_ratio_reverse: float
    # Torque Converter Stall RPM: 1800-3000 common
    stall_rpm: int

    def __str__(self):
        return f'{self.model} {self.gear_count} Speed'

    def create_transmission(self):
        return Transmission(self)


class Transmission(VehicleChild):
    def __init__(self, transmission_info: TransmissionInfo):
        self._info = transmission_info

    @property
    def info(self):
        return self._info
    
    @property
    def gears(self):
        return list(self._info.gear_ratios)