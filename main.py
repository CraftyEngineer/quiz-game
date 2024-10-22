from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

for i in question_data:
    question=Question(i['question'],i['correct_answer'])
    question_bank.append(question)


quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.nextQuestion()
print("You have successfuly completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.q_number}")