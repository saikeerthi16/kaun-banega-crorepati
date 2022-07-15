print("Let's start the game")
print("Here is your question:")
question=["Q.1 How many continents are there?",
"Q.2 what is the capital of india?",
"Q.3 which course navgurukul teach?"]
option=[["seven","eight","nine","five"],
["chennai","chandigarh","delhi","mumbai"],
["counselling","software","tourism","agriculture"]]
solution=[1,3,2]
ans_list=[
["1.seven","2.eight"],
["2.chandigarh","3.delhi"],
["1.counselling","2.software"]]
i=0
count=0
price=0
while i<len(question):
    print(question[i])
    j=i
    s_no=0
    while s_no<len(option[i]):
        a=option[j][s_no]
        print(s_no+1,a)
        s_no+=1
    if count==0:                                          
        lifeline=input("Do u want lifeline:-yes/no : ")
        if lifeline=="yes":
            count+=1
            print("select your option") 
            sel_opt=0
            b=i
            while sel_opt<len(ans_list[i]):
                c=ans_list[b][sel_opt]
                sel_opt+=1
                print(c)
            ans=int(input("choose your answer : ")) 
            if ans==solution[i]:
                price+=1000
                print("correct answer, and your winning price is",price)
                print("congratulations")
                print("your next question is:")
            else:
                print("wrong answer")
                break  
        else:
            ans1=int(input("choose your answer : "))
            if ans1==solution[i]:
                price+=1000
                print("correct answer, and your winning price is",price) 
                print("congratulations")
            else:
                print("wrong answer")
                break
    else:
        ans2=int(input("choose your answer: "))
        if ans2==solution[i]:
            price+=1000
            print("correct answer and your winning price is",price)
            print("congratulations")
            print("your next question is:-")   
        else:
            print("wrong answer") 
            break
    i+=1







