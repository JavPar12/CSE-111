EARTH_ACCELERATION_OF_GRAVITY = 9.80665
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016

def water_column_height(tower_height, tank_height):
    water_column_height = tower_height + (3 * tank_height) / 4
    return water_column_height

def pressure_gain_from_water_height(height):
    pressure = (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    pressure_loss = (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    lost_pressure = (0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings) / 2000
    return lost_pressure

def reynolds_number(hydraulic_diameter, fluid_velocity):
    reynolds = (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY
    return reynolds

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    pressure_loss = -k * WATER_DENSITY * fluid_velocity**2 / 2000
    return pressure_loss

def kpa_to_psi(pressure_kpa):
    psi = pressure_kpa * 0.145038
    return psi
