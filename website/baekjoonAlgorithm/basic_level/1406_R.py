#에디터(스택)
"""
-시간제한 0.3  메모리제한 512MB
-insert, remove O(N)의 시간 복잡도를 가지고 있다.
-그래서 시간초과가 났다.

string_list = list(input())
cursor = len(string_list)

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'P':
        string_list.insert(cursor, command[1])
        cursor += 1
  
    elif command[0] == 'L':
        if cursor > 0:
            cursor -= 1

    elif command[0] =='D':
        if cursor < len(string_list):
            cursor += 1
  
    else:
        if cursor > 0:
            string_list.remove(string_list[cursor-1])

print(''.join(string_list))
"""

#자료구조 - 이중연결 리스트
#삽입, 삭제 O(1) , 탐색 O(n)의 시간복잡도를 가진다
import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []
for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())
    elif command[0] =='D':
        if st2:
            st1.append(st2.pop())
    elif command[0] == 'B':
        if st1:
            st1.pop()
    else:
        st1.append(command[1])

        
st1.extend(reversed(st2))
print(''.join(st1))