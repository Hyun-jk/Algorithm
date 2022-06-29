#문자열 재정렬
data = input()
result = []
value = 0

#알파벳인지 확인하기(isalpha) vs (isdigit) 숫자인지 파악하는 함수
#isalpha() 함수는 문자열의 구성이 알파벳인지에 대해서 확인하는 함수.
#주의 사항 -->문자열에 숫자 및 공백이 포함되어 있으면 False를 리턴한다.
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

#알파벳 오름차순 정렬
result.sort()

#숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

#최종 결과 출력(리스트를 문자열로 변환하여 출력)
#join함수 ---> '구분자'.join(리스트) 로 반환해줌
print(''.join(result))