#2018 카카오
#3차 파일명 정렬
def solution(files):
    answer = []
    #초기화를 왜 시켜줘야하지?
    head,number,tail ='','',''
    for file in files:
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                
                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                
                answer.append([head,number,tail])
                head,number,tail ='','',''#초기화를 시켜주면 답이 맞는다
                break
            
    answer.sort(key=lambda x:(x[0].upper(),int(x[1])))
    
    return [''.join(i) for i in answer]

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
files2 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]