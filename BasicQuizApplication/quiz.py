def quiz():
    questions = {
        "What is the capital of France?": "Paris",
        "What is 5 + 7?": "12",
        "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    }

    score = 0
    for question, answer in questions.items():
        user_answer = input(question + " ").strip()
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")

    print(f"\nYour final score is {score}/{len(questions)}")

quiz()
