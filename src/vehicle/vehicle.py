from dataclasses import dataclass
from enum import Enum, auto
from vehicle.formulas import calc_engine_rpm_from_oss, calc_oss_from_mph, calc_mph_from_oss

@dataclass
class VehicleInfo:
    """Common vehicle information"""
    # Vehicle Year: 2009
    year: int
    # Vehicle Make: Chevy
    make: str
    # Vehicle Model: Corvette
    model: str
    # Engine size in liters: 5.3L
    engine_size: float

    def __str__(self):
        return f'{self.year} {self.make} {self.model} {self.engine_size}'
    
    def create_vehicle(self):
        return Vehicle(self)

class InputType(Enum):
    OSS = auto()
    MPH = auto()
    KPH = auto()

OutputType = InputType

class Vehicle(object):
    def __init__(self, vehicle_info: VehicleInfo):
        self._info = vehicle_info
        self._engine = None
        self._transmission = None
        self._tire = None
        self._drivetrain = None
    
    def __str__(self):
        return str(self.info)

    def __repr__(self) -> str:
        return f'<{type(self)} object ({str(self._info)}) at {hex(id(self))}>'
    
    def __check_is_child(self, value):
        if not isinstance(value, VehicleChild):
            raise TypeError(f'Error: object is not of type "{type(VehicleChild)}"')

    @property
    def info(self):
        return self._info

    @property
    def engine(self):
        if not self._engine:
            raise ValueError("engine is not set")
        return self._engine
    
    @engine.setter
    def engine(self, value):
        self.__check_is_child(value)
        value._vehicle = self
        self._engine = value

    @property
    def transmission(self):
        if not self._transmission:
            raise ValueError("transmission is not set")
        return self._transmission
    
    @transmission.setter
    def transmission(self, value):
        self.__check_is_child(value)
        value._vehicle = self
        self._transmission = value

    @property
    def tire(self):
        if not self._tire:
            raise ValueError("tire is not set")
        return self._tire
    
    @tire.setter
    def tire(self, value):
        self.__check_is_child(value)
        value._vehicle = self
        self._tire = value
    
    @property
    def drivetrain(self):
        if not self._drivetrain:
            raise ValueError("drivetrain is not set")
        return self._drivetrain
    
    @drivetrain.setter
    def drivetrain(self, value):
        self.__check_is_child(value)
        value._vehicle = self
        self._drivetrain = value
    
    def get_oss(self, mph):
        return calc_oss_from_mph(mph, self.tire, self.drivetrain.axle_ratio)
    
    def get_rpm(self, oss, gear):
        return calc_engine_rpm_from_oss(oss, self.transmission.gears[gear-1])
    
    def get_mph_from_oss(self, oss):
        return calc_mph_from_oss(oss, self.tire, self.drivetrain.axle_ratio)
    
    def get_rpm_from_mph(self, mph, gear):
        oss = self.get_oss(mph)
        return self.get_rpm(oss, gear)

    



class VehicleChild(object):
    _vehicle = None

    def __repr__(self) -> str:
        return f'<{type(self)} object ({str(self._info)}) at {hex(id(self))}>'

    @property
    def vehicle(self):
        if not self._vehicle:
            raise ValueError("vehicle is not set")
        return self._vehicle
    
    @vehicle.setter
    def vehicle(self, value):
        self._vehicle = value


if __name__ == "__main__":
    corvette_info = VehicleInfo(2019, "Chevy", "Corvette", 5.3, "6L80")
    corvette = Vehicle(corvette_info)
    print(corvette)
