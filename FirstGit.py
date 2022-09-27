import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
nametopay = len(names)
random_1 = random.randint(0, nametopay - 1)
persontopay = names[random_1]
print(persontopay + " will buy the meal today!")


