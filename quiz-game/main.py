from question_model import new_question
from data import question_data
from quiz_brain import quiz_brain

question_bank = []
for Question in question_data:
    temp = new_question(Question["question"], Question["answer"])
    question_bank.append(temp)
print(question_bank)

quiz = quiz_brain(question_bank)
quiz.next_question()
while quiz.still_have_questions():
    quiz.next_question()
print(f"your total score was {quiz.score}/{quiz.question_no}")
