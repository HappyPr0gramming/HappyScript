#This is where I will define all the functions
#For the interpreter of happyscript!

def convert(a):
    return int(a)

##########################
def parenthesis1(a):
    return a.find('(')

def parenthesis2(a):
    return a.find(')')
##########################

##########################
#detect arguments
def bracket1(a):
    return a.find('[')

def bracket2(a):
    return a.find(']')
##########################

##########################
def cls1(a):
    return a.find('{')

def cls2(a):
    return a.find('}')
##########################

##########################
def slash1(a):
    return a.find('?')

def slash2(a):
    return a.find('¿')
##########################