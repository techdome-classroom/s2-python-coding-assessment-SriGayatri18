class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        matching_brackets = {')': '(', '}': '{', ']': '['}
        
        stack = []
        
        for char in s:
            
            if char in matching_brackets:
                
                if stack and stack[-1] == matching_brackets[char]:
                    stack.pop()  
                else:
                    return False  
            else:
               
                stack.append(char)
        
     
        return not stack


solution = Solution()
test_cases = ["()", "()[]{}", "(]", "([{}])", "((()))", "{[()()]}", "(())("]
for i, test in enumerate(test_cases):
    result = solution.isValid(test)
    print(f"Test Case {i+1}: Input: {test} -> Output: {result}")



  

