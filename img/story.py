#my python story

def greeting():
    print("hello...")
    response=input('do you want to play? yes/no ')
    return response
def second_choice():
    print ("great")
    response=input('are you playing sports?... ')
def haters():#exits game
    print("lame,idiota, bye then.")
def opened():
    print("i like you for playing")
def not_opened():
    print("you must not be my friend")
x=greeting()


if x=="yes":
    y=second_choice()
    if y=="yes":
        opened()
    else:
        not_opened()
else:
    haters()
print(y)


print("This is a new game! please!  Would you like to start over? (yes/no)")
response=input()
response=response.lower()

if response=='yes' or response=='y':
    print ("Great!  Let's get started!")
    game = True
else:
    print("Ok,let us sleep")


while game==False:
    print('ok bye then')

    
print("Should I study or play minecraft with you (study/s/playing minecraft/minecraft)?")
response=input()
response=response.lower()
game==True
if response=='s' or response=='study':
    print ("Good!  Now we can be productive together as one.....would you like to nap or nap better first? (nap/nap)")
    game = True 
else:
    print('well at least i can rest my tired eyes...we should nap together')
    game==False

print("would you like to take a nap wit me? (of course/yes)")
response=input()
response=response.lower()
game==True
if response=='of course' or response=='yes':
    print("i do not want to sleep with you ")
    game==True
else:
    print("you must not want to sleep then huh")
    game==False
print('instead of sleeping would you rather say bye and go our seperate ways forever? ( i hate you, leave)')
response=input()
response=response.lower()
game==True
if response=='i hate you' or response=='leave':
    game==False
elif response=='no' or response=='never':
    print('i still do not want you around leave')
    game==False










    
