from typing import List

test = [0,0]
test1 = [0, 0,1, 0, 0, 0, 0,1, 0, 0, 0, 0,1, 0, 0, 0, 0, 0,1, 0,1, 0, 0, 0,1, 0, 0,1, 0, 0, 0,1, 0,1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]



def minimum_jumps(lista_nums: List[int])  -> int:
    
    
    step = 0
    lenght = len(lista_nums)-1
    count_steps=0   
    if lenght == 1:
        return 1
    while step < lenght:
        
        if step+2 <= lenght and lista_nums[step+2] == 1:
            step +=1
            count_steps += 1
            if lista_nums[step] == 1:
                print("no solution")
                break
        elif step+2 <= lenght:
            step +=2
            count_steps += 1
            if step+1 <= lenght and lista_nums[step+1] != 1 :
                if step+2 <=lenght and  lista_nums[step+2] == 1:
                    step +=1
                    count_steps += 1
                elif step+1 ==lenght:
                    step+=1
                    count_steps += 1
       
    return count_steps


print(minimum_jumps(test))

def test_answer():
    assert minimum_jumps(test) == 4
