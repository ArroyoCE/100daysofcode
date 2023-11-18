class Brain:

    def __init__(self, questions):
        import os
        question_number = 0
        right = 0

        self.question_list = questions
        while question_number < 10:
            os.system('cls')
            decision = input(f"Q.{question_number + 1}: {self.question_list[question_number].text} (True/False): ")
            if decision == self.question_list[question_number].answer:
                right += 1
                print("You got it right!")
                if question_number < 9:
                    print(f"Your current score is: {right}/{question_number+1}")
                    input("\nPress any key for the next question.")
            else:
                print("That's wrong!")
                if question_number < 9:
                    print(f"Your current score is: {right}/{question_number + 1}")
                    input("\nPress any key for the next question.")

            question_number += 1

        print(f"You've completed the quizz!\nYour final score is: {right}/{question_number}")
        input("\nPress any key to finish.")
