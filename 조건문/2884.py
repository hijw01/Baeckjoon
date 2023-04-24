hour, min = map(int, input().split())

if min < 45:
    hour = hour-1
    min = 60 + min

H, M = map(int, input().split())

if M < 45 :	
    if H == 0 :
        H = 23
        M += 60
    else :	
        H -= 1	
        M += 60
        
print(H, M-45)