#number-guesser
import random as rand
guess_list = []
leader_list = [8,9,10,11,12]
leader_name_list = ["John","Harry", "David", "Isaac","Oliver" ]
#functions
def num_guess(num):
    global correct
    correct = False
    global rand_num
    global playagain
    global leader_list
    global leader_name_list
    global name
    x = 0
    #print(rand_num)
    if num <= 100:
        if num == rand_num:
            guess_list.append(guess)
            print("Correct")
            print("You guessed " + str(len(guess_list)) +" times!")
            #print(guess_list)
            correct = True
            for number in leader_list:
                if len(guess_list) < leader_list[x]:
                    leader_list.insert(x,len(guess_list))
                    leader_name_list.insert(x,name)
                    leader_list.pop()
                    guess_list.append(1)
                    guess_list.append(1)
                    guess_list.append(1)
                    guess_list.append(1)
                    guess_list.append(1)
                    guess_list.append(1)
                    guess_list.append(1)
                    guess_list.append(1)
                    guess_list.append(1)
                    guess_list.append(1)
                x += 1                    
            guess_list.pop()
            guess_list.pop()
            guess_list.pop()
            guess_list.pop()
            guess_list.pop()
            guess_list.pop()
            guess_list.pop()
            guess_list.pop()
            guess_list.pop()
            guess_list.pop()
            #print(guess_list)
            while len(guess_list) > 0:
              guess_list.pop()
            #print(guess_list)      
            print(str(leader_name_list[0]) + " " + str(leader_list[0]))
            print(str(leader_name_list[1]) + " " + str(leader_list[1]))
            print(str(leader_name_list[2]) + " " + str(leader_list[2]))
            print(str(leader_name_list[3]) + " " + str(leader_list[3]))
            print(str(leader_name_list[4]) + " " + str(leader_list[4]))
            playagain = input ("would you like to play guess the number? y or n \n")
            return playagain
        elif num <= rand_num:
            print("Too Low!")
            guess_list.append(guess)
        elif num >= rand_num:
            print("Too High!")
            guess_list.append(guess)
    return correct

#events
correct = False
playagain = ("y")
while playagain == ("y"):
    name = input("what is your name ")
    rand_num = rand.randint(1,100)
    while correct != True:    
        guess = int(input("pick a number 1-100 \n"))
        num_guess(guess)
    correct = False
print("goodbye")