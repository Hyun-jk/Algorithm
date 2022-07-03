#SuperSum >>>어렵다아아
k,n = map(int,input().split())

def superSum(k,n):
   if k ==0 and n >0:
         return n
    
    #SuperSum(k,n)=SuperSum(k−1,1)+SuperSum(k−1,2)+...+SuperSum(k−1,n)
     