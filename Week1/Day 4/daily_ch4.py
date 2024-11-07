# DAILY CHALLENGE  "MATRIX"

matrix=[
    ['7','i','i'],
    ['T','s','x'],
    ['h','%','?'],
    ['i',' ','#'],
    ['s','M',' '],
    ['$','a',' '],
    ['#','t','%'],
    ['^','r','!']
     ]

def decryption(matrix):
    mes_code=[]
    columns=len(matrix[0])
    for column in range(columns):
        for row in matrix:
            char=row[column]
            if char.isalpha():
                mes_code.append(char)
            elif mes_code and mes_code[-1] != " ":
                mes_code.append(" ")
    crypt=''.join(mes_code)
    print(crypt)
decryption(matrix)
        
