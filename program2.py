class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to map Roman numerals to their respective integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # Iterate through the Roman numeral string
        for i in range(n):
            # If this value is less than the value of the next symbol, subtract it
            if i + 1 < n and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            else:
                total += roman_to_int[s[i]]
        
        return total


