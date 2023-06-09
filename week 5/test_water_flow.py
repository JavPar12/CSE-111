from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe,pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction,kpa_to_psi
from pytest import approx
import pytest

def test_water_column_height():
    assert water_column_height(0, 0) == 0
    assert water_column_height(0, 10) == 7.5
    assert water_column_height(25, 0) == 25
    assert water_column_height(48.3, 12.8) == 57.9

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0) == approx(0, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692,0,0.018,1.75) == approx(0,abs=0.001)
    assert pressure_loss_from_pipe(0.048692,200,0,1.75) == approx(0,abs=0.001)
    assert pressure_loss_from_pipe(0.048692,200,0.018,0) == approx(0,abs=0.001)
    assert pressure_loss_from_pipe(0.048692,200,0.018,1.75) == approx(-113.008,abs=0.001)
    assert pressure_loss_from_pipe(0.048692,200,0.018,1.65) == approx(-100.462,abs=0.001)
    assert pressure_loss_from_pipe(0.28687,1000,0.013,1.65) == approx(-61.576,abs=0.001)
    assert pressure_loss_from_pipe(0.28687,1800.75,0.013,1.65) == approx(-110.884,abs=0.001)



def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0, 3) == approx(0, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)

def test_reynolds_number():
    assert reynolds_number(0.048692, 0) == approx(0, abs=1)
    assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    assert reynolds_number(0.28687, 1.65) == approx(471729, abs=1)
    assert reynolds_number(0.28687, 1.75) == approx(500318, abs=1)

def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-163.750, abs=0.001)

def test_kpa_to_psi():
    assert kpa_to_psi(0) == 0
    assert kpa_to_psi(100) == 14.5038
    assert kpa_to_psi(200) == 29.0076
    assert kpa_to_psi(500) == 72.5195
    assert kpa_to_psi(1000) == 145.038







PVC_SCHED80_INNER_DIAMETER = 0.28687  # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013   # (unitless)
SUPPLY_VELOCITY = 1.65                # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692  # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018    # (unitless)
HOUSEHOLD_VELOCITY = 1.75             # (meters / second)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    pressure_psi = kpa_to_psi(pressure)

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {pressure_psi:.2f} psi")

if __name__ == "__main__":
    main()
