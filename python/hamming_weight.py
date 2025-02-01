# problem: https://leetcode.com/problems/number-of-1-bits/

# solution 1
# def hamming_weight(n:int):  
#    result = 0 
#    while (n!=0):
#       if(n & 1==1):
#          result +=1
#       n= n >> 1
#    return result

# solution 2 is: n & (n-1) while n>0
def hamming_weight(n:int):  
   result = 0 
   while n:
      n= n &(n-1)
      result +=1
   return result

def hamming_weight_executor():
   print("reverse Bits")
   print(hamming_weight(11),"->3")
   print(hamming_weight(2147483645),"->30")
   