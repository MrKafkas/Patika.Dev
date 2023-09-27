class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer == answer

# print(q1.checkAnswer('Python'))
# print(q2.checkAnswer('C#'))
# print(q3.checkAnswer('Java'))

class Quiz:
    def __init__(self,Questinos):
        self.Questions=Questinos
        self.score=0
        self.questionsIndex=0
    def getQuestion(self):
        return self.questions[self.questionIndex]
    def displayQuestion (self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex+1}: {Question.text}')
q1=Question('En iyi programlama dili hangisidir?',['C#','Python','Javascript','Java'], 'Python')
q2=Question('En popüler programlama dili hangisidir?',['C#','Python','Javascript','Java'], 'C#')
q3=Question('En çok kazandıran programlama dili hangisidir?', ['C#','Python','Javascript','Java'], 'Java')
Questions=[q1,q2,q3]
quiz=Quiz(Questions)
question=quiz.Questions[quiz.questionsIndex]
print(question.text)

Quiz.displayQuestion()