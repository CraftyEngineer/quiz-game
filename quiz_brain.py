
class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def nextQuestion(self):
        current_question=self.q_list[self.q_number]
        self.q_number+=1
        user_answer=input(f"Q {self.q_number}: {current_question.text} (True/False): ")
        self.checkAnswer(user_answer,  current_question.answer)

    def still_has_questions(self):
        return self.q_number<len(self.q_list)
    
    def  checkAnswer(self, user_answer, actual_answer):
        if user_answer.lower()==actual_answer.lower():
            print("Correct!")
            self.score+=1
            
        else:
            print(f"Sorry, that's incorrect!")

        print(f"The answer was {actual_answer}")
        print(f"Your score is {self.score}/{self.q_number}")
        print("\n")

          
    

        
