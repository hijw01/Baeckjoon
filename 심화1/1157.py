word = input().lower() #소문자로 입력받음
word_list = list(set(word)) #단어에서 사용된 알파벳만 리스트에 넣음(중복 없이)
cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else: 
    print(word_list[(cnt.index(max(cnt)))].upper()) #제일 많이 사용된 문자 대문자로 출력