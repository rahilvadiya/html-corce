questions = [
       
    [
        "Which Languge Was used to creat fb?","Python",
        "French","JavaScript","Php","None",4
        ],
    [
        "Which Languge Was used to creat fb?","Python",
        "French","JavaScript","Php","None",4
        ],
    [
        "Which Languge Was used to creat fb?","Python",
        "French","JavaScript","Php","None",4
        ],
    [
        "Which Languge Was used to creat fb?","Python",
        "French","JavaScript","Php","None",4
        ],
    [
        "Which Languge Was used to creat fb?","Python",
        "French","JavaScript","Php","None",4
        ],
    [
        "Which Languge Was used to creat fb?","Python",
        "French","JavaScript","Php","None",4
        ],
    [
        "Which Languge Was used to creat fb?","Python",
        "French","JavaScript","Php","None",4
        ],
    [
        "Which Languge Was used to creat fb?","Python",
        "French","JavaScript","Php","None",4
        ],
    [
        "Which Languge Was used to creat fb?","Python",
        "French","JavaScript","Php","None",4
        ],
    [
        "Which Languge Was used to creat fb?","Python",
        "French","JavaScript","Php","None",4
        ],
]

levels = [1000,2000,3000,5000,10000,20000,50000,80000,160000,320000]

money=0
for i in range(0,len(questions)):
    question = questions[i]
print(f"question for Rs.{levels[i]}")
print(f"a.{question[1]}           b.{question[2]}")
print(f"c.{question[3]}           d.{question[4]}")
reply = int(input("Enter your Answer(1-4)"))
if(reply == question[-1]):
    print(f"Correct answer , you have won Rs.{levels[i]}")    
    if(i == 4):
        money = 10000
    elif(i == 9):
        money = 320000
    elif(i == 14):
     money = 1000000
    else:
        print("wrong answer") 
        





