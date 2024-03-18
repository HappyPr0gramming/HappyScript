import func
import Memory
import random
import math

codelist = []
var1 = None

while True:
    code = input('HappyScript >>> ')

    #detect type of operation
    startfunc = func.parenthesis1(code)
    endfunc = func.parenthesis2(code)
    insideparenthesis = code[startfunc + 1:endfunc]

    #convert the arguments
    arg1 = func.bracket1(code)
    arg2 = func.bracket2(code)
    insideargs = code[arg1 + 1:arg2]

    #covert the class
    class1 = func.cls1(code)
    class2 = func.cls2(code)
    insideclass = code[class1 + 1:class2]

    #convert the slashes
    slasha = func.slash1(code)
    slashb = func.slash2(code)
    insideslash = code[slasha + 1:slashb]

    if insideparenthesis == '^':
        intsideargs = int(insideargs)
        print(intsideargs ** 2)
        
    elif insideparenthesis == 'text':
        print(insideargs)

    elif insideparenthesis == 'rangen':
        intsideargs = int(insideargs)
        print (random.randint(0, intsideargs))

    elif insideparenthesis == 'ask':
        input(insideargs)

    elif insideparenthesis == 'imp':
        if insideargs == 'canvas':
            import turtle

    elif insideclass == 'canvas':
        x = turtle.Screen()
        x.title('HappyScript Canvas')
        intsideargs = int(insideargs)
        if insideparenthesis == 'forward':
            turtle.forward(intsideargs)
        if insideparenthesis == 'right':
            turtle.right(intsideargs)
        if insideparenthesis == 'left':
            turtle.left(intsideargs)
        if insideparenthesis == 'back':
            turtle.forward(0 - intsideargs)

    elif insideclass == 'var':
        if insideparenthesis == 'define':
            var1 = insideargs
        if insideparenthesis == 'show':
            print(var1)

    elif insideslash == 'memory':
        Memory.store(insideargs, codelist)

    elif insideslash == 'list memory':
        print(codelist)

    elif insideparenthesis == 'squareroot':
        intsideargs = int(insideargs)
        try:
            print(math.sqrt(intsideargs))
        except:
            print('ERROR')
            print('THE INTEGER YOU JUST ENTERED IS NOT VALID')
        
    else:
        print('SYNTAX ERROR!')
        print('the text you just entered is not valid')