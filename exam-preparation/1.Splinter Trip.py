travel = float(input())
fuel_tank = float(input())
heavy_wind = float(input())
non_heavy = travel-heavy_wind
non_heavy_consum = non_heavy*25
heavy_consum=heavy_wind*25*3/2
fuel_consum=non_heavy_consum+heavy_consum
Tolerance =fuel_consum*5/100
total_fuel_consum = fuel_consum+Tolerance
remaining_fuel = fuel_tank - total_fuel_consum
print('Fuel needed: {0:.2f}L'.format(total_fuel_consum))
if (remaining_fuel>=0.0):
    print('Enough with {0:.2f}L to spare!'.format(remaining_fuel))
else:
    print('We need {0:.2f}L more fuel.'.format(-remaining_fuel))