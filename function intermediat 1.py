import random
def randInt(min= 0 , max= 100 ):
    if(min>max):
        return "min cannot be bigger than max"
    if(max<0):
        return "max cannot be smaller than zero"
    num = min + (random.random())*max-min
    return round(num)
print(randInt())
print(randInt(40,30))
#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

