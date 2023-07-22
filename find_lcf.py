#find_lcf
def lcf (a,b):
    if a > b :
        greater = a
    else:
        greater = b
    
        while(True):
            if(greater %  a == 0 ) and (greater % b == 0):
                result = greater
                break
            else:
                greater+=1
        return result
        
a = int(input("Enter No:"))
b = int(input("Enter N0:"))

print(f"lcm: {lcf(a,b)}")