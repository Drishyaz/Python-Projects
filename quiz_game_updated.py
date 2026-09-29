quiz_data = [
    {
        "question": "Which planet is known as the Red Planet?",
        "correct_answer": "Mars",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"]
    },
    {
        "question": "What is the chemical symbol for water?",
        "correct_answer": "H2O",
        "options": ["CO2", "H2O", "O2", "NaCl"]
    },
    {
        "question": "Who painted the Mona Lisa?",
        "correct_answer": "Leonardo da Vinci",
        "options": ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Claude Monet"]
    },
    {
        "question": "What is the smallest prime number?",
        "correct_answer": "2",
        "options": ["0", "1", "2", "3"]
    }
]

def game_start():
    score = 0
    print("GAME STARTS NOW!")
    for item in quiz_data:
        print("\n"+item["question"])
        print("\nThe options are:")
        for x in item["options"]:
            print(x)
            
        user_choice = int(input("\nWhat is your answer? Choose option (1/2/3/4): "))
        if item["options"][user_choice - 1] == item["correct_answer"]:
            print("Correct! You score +1 points")
            score += 1
        else:
            print("Wrong answer.. You scored 0 points")

    print("\nFinal score:",score)

while True:
    input('''What do you want to do?
1. Update questions
2. Play Quiz''')
    game_start()

    if(input("Do you wanna try again? (y/n)").lower()=="y"):
        game_start()
    else:
        break
