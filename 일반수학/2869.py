A, B, V = map(int, input().split())

x = (V-B)/(A-B)
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)
#간단하게?
#a,b,v = map(int,input().split())
#k = (v-b)/(a-b)
#print(int(k) if k == int(k) else int(k)+1)	#삼항연산자