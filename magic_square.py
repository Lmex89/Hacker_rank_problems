def extraLongFactorials(n):
    if n == 0 or n == 1:
        print(1)
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result

def is_palindrome(n):
    tam = len(n)
    fin = int(tam/2)
    for i in range(0,fin):
        if n[i] != n[tam-1]:
           return False
        else:
            tam = tam -1
    return True

def check_par(vector,i,maximum):
    lenght = len(vector)-1
    contador = 0
    if (vector[i] != vector[lenght-i] and vector[i] != maximum  and vector[lenght-i] != maximum):
        vector[i] = maximum
        contador +=1
    elif (vector[i] != vector[lenght-i] and vector[lenght-i] != maximum ):
         vector[lenght-i] = maximum
         contador +1
    elif (vector[i] != vector[lenght-i] and vector[i] != maximum ):
        vector[i] = maximum
        contador +=1

    return vector,contador

def solve(n, k, v):
    ch_set = set()
    for i in range(0,int(n/2)):
        if v[i] != v[n-i-1]:
            if k == 0:
                return -1
            k -= 1
            ch_set.add(i)
            if v[i] > v[n-i-1]:
                v[n-i-1] = v[i]
            else:
                v[i] = v[n-i-1]
    for i in range(0,int(n/2)):
        if k == 0:
            break
        if v[i] < '9':
            if i in ch_set:
                k -= 1
            elif k >= 2:
                k -= 2
            else:
                continue
            v[i] = '9'
            v[n-i-1] = '9'
    if k > 0 and n%2 == 1:
        v[n/2] = '9'
    return ''.join(v)

n, k = map(int, input().split())
v = [c for c in input().strip()]
print(solve(n, k, v))
