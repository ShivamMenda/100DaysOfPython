class QuizBrain:
    def __init__(self,question_list) :
        self.question_number=0
        self.question_list=question_list
        self.score=0
    def still_has_questions(self):
       return self.question_number<len(self.question_list)
    def next_question(self):
        curques=self.question_list[self.question_number]
        self.question_number+=1
        user_ans=input(f"Q.{self.question_number}:{curques.text} (True/False)? ")
        self.check_answer(user_ans,curques.answer)
    def check_answer(self,user_ans,correct_ans):
        if(user_ans.lower()==correct_ans.lower()):
            self.score+=1
            print("You got it right")
        else:
            print("That's wrong")
        print(f"The correct answer is {correct_ans}")
        print(f"The current score is {self.score}/{self.question_number}")
        print("\n")



    
           
     