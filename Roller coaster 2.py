print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
  bill = 0
  print("Thank you for your response...")
  age = int(input("What is your age?. "))
  if age < 12:
    bill = 5
    print("Child Tickets are $5.")
  elif age <=18:
    bill = 7
    print("Youth Tickets are $7")
  else:
    bill = 12
    print("Adult Tickets are $12.")
  want_a_photo = input("Do you want a photo taken? Y or N. ")
  if want_a_photo == "Y":
    bill +=3
    print(f"Your bill is {bill}")
else:
  print("check back some other time")