#최대공약수와 최소 고배수
import math
n,m = map(int,input().split())
gcd_num = math.gcd(n,m)
lcd_num = n * m // gcd_num
print(gcd_num)
print(lcd_num)