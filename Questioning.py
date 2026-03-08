# we will create a program who will work like "Python-Quiz_Game" show!!!

print("++++++++++Phython-Quiz-Game+++++++++++")
choice=input("ARE YOU READ??")
prize=0
if choice.lower()=="yes":
    print("HEREs YOUR QUESTIONS ARE: ")
    print("**************************")
    #question number 1:
    print("QUESTION # 01")
    print("Which country is shaped like a boot??      (4000/RS)")
    answer=["1.BRAZIL","2.ITALY","3.INDIA",'4.AUSTRILLIA']
    for i in answer:
        print(i)
    print("Choose answer")
    ans=(input("Let us know : "))
    if ans=="2" or ans.lower()=="italy":
        print("Yes Correct Answer is \"ITALY\"")
        prize=prize+4000
        print("Prize become : ",prize)
    else:
        print("Sorry Your answer is wrong!")
        print("Current Prize money is : ",prize)
    #Question number 2 :
    print("\n************************************")
    print("QUESTON # 02")
    print("Which one is the Tallest Animal??             (10000/RS)")
    animal=["1.ElEPHANT",'2.GIRAFFE','3.KANGROO','4.OSTRICH']
    for ani in animal:
        print(ani)
    print("Choose answer")
    ans=(input("Let us know : "))
    if ans=="2" or ans.lower()=="Giraffee":
        print("Yes Your Answer is Correct!!")
        prize=prize+10000
        print("Your Prize become : ",prize)
    else:
        print("Sorry Your anwer is Wrong....")
        print("Current Prize money is : ",prize)
    #question number 3 :
    print("\n*************************************")
    print("Question # 03")
    print("What is the capital city of South Korea??                    50000/RS")
    city=['1.BUSAN','2.TOKYO','3.SEOUL','4.BANGKOK']
    for i in city:
        print(i)
    print("Choose answer")
    ans=(input("Let us know : "))
    if ans=="3"  or ans.lower()=="Seoul":
        print("Yes Answer is Correct!!")
        prize=prize+50000
        print("Your Prize become : ",prize)
    else:
        print("Wrong Answer...")
        print("Current Prize Money is : ",prize)
    #question number 4 :
    print("\n**************************************")
    print("QUESTION # 04")
    print("Which Planet is closest to the Sun??                                15000/RS")
    planet=['1.EARTH','2.JUPITER','3.MARS','4.MERCURY']
    for i in planet:
        print(i)
    print("Choose answer")
    ans=(input("Let us know : "))
    if ans=="4" or ans.lower()=="Mercury":
        print("Your Answer is Correct!!")
        prize=prize+15000
        print("Prize become : ",prize)
    else:
        print("Answer is wrong ...")
        print("Current Prize money is : ",prize)
    #question number 5 : 
    print("\n****************************************")
    print("QUESTION # 05")
    print("Which is the largest ocean in the World??                            90000/RS")
    ocean=['1.ATLANTIC','2.INDIAN','3.PACIFIC','4.ARCTIC']
    for i in ocean:
        print(i)
    print("Choose answer")
    ans=(input("Let us know : "))
    if ans=="3" or ans.lower()=="Pacific":
        print("Yes Answer is Correct!!")
        prize=prize+90000
        print("Prize become : ",prize)
    else:
        print("Sorry Wrong.......")
        print("Current prize money is : ",prize)
