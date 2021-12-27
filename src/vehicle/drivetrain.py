from dataclasses import dataclass
from vehicle.vehicle import VehicleChild
from vehicle.tire import Tire

@dataclass
class DrivetrainInfo:
    """Common Drivetrain information"""
    axle_ratio: float
    tcase_ratio: float
    tire: Tire

    def __str__(self):
        return f'{self.axle_ratio} Axle with {str(self.tire.diameter)}" tires'

    def create_drivetrain(self):
        return Drivetrain(self)


class Drivetrain(VehicleChild):
    def __init__(self, drivetrain_info: DrivetrainInfo):
        self._info = drivetrain_info

    @property
    def info(self):
        return self._info
    
    @property
    def axle_ratio(self):
        return self._info.axle_ratio

    @property
    def tire(self):
        return self._info.tire
    
    @property
    def tcase_ratio(self):
        return self._info.tcase_ratio
