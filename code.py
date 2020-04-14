#define a function called "add10" that takes in 1 argument
# and literally adds 10.  Return the value as well
def add10(  num ):
    a  = num + 10
    return  a



# answer = call the function. print the answer
var                  =  1234
# ^name of variable     ^ value that im assigning


                        # <------   add10( 5 )
answer               =    add10( 5 )
# ^name of variable     ^ value that im assigning
print( answer )



# define a function called "isAbove0" that checks if a number is above 0
# takes in 1 value, a number
# performs a check
# if greater then 0   -> true
#                else -> false

def isAbove0( num ):           # <- whole line is called the function signature

    if num > 0:
        return True
    else:
        return False

# create a variable "result" and assign it to isAbove0(-5)
# print the variable "result"
result = isAbove0( -99 )
        # ^ isAbove0 never returned anything. selfish function
print( result)
