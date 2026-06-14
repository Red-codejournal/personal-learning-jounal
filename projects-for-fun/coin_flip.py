import random
outcome = ["head", "tail"]
flip = int(input("How many flip : "))
    
def flipping(flip):
    for i in range(flip):
        print(random.choice(outcome), end=" ")

def flipping2(flip,probb):
    for i in range(flip):
        if random.random() > probb:
            print("head", end=" ")
        else : 
            print("tail", end=" ")


prob = str(input("Adjust probability (y/n)? "))
if prob=="y" :
    x=float(input("What is the probability of tail? "))
    flipping2(flip,x)
elif prob=="n":
    flipping(flip)