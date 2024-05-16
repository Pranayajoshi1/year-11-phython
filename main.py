import random
GOOD_COMMENTS = ["Way to go!", "Keep it up!" , "Fantastic"]
BAD_COMMENTS = ["keep trying", "Maybe next time", "Don't give up"]
QUESTION_FORMAT = "{}\nA. {} B. {} C. {} D. {}"
QUESTIONS = ["What is the capital of New Zealand?",
            "In which part of your body would you find the cruciate ligament?",
            "What is the name of the main antagonist in the Shakespeare play Othello??"
            ]
OPTIONS = [[ "Wellington" "New York" "Nepal" "Kathmandu"]
          [ "Knee" "Hand" "Nail"  "Hair"]
          [ "Shawn" "UGO" "Steve" "Iago"]]
SHORT_OPTIONS = [ "a", "b", "c", "d"]
ANSWERS = [1,2,4]
# Intro/
name = input("What's your name?")
print("Hello! Welcome to the quiz" ,name)
while True:
    try:
        tries = input("How many attempts do you want at each question? 1-3")
        tries = int(tries)
        break
    except:
        print("That's not a number unfortunately. Maybe type 1, 2 or 3.")

#Question 1
play = "yes"
while play == "yes":    
    score = 0
    question = "What is the capital of New Zealand?"
    a = "Wellington"
    b = "New York"
    c = "Nepal"
    d = "Kathmandu"
    answer  = input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()
    score += 5
    print(random.choice(GOOD_COMMENTS))
    if answer.lower() == a or answer.lower() == "a":
        print("Correct! The answer Wellington")
        
        
    elif answer == "":
        print("Are you here?")
    elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
        print("That wasn't an option")
    else: 
        print("Sorry! That's incorrect. :(")
        print(random.choice(BAD_COMMENTS))
        print("The correct answer is Wellington! Better of luck, next time.")
    #Question 2
    answer =input("In which part of your body would you find the cruciate ligament?").upper()
    if answer == "Knee".upper():
        print("Correct! The answer is Knee. Good job!")
        score += 5
        print(random.choice(GOOD_COMMENTS))
    elif answer == "":
        print("Are you here?")
    else: 
        print("Sorry! That's incorrect. :(")
        print(random.choice(BAD_COMMENTS))
        print("The correct answer is Knee! Better luck next time.")
    #Question 3
    answer =input("What is the name of the main antagonist in the Shakespeare play Othello??").upper()
    if answer == "Iago".upper():
        print("Correct! It is indeed Iago!")
    
        score +=5
        print(random.choice(GOOD_COMMENTS))
    elif answer == "":
        print("Did something short-circuit?")
    else:
        print("Sorry! That's incorrect. :(")
        print(random.choice(BAD_COMMENTS))
        print("The correct answer is Iago! Better luck next time.")
    # Ending
    print("Good job {}! Thank you so much for answering my quiz! Your final score {} out of 15".format(name, score)) 
    play = input("Do you want to play again?").lower()

print("Oh okay! Goodbye then! ^_^")
print(" Game end. Thank you for playing")

