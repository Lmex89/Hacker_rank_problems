

from math import sqrt,floor,ceil

def check_len(vect_str):
    
    tam = len(vect_str[0])
    uno = []
    cola = []
    for i in vect_str:
        if (tam == len(i)):
           uno.append(i)
        else:
            cola.append(i) 
    return uno,cola


def print_encode_square(uno,cola):
    
    encode_b = []
    contador = 0
    for i in range(0,len(uno[0])):
        temp = ''
        for j in uno:
            temp = temp + j[contador]
        encode_b.append(temp)
        contador +=1
    if len(cola)> 0:    
        cola_list = list(cola[0])
        contador = 0
            
        for m in range(0,len(uno[0])):
            if m < len(cola_list):
                temp = ""
                temp = encode_b[contador] + cola_list[m]
                encode_b[contador] =temp
                
            elif m >= len(cola_list):
                temp =""
                temp += encode_b[contador]
                encode_b[contador] =temp
            contador +=1
    elif (len(cola) == 0):
        contador = 0
        for m in range(0,len(uno[0])):
            temp =""
            temp += encode_b[contador]
            encode_b[contador] =temp
            contador +=1
        
    return encode_b

def final_string(encode_final):
    
    ans = ""
    for i in encode_final:
        ans = ans + i + " "
        
    return ans
    
    
def encryption(string):
    
    length = len(string)
    row = floor(sqrt(len(string)))
    column = ceil(sqrt(len(string)))

    L = row * column

    if (L >= length):
        minimum = min((row,column))
        maximum = max((row,column))
        contador = 1
        text =  []
        for i in range(0,row):
            text.append(string[(i*maximum):maximum*contador])
            contador += 1
   
    elif (L < length):
        maximum = max(row,column)
        text = []
        contador = 1
        for i in range(0,maximum):
            text.append(string[(i*maximum):maximum*contador])
            contador += 1
       
    uno,cola = check_len(text)
    encode = print_encode_square(uno,cola)
    string_encode = final_string(encode)
    return (string_encode)

string="haveaniceday"
print(encryption(string))