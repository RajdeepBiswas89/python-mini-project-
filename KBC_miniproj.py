'''create a program capable of displaying questions to the user like kbc
use list data type to store the questions and their correct answers
display the final amount the person is taking home after playing the game
'''
questions=[
     ["national anthem of india","jana ganna manna","vande mataram","amar sonar bangla","we shall overcome",1],
     ["national anthem of india","jana ganna manna","vande mataram","amar sonar bangla","we shall overcome",1],
     ["national anthem of india","jana ganna manna","vande mataram","amar sonar bangla","we shall overcome",1],
     ["national anthem of india","jana ganna manna","vande mataram","amar sonar bangla","we shall overcome",1],
     ["national anthem of india","jana ganna manna","vande mataram","amar sonar bangla","we shall overcome",1],

]
levels=[10000,20000,30000,40000,50000,100000,200000]
money=0 
for i in range(0 , len(questions)):
    question=questions[i]
    print(f"questions for rupees {levels[i]}")
    print(f"{question[0]}")
    print(f"a) {question[1]}        b) {question[2]}")
    print(f"c) {question[3]}        d) {question[4]}")
    reply=int(input("enter your choices between 1 to 4 or 0 to quit from the game"))
    if(reply==0):
        money= levels[i-1]
        break
    if(reply==question[5]):
        print(f"congrats your answer is correct ,you won rupees {levels[0]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=20000
        elif(i==14):
            money=10000000
    else:
        print("wrong answers")
        break

        

