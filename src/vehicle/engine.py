from dataclasses import dataclass
from vehicle.vehicle import VehicleChild

@dataclass
class EngineInfo:
    """Common Engine information"""
    # RPM the engine idles at
    idle_rpm: str
    # max RPM (Rev limiter)
    max_rpm: int
    # RPM where horsepower is the highest
    peak_hp_rpm: int
    # RPM where torque is the highest
    peak_torque_rpm: int
    # Torque Converter Stall RPM: 1800-3000 common

    def __str__(self):
        return f'{self.model} {self.gear_count} Speed'

    def create_engine(self):
        return Engine(self)


class Engine(VehicleChild):
    def __init__(self, engine_info: EngineInfo):
        self._info = engine_info

    @property
    def info(self):
        return self._info
    
    @property
    def idle_rpm(self):
        return self._info.idle_rpm
    
    @property
    def max_rpm(self):
        return self._info.max_rpm
    
    @property
    def peak_hp_rpm(self):
        return self._info.peak_hp_rpm

    @property
    def peak_torque_rpm(self):
        return self._info.peak_torque_rpm