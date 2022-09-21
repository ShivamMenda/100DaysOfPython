from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[] #Get questions and answers from the data and converting into objects
for i in question_data:
    question_text=i["text"]
    question_ans=i["answer"]
    question_bank.append(Question(question_text,question_ans))

quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed quiz")
print(f"The final score is {quiz.score}/{quiz.question_number}")
