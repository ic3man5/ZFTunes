from dataclasses import dataclass
from vehicle.vehicle import VehicleChild
from vehicle.formulas import calc_oss_from_engine_rpm

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

class Gear(VehicleChild):
    def __init__(self, index, ratio, transmission: Transmission):
        """
        index = gear position 1-10 typical, 0 = reverse
        ratio = float: gear ratio
        trnasmission: Transmission object (requires an attached vehicle)
        """
        self._index = index
        self._ratio = ratio
        self._trans = transmission
    
    @property
    def ratio(self):
        """Returns the gear ratio as a float"""
        return self._ratio
    
    def min_oss(self):
        """Returns the ideal minimum OSS based on engine idle RPM"""
        rpm = self._trans.vehicle.engine.idle_rpm
        oss = calc_oss_from_engine_rpm(rpm, self._ratio)
        return oss
    
    def max_oss(self):
        """Returns the ideal max OSS based on engine idle RPM"""
        rpm = self._trans.vehicle.engine.max_rpm
        oss = calc_oss_from_engine_rpm(rpm, self._ratio)
        return oss

    def peak_hp_oss(self):
        """Returns the ideal OSS based on engine peak horsepower RPM"""
        rpm = self._trans.vehicle.engine.peak_hp_rpm
        oss = calc_oss_from_engine_rpm(rpm, self._ratio)
        return oss
    
    def peak_torque_oss(self):
        """Returns the ideal OSS based on engine peak torque RPM"""
        rpm = self._trans.vehicle.engine.peak_torque_rpm
        oss = calc_oss_from_engine_rpm(rpm, self._ratio)
        return oss
