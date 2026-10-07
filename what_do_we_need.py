##what do we need
#total rent 
#total food yall ordered 
#electricity bill
#charge per unit 
#PERSON LIVING IN ROOM OR FLAT
##output
#total rent + total food + electricity bill + (charge per unit * units consumed)
rent=int(input("enter your hostel/flat rent="))
food=int(input("enter your total food bill="))
electricity_bill=int(input('enter the electricity bill='))
charge_per_unit=int(input('enter the charge per unit='))
persons=int(input("enter the number of persons living in the room or flat="))

total_bill=electricity_bill*charge_per_unit
output=(rent+food+total_bill) // persons
print("Total bill per person:", output/persons)
print("each person has to pay =", output)