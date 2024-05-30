guesses = []
BIGGEST_COUNTRY_ANSWER = ["russia", "india", "china", "us", "brazil", "australia", "canada" "new york", "Travis"]

#------------------FUNCTIONS---------------

# welcomes user
def intro():
    name = input("What's your name?")
    print("Hello! Welcome to the quiz" ,name)
    print("This quiz is all about the ten larget countries in the world. You need answer as much you know.")

# asks for password
def getpassword():
  while True:
    password = input("What's the password?")
    if password == "Meww":
      return
    else:
      print("That's wrong answer")

def getlives():
    while True:
        live = input("How many chance you need?")
        try:
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("Please choose a positive number")
        except:
            print("That wasn't a number")

def inlist(answer, list):
    if answer in list:
        return True
    else:
     return False           


# -------- MAIN CODE -----------
intro()
lives = getlives()
score = 0
# Begin quiz
while lives > 0:
 

