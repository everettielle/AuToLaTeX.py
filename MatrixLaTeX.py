INV_MINUS_DEF = '\\newcommand{\\p}{\\phantom{-}}'
INV_MINUS = '\\p'
VECTOR_SKELETON = '\\begin{{bmatrix}}\n{}\n\\end{{bmatrix}}'
vector_in = ''
output = ''
userInput = input("Enter the matrix (a b / c d): ")
userInput_list = userInput.split()
output += INV_MINUS_DEF + '\n'
contain_minus = False
contain_minus_first = False
for i, e in enumerate(userInput_list):
    if(e == '/'):
        pass
    elif(int(e) < 0):
        if(i == 0):
            contain_minus_first = True
        elif(userInput_list[i-1] == '/'):
            contain_minus_first = True
        else:
            contain_minus = True
for i, e in enumerate(userInput_list):
    if(e == '/'):
        vector_in += '\\\\\n'
    elif(int(e) < 0):
        vector_in += '  ' + e + ' '
    else:
        if(contain_minus_first and not contain_minus):
            if(i == 0 or userInput_list[i-1] == '/'):
                vector_in += INV_MINUS + ' ' + e + ' '
            else:
                vector_in += e + ' '
        elif(contain_minus):
            vector_in += INV_MINUS + ' ' + e + ' '
        else:
            vector_in += e + ' '
    if(i+1 == len(userInput_list)):
        pass
    elif(userInput_list[i+1] == '/' or e == '/'):
        pass
    else:
        vector_in += '& '

output += VECTOR_SKELETON.format(vector_in)
print(output)