# Rent Calculator :-

rent = int(input(" Enter your flat rent :- "))
electricity_current_unit_reading = int(input(" Enter the current meter reading :- "))
electricity_previous_unit_reading = int(input(" Enter the previous meter reading :- "))
charge_per_unit = int(input(" Enter charge per unit :- "))
water_charge = int(input(" Enter the charges of water :- "))

calculated_electricity_unit = (electricity_current_unit_reading - electricity_previous_unit_reading)
print("Electricity unit spend :",calculated_electricity_unit)

total_electricity_bill = (calculated_electricity_unit * charge_per_unit)
print("Electricity bill :",total_electricity_bill)

water_charge_bill = water_charge
print("Water charges :",water_charge_bill)

total_rent = (rent + total_electricity_bill + water_charge_bill)
print("The renter want to pay the rent :",total_rent)

print("Thank you ...")