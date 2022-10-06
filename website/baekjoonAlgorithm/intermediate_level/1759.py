from itertools import combinations
#암호 만들기
L,C = map(int,input().split())
letter_list = list(input().split())
letter_list.sort()
vowel_list = ("a","e","i","o","u")

for password in combinations(letter_list,L):
    vowel_count,consonant_count = 0,0

    for letter in password:
        if letter in vowel_list: #모음의 수 확인
            vowel_count +=1 
        else: #자음의 수 확인
            consonant_count +=1

    if vowel_count >0 and consonant_count >=2 :
        print("".join(password))


