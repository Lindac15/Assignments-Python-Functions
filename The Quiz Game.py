# Task 1: Develop a list of questions and answers.
# Task 2: Write a function that quizzes the user and takes their answers.
# Task 3: Score the quiz and give the user feedback on their performance.

def ask_question(question, correct_answer):
    user_answer = input(f"{question} ").lower()
    return user_answer == correct_answer.lower()

def quiz_game ():

    questions = {  # Task 1
        "Which planet is known as the 'Red Planet'?": "Mars",
        "Which famous scientist developed the theory of relativity?": "Albert Einstein",
        "What is the powerhouse of the cell?": "Mitochondria",
        "Who was the first person to set foot on the moon?": "Neil Armstrong",
        "What is the largest planet in our solar system?": "Jupiter",
        "What is the name of a negative subatomic particle?": "Electron",
        "Which element doesn't have nuetron in it's nucleus?": "Hydrogen",
        "Which element has 10 protons?": "Neon",
        "What delivers messages from nerves to other nerves or muscles?": "Neurotransmitters",
        "What secrets only 'release' or 'inhibitory' factors controlling the pituitary?": "Hypothalamus",
        "What is the largest organ in the human body?": "Skin",
        "What is the hardest natural substance on Earth?": "Diamond"
    }       
    score = 0
    total_questions = len(questions)

    print("Welcome to the Quiz Game!")
    print("NOTE: If your spelling is incorrect, it is considered a wrong answer.")

    for question, answer in questions.items():
        if ask_question(question, answer):
            score += 1  
            print("Correct!")
        else:
            print("Incorrect!")
    print(f"Your score is {score}/{total_questions}.")
    if score == total_questions:
        print("Congratulations! You got a perfect score!")
    elif score >= total_questions / 2:
        print("Good job! You passed the quiz.")
    else:
        print("You failed the quiz. Better luck next time.")    
    
quiz_game()