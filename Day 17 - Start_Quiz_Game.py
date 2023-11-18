# class User:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     def rename_user(self, name):
#         self.name = name


# user_1 = User('Rafael', 0o01)
# user_1.rename_user('José')
# print(user_1.id, user_1.name)

from lib.data import question_data
from lib.question_model import Question
from random import shuffle
from lib.quiz_brain import Brain

question_bank = []
shuffle(question_data)


for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

brain = Brain(question_bank)
