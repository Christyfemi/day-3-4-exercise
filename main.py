# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill=0
bill2=0
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size=="S":
  bill=15
  bill2=17
  print("You will have to pay $15")
elif size=="M":
  bill=20
  bill2=23
  print("You will have to pay $20")
else:
  bill=25
  bill2=28
  print("You will have to pay $25") 
if add_pepperoni=="Y":
 if size=="S":
  bill+=2
  print(f"The bill is now ${bill}")
 else: 
  bill+=3
  print(f"The bill is now ${bill}")  
if extra_cheese=="Y":
  bill2+=1 
  print(f"The final bill2 is ${bill2}")





