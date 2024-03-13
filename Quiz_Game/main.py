
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for text in question_data:
    question_text=text["text"]
    question_answer = text["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("you have completed the quiz!!")
print(f"your total score was:{quiz.score}/{quiz.question_number}")

#Explanation
""" we are converting the given data into 
     question_bank=[
       Question(q1,a1),
       Question(Q2,a2),
       Question(Q3,a3),...... 
     ]
     To get hold of q1 we are using- question_bank.text
       To get hold of a1 we are using- question_bank.answer
     """