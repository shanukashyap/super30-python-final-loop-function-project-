"""Simple Python Quiz Application."""


questions = [
    {
        "question": "What keyword is used to define a function in Python?",
        "answer": "def"
    },
    {
        "question": "Which loop is commonly used when the number of iterations is known?",
        "answer": "for"
    },
    {
        "question": "Which keyword is used to return a value from a function?",
        "answer": "return"
    },
    {
        "question": "Which data type stores key-value pairs?",
        "answer": "dictionary"
    },
    {
        "question": "Which loop continues while a condition is true?",
        "answer": "while"
    }
]


def run_quiz():
    """Display questions and calculate the user's score."""
    score = 0

    for question in questions:
        print("\n" + question["question"])
        answer = input("Your answer: ")

        if answer.lower() == question["answer"]:
            print("Correct!")
            score = score + 1
        else:
            print("Incorrect.")

    percentage = (score / len(questions)) * 100

    print("\n--- QUIZ RESULT ---")
    print("Score:", score, "/", len(questions))
    print("Percentage:", percentage)


run_quiz()