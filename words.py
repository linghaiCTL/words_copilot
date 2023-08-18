import pandas as pd
import random
import os
import sys

path=os.path.abspath(os.path.dirname(sys.argv[0]))
file_path=path+'\\GRE_words.xlsx'
data=pd.read_excel(file_path)
word_list=[data.iloc[i].tolist() for i in range(data.shape[0])]

#print(word_list)

score=0
county=0
error_list=[]
ever_error_list=[]
print (len(word_list))
os.system('cls')
print ("Welcome to the GRE word test!")

while True:
    county+=1
    iferror=False
    if error_list and (random.randint(0,10)>9):
        rand=random.randint(0,len(error_list)-1)
        pair=error_list[rand]
        error_list.pop(rand)
        ever_error_list.append(pair)
        iferror=True
            
    if not iferror:
        while True:
            if not word_list:
                print ("You have finished all the words! Congratulations!")
                print (f"Your final score is {score} .")
                print ("Press any key to quit.")   
                input()
                exit()
            rand=random.randint(0,len(word_list)-1)
            pair=word_list[rand]
            if type(pair[0])==str:
                break
            word_list.pop(rand)
            continue
    print (f"Word {county}:")
    print("press any key to show the meaning")
    print (pair[0])
    str1=input()
    print (pair[1])
    print ("if your answer is correct, press enter. If not, type in the correct answer.")
    while True:
        str2=input()
        if str2==pair[1]:
            print ("work hard next time!")
            error_list.append(pair)
            if pair in ever_error_list:
                score-=5
                print("You have seen this word before, so you lose 5 points this time.")
            else:
                score-=1
            break
        elif str2=='':
            print ("Correct!")
            break
        else:
            print ("Wrong! Try again. Please be more careful.")
    if(county%10==0):
        print (f"Your score is {score} in the first {county} words.")
        print ("Press any key to continue.")
        input()
    print ("Press q to quit, or press any key to continue.")
    if input()=='q':
        break
    os.system('cls')
