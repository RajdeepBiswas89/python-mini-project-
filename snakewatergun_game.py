import random
user=int(input("enter 0 for snake,\nenter 1 for water,\nenter 2 for gun : "))
computer=random.randint(0,2)
def choices(computer,user):
    if(user<0 or user>2):
     print("invalid input,please input number between 0 and 2")
     exit()
    if (computer==user):
      return 0
    elif ((user==0) and (computer==2)):
       return -1
    elif((user==1) and (computer==0)):
       return -1
    elif((user==2) and (computer==1)):
       return -1
    else:    
       return 1
select=choices(computer,user)
if(select==0):
   print("match draw")
elif(select==1):
   print(f"you won\n computer choose={computer}\n user choice={user}")
else:
   print(f"you lose! computer won\n computer choose={computer}\n user choice={user} ")
