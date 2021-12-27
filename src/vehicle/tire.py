from dataclasses import dataclass
import re
from vehicle.vehicle import VehicleChild
from vehicle.formulas import cm_to_in

class TireInfo:
    # Tire size = 275/55R20
    size: str
    _diameter: int

    def __init__(self, size):
        """
        size: 
            string: assumes metric XXX/YYRZZ format
            float: assumes industrial inches
        """
        self.metric_expression = r"""\d{3}\/\d{2,}R\d{2}"""
        if isinstance(size, str):
            # Find the metric string (275/55R20)
            result = re.findall(self.metric_expression, size)
            if not result:
                raise ValueError(f'"{size}" parameter is not a valid tire metric size')
            self._metric_string = result[0]
            # Get the tire width, aspect ratio, and wheel diameter
            numbers = re.findall(r"""\d+""", self._metric_string)
            # Need to convert from string to integer
            width, aspect_ratio, wheel_diameter = [int(x) for x in numbers]
            # tire sidewall height x 2 in mm
            height_mm = (width*(aspect_ratio/100.0))*2
            # Convert to inches and add the wheel (rim) diameter
            self._diameter = cm_to_in(height_mm/10)+wheel_diameter
            # Round to 4 digits, if we needed more we are doing some crazy stuff...
            self._diameter = round(self.diameter, 4)
            self.size = size
        elif isinstance(size, (int, float)):
            self._diameter = size
            self.size = ''
        else:
            raise TypeError(f"size parameter type {type(self.size)} is not an expected type!")

    @property
    def diameter(self):
        """Returns the tire diameter in inches"""
        return self._diameter

    def __str__(self):
        msg = f'{self.diameter}"'
        if self.size:
            msg += f' ({self.size})'
        return msg
    
    def create_tire(self):
        return Tire(self)


class Tire(VehicleChild):
    def __init__(self, tire_info: TireInfo):
        self._info = tire_info

    @property
    def diameter(self):
        return self._info._diameter

    @property
    def circumference(self):
        """Returns the tire circumference in inches"""
        return self.diameter * 3.14
    
    def miles_per_rev(self):
        inches_per_rev = self.circumference
        return inches_per_rev / (5280*12)
    
    def revs_per_mile(self):
        return 1/self.miles_per_rev()

