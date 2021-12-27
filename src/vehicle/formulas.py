import re

def in_to_cm(inches):
    """Convert inches to centimeters"""
    return inches*2.54

def cm_to_in(cm):
    """Convert centimeters to inches"""
    return cm/2.54

def to_ordinal_number(n) -> str:
    """Takes an integer and outputs an ordinal number string"""
    return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(4 if 10 <= n % 100 < 20 else n % 10, "th")

class Tire(object):
    _diameter = 0

    def __init__(self, tire_size):
        """
        size: 
            string: assumes metric XXX/YYRZZ format
            float: assumes industrial inches
        """
        self.metric_expression = r"""\d{3}\/\d{2,}R\d{2}"""
        if isinstance(tire_size, str):
            # Find the metric string (275/55R20)
            result = re.findall(self.metric_expression, tire_size)
            if not result:
                raise ValueError(f'"{tire_size}" parameter is not a valid tire metric size')
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
        elif isinstance(tire_size, (int, float)):
            self._diameter = tire_size
        else:
            raise TypeError(f"tire_size parameter type {type(tire_size)} is not an expected type!")

    @property
    def diameter(self):
        """Returns the tire diameter in inches"""
        return self._diameter

    @property
    def circumference(self):
        """Returns the tire circumference in inches"""
        return self.diameter * 3.14
    
    def miles_per_rev(self):
        inches_per_rev = self.circumference
        return inches_per_rev / (5280*12)
    
    def revs_per_mile(self):
        return 1/self.miles_per_rev()


def calc_oss_from_mph(mph, tire, axle_ratio):
    """Calculates the OSS (Output Shaft Speed - transmission) in RPM"""
    # revs_per_mile * MPH = revs_per_hour
    #   632.3636 * 3 = 1897.0908 revs_per_hour
    # revs_per_hour / 60 = revs_per_minute
    #   1897.0908 / 60 = 31.61818 RPM
    # RPM x Axle Ratio = RPM
    #   31.61818 x 3.21 = 101.4943578
    revs_per_hour = tire.revs_per_mile() * mph
    tire_rpm = revs_per_hour / 60
    oss = tire_rpm * axle_ratio
    return oss

def calc_mph_from_oss(oss, tire, axle_ratio) -> float:
    """Calculates MPH from (Output Shaft Speed - transmission). Rounded to 1 digit"""
    # oss = tire_rpm * axle_ratio
    # oss / axle_ratio = tire_rpm
    # tire_rpm / revs_per_mile * 60 = mph
    # ((oss / axle_ratio) / revs_per_mile * 60)
    mph = round(oss / axle_ratio / tire.revs_per_mile() * 60, 1)
    return mph

def calc_engine_rpm_from_oss(oss, trans_gear_ratio):
    """Calculates engine RPM from transmission OSS"""
    return oss * trans_gear_ratio

if __name__ == "__main__":
    tire = Tire("LT275/55R20")
    axle_ratio = 3.21
    gear_ratios = [5, 3.2, 2.1429, 1.72, 1.3139, 1, 0.8221, 0.64]

    print(f'Tire diameter: {tire.diameter}"')
    print(f'Tire Revs per mile: {tire.revs_per_mile()}')
    print(f'Tire Miles per rev: {tire.miles_per_rev()}')

    for mph in range(1, 100):
        oss = calc_oss_from_mph(mph, tire, 3.21)
        new_mph = calc_mph_from_oss(oss, tire, 3.21)
        print(f"{mph}/{new_mph} MPH: {round(oss, 1)}RPM", end="\t")
        for gear, ratio in enumerate(gear_ratios):
            rpm = calc_engine_rpm_from_oss(oss, ratio)
            print(f"{gear+1}: {round(rpm, 0)} RPM", end="   ")
        print()
