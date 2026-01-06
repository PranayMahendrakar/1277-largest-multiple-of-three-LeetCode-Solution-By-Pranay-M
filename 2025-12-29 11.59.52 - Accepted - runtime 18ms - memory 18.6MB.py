class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        # Sort digits in descending order
        digits.sort(reverse=True)
        
        # If all zeros, return "0"
        if digits[0] == 0:
            return "0"
        
        # Group digits by remainder when divided by 3
        remainder = [[], [], []]
        total = 0
        for d in digits:
            remainder[d % 3].append(d)
            total += d
        
        # If total % 3 == 0, we can use all digits
        if total % 3 == 0:
            return ''.join(map(str, digits))
        
        # If total % 3 == 1, remove one digit with remainder 1 or two digits with remainder 2
        if total % 3 == 1:
            if remainder[1]:
                remainder[1].pop()
            elif len(remainder[2]) >= 2:
                remainder[2].pop()
                remainder[2].pop()
            else:
                return ""
        # If total % 3 == 2, remove one digit with remainder 2 or two digits with remainder 1
        else:
            if remainder[2]:
                remainder[2].pop()
            elif len(remainder[1]) >= 2:
                remainder[1].pop()
                remainder[1].pop()
            else:
                return ""
        
        # Combine all remaining digits and sort in descending order
        result = remainder[0] + remainder[1] + remainder[2]
        result.sort(reverse=True)
        
        if not result:
            return ""
        if result[0] == 0:
            return "0"
        
        return ''.join(map(str, result))