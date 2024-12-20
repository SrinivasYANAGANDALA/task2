import random
user=input("enter your choice :")
chances=["rock","paper","sisser"]
system=random.choice(chances)
print(f"\n your selected {user} and system chooses {system}")
if user==system:
  print(f"both are selected the same{user}")
elif user=="rock":
      if system=="paper":
          print("you loos! paper covers rock. ")
      else:
          print("you whine! rockbreaks sisser ")
elif user=="paper":
      if system=="sisser":
          print("you loos! sisser cuts paper. ")
      else:
          print("you whine! paper covers rock.")
elif user=="sisser":
      if system=="rock":
          print("you loos! rock break sisser. ")
else:
      print("you whine! sisser cuts paper.")
