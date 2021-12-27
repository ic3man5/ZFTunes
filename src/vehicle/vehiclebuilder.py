from config.manager import ConfigManager
from vehicle.vehicle import VehicleInfo
from vehicle.engine import EngineInfo
from vehicle.trans import TransmissionInfo
from vehicle.tire import TireInfo
from vehicle.drivetrain import DrivetrainInfo


def create_from_config(config_name):
    manager = ConfigManager()
    config = manager.load(config_name)
    # Create the vehicle
    info = config['info']
    engine_size = info['engine']
    engine_size = float(engine_size.strip('L'))
    vehicle_info = VehicleInfo(info['year'], info['manufacturer'], info['model'], engine_size)
    vehicle = vehicle_info.create_vehicle()
    # Create the engine
    engine_config = config['engine']
    engine_info = EngineInfo(engine_config['idle_rpm'], engine_config['max_rpm'], engine_config['peak_hp_rpm'], engine_config['peak_torque_rpm'])
    vehicle.engine = engine_info.create_engine()
    # Create the transmission
    trans_config = config['transmission']
    gears = trans_config['gears']
    try:
        reverse_ratio = trans_config['reverse_ratio']
    except KeyError as _:
        reverse_ratio = -1.0
    trans_info = TransmissionInfo(trans_config['name'], len(gears), gears.values(), reverse_ratio, trans_config['stall_rpm'])
    vehicle.transmission = trans_info.create_transmission()
    # Create the Tire
    dt_config = config['drivetrain']
    tire_info = TireInfo(dt_config['tire_diameter'])
    vehicle.tire = tire_info.create_tire()
    # Create the Drivetrain
    dt_info = DrivetrainInfo(dt_config['axle_ratio'], dt_config['transfer_case_ratio'], vehicle.tire)
    vehicle.drivetrain = dt_info.create_drivetrain()

    return vehicle