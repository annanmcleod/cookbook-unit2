from dataclasses import dataclass 
@dataclass
class User:
  user: str
  password: str
nomnom=[]
cookie=[]
def honey():
    print("Welcome to the BCCA Official Cookbook!")
    print("Please enter your Username and Password.\n")
    user = input("Username: ")
    try:
      with open (f"folders/{user}.txt","r") as nom :
        l = nom.read().splitlines()
        if user in l :
            password = input("Password: ")
            if password in l: 
              pass
            else:
              print("Invaild password")
              print("")
              honey()
        else:
            print("Invaild username")
            print("")
            honey()
    except :
      print("")
      print("wrong username \ntry again")
      print(" ")
      honey()
       
def pasta():
  username=input("what do you want your username as? ")
  file_name = f"folders/{username}.txt"
  with open(file_name, "w") as peach :
    passwrods=input("what would you want you password as? ")
    peach.write(username+"\n"+passwrods)
def pineapple():
  file = input("Recipe List> ")
  try:
    with open(f"recipes_list/{file}.txt") as pear:
      name = input("Name> ")
    with open(f"recipes_list/{file}.txt", "a") as pear:
      pear.write("\n" + name)
    with open(f"recipes_storage/{name}.txt", "w") as pear:
      print("Ingredients> ")
      items = input("> ")
      pear.write("\n" + items)
      print("Directions> ")
      instructions = input("> ")
      pear.write("\n" + instructions)
    cake = input("Cook Time> ")
    with open(f"recipes_storage/{name}.txt", "w") as strawberry:
      strawberry.write(f"<{name}>" + "\n" + "\n"+ "Ingredients>"  + "\n" + items + "\n" + "\n" +"Directions>" +"\n" + instructions + "\n" + "\n" + "Cook Time> " + cake)
    strawberry.close()
  except:
    name = input("Name> ")
    with open(f"recipes_list/{file}.txt", "w") as pear:
      pear.write(name)
    with open(f"recipes_list/{file}.txt", "w") as pear:   
      pear.write(file)
    with open(f"recipes_storage/{name}.txt", "a") as pear:
      print("Ingredients> ")
      items = input("> ")
      with open(f"recipes_storage/{name}.txt", "a") as pear:
        pear.write(items)
      print("Directions> ")
      instructions = input("> ")
      with open(f"recipes_storage/{name}.txt", "a") as pear:
        pear.write("\n" + instructions)
    cake = input("Cook Time> ")
    with open(f"recipes_storage/{name}.txt", "w") as strawberry:
      strawberry.write(f"<{name}>" + "\n" + "\n"+ "Ingredients>"  + "\n" + f">{items}" + "\n" + "\n" +"Directions>" +"\n" + f">{instructions}" + "\n" + "\n" + "Cook Time> " + cake)
    strawberry.close()

def popcorn():
  cooking=input("What kind of recipe do you want you look at ? ")
  try:
    with open (f"recipes_storage/{cooking}.txt", "r") as file:
      print(f"{file.readlines()}")
  except:
     with open (f"recipes_list/{cooking}.txt", "r") as files:
      print(f"{files.readlines()}")
def lasagna():
  print("You have the options of desserts, pastas, crockpot recipes, hot plate recipes, and dips .")
def main():
  monster=input ("Do you have an account? ")
  if monster=="no" or monster == "No":
    pasta()
    print("")
    honey()
  elif monster=="yes" or monster == "Yes":
    honey()
  while True:
      print("Are you [adding], [viewing] all recipes , [searching] for a specific recipe , [logout]. ")
      strawberry = input("> ")
      if strawberry == "adding":
        pineapple()
      if strawberry == "viewing":
        lasagna()
      if strawberry == "searching":
        popcorn()
      if strawberry == "logout":
        break
if __name__ == "__main__":
  main()

