#Draw a pyramid with the number of lines asked to the user

lines= int(input('Number of lines \n'))
for numLines in range(lines):
    spaces = lines - numLines - 1
    asterisks=  1 + numLines *2
    print(" "*spaces+"*"*asterisks)


 