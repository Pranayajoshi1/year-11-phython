import random
GOOD_COMMENTS = ["Way to go!", "Keep it up!" , "Fantastic"]
BAD_COMMENTS = ["keep trying", "Maybe next time", "Don't give up"]
QUESTION_FORMAT = "{}\nA. {} B. {} C. {} D. {}"
QUESTIONS = ["What is the capital of New Zealand?",
            "In which part of your body would you find the cruciate ligament?",
            "What is the name of the main antagonist in the Shakespeare play Othello??"
            ]
OPTIONS =  [[ "Wellington", "New York", "Nepal", "Kathmandu"],
            [ "Knee", "Hand", "Nail", "Hair"],
            [ "Shawn", "UGO", "Steve", "Iago"]]

SHORT_OPTIONS = [ "a", "b", "c", "d"]
ANSWERS = [0,2,4]
play = "yes"
# ---------INTRO------------
name = input("What's your name?")
print("Hello! Welcome to the quiz" ,name)
while True:
    try:
        tries = input("How many attempts do you want at each question? 1-3")
        tries = int(tries)
        break
    except:
        print("That's not a number unfortunately. Maybe type 1, 2 or 3.")

#--------START THE QUIZ----------
    while play == "yes":
        score = 0
#-------LOOP THROUGH EACH QUESTION/ANSWER--------
for i in range(len(QUESTIONS)):
    question_attempts = tries
    while question_attempts > 0:
#-------CHECK THE USER'S ANSWER--------------|
        if answer == OPTIONS[i][ANSWERS[i]] or answer == SHORT_OPTIONS[ANSWERS[i]]:
            print("Correct")
            score += 5
            break
            print(random.choice(GOOD_COMMENTS))
        elif answer == "":
            print("Are you here?")
        elif answer in SHORT_OPTIONS or answer in OPTIONS[i]:
            print("Wrong!")
        else:
            print(random.choice(BAD_COMMENTS))
    else:
        print("That wasn't an option")
        question_attempts -= 1
        print("The answer is Wellington")
#----------ENDING---------
    print("Well done {}. You finished the quiz. Your final score is {}".format(name, score))
#----------REPLAY---------
    play = input("Do you want to play again?").lower()

print("Oh okay! Goodbye then! ^_^")
print(" Game end. Thank you for playing")   

