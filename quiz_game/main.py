def new_game():
    #start the game
    guesses = []
    correct_guesses = 0
    question_num = 0
# -------------------------------
    #write the questions
    for key in questions:
        print("------------------")
        print(key)
        for i in options[question_num]:
            print(i)
        #get the user input
        guess = input("enter (A,B,C): ")
        guess = guess.upper()
        guesses.append(guess)
# -------------------------------
        #debug the correct or wrong print msg and add correct_guesses
        correct_guesses+=check_answers(questions.get(key), guess)
        question_num+=1
# -------------------------------
    display_score(question_num,correct_guesses,question_num-correct_guesses)
    play_again()
# -------------------------------
def check_answers(answer, guess):
    if(answer == guess):
        print("u r correct")
        return 1
    else:
        print("u r wrong")
        return 0
#-------------------------------
def display_score(totalQuestions, correctAns, wrongAns):
    print("SCORE")
    print("----------------------")
    print("you have answered: " + str(totalQuestions))
    print("----------------------")
    print("you got: " + str(correctAns) + " right")
    print("----------------------")
    print("you have answered "+ str(wrongAns) + " wrong")
#-------------------------------
def play_again():
    choices = ["Y","N"]
    restart = None
    while restart not in choices:
        restart = input("Do you want to play again?? (Y/N)").upper()
    if(restart == "Y"):
        new_game()
    else:
        exit()
#-------------------------------
questions = {
    "Who am i?":"A",
    "how old am i?":"A",
    "whats my height?":"B",
}
#-------------------------------
options = [
    ["A. Lucas","B. teste2", "C. Teste3"],
    ["A. 16", "B. 18", "C. 32"],
    ["A. 1.18m", "B. 1.76", "C. 2m"]
]
#-------------------------------
new_game()