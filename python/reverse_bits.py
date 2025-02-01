# problem: https://leetcode.com/problems/reverse-bits/
# history 1/2/25 - 2 hour

# solution 1
def reverse_bits(n:int):  
   result = 0 
   for i in range(32):
      temp_bit = (n >>i)&1
      result = result | (temp_bit<<(31-i))
   return result

def reverse_bits_executor():
   print("reverse Bits")
   
   print(reverse_bits(0b00000010100101000001111010011100),"->964176192")
   print(reverse_bits(0b11111111111111111111111111111101),"->3221225471")


