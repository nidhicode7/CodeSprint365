'''
Problem 273:Convert a non-negative integer num to its English words representation.

 
Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
'''
class Solution:
    def numberToWords(self, num: int) -> str:
        # Base case: if the number is 0
        if num == 0:
            return "Zero"

        # Words for numbers < 20
        less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                        "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", 
                        "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", 
                        "Nineteen"]

        # Words for tens place (20, 30, ..., 90)
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", 
                "Seventy", "Eighty", "Ninety"]

  
        thousands = ["", "Thousand", "Million", "Billion"]

       
        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return less_than_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return less_than_20[n // 100] + " Hundred " + helper(n % 100)

        res = ""
        i = 0  

        while num > 0:
            curr = num % 1000  
            if curr != 0:
                res = helper(curr) + thousands[i] + " " + res  # add group word
            num = num // 1000 
            i += 1

        return res.strip()  
