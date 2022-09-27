chequebook_onebank = input("Home delivery? Y or N? ")
if chequebook_onebank == "Y":
    print("Enter Address")
    logistics =input("Cost of logistics is borne by customer. Agree or Disagree? ")
    if logistics == "Agree":
        print("Send to Address from CPC")
        print("Activate after customer acknowledges")
    else:
        print("Kindly opt for branch pick up")

else:
  print("Send to Branch from CPC")
  print("CEM sends for activation")
  print("Customer is notified to pick up")
  print("Customer picks up and dazzall")


