class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question, options, correct_option):
        self.questions.append({
            "question": question,
            "options": options,
            "correct_option": correct_option
        })

    def run_quiz(self):
        score = 0
        for i, question_data in enumerate(self.questions, start=1):
            print(f"Question {i}: {question_data['question']}")
            for j, option in enumerate(question_data['options'], start=1):
                print(f"{j}. {option}")
            user_answer = int(input("Your answer: "))
            if user_answer == question_data['correct_option']:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
            print()

        print(f"Quiz completed. Your score: {score}/{len(self.questions)}")


def main():
    quiz = Quiz()

    # Add questions
    quiz.add_question("What is the capital of France?", ["London", "Paris", "Berlin"], 2)
    quiz.add_question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus"], 2)
    quiz.add_question("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Jane Austen"], 2)

    print("Welcome to the Quiz!")
    user_choice = input("Enter 'S' to start the quiz: ").upper()

    if user_choice == 'S':
        quiz.run_quiz()
    else:
        print("Invalid choice. Exiting the quiz.")


if __name__ == "__main__":
    main()
