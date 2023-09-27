class Questions:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer==answer

class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0
    
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question=self.getQuestion()
        print(f'Soru{self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-'+q)
        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()
    
    def guess(self,answer):
        question=self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

        
    
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore (self):
        totalQuestion = len (self.questions)
        if questionNumber>totalQuestion:
            print('Quiz bitti.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}')
    
    def displayProgress(self)
q1=Questions('en iyi programlama dili hangisidir?',['C#','Python','java','javascript'],'Python')
q2=Questions('en çok kazandıran programlama dili hangisidir?',['C#','Python','java','javascript'],'Python')
q3=Questions('en kullanışlı programlama dili hangisidir?',['C#','Python','java','javascript'],'Python')
questions=[q1,q2,q3]

quiz=Quiz(questions)
quiz.displayQuestion()