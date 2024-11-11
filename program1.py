class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty; otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the top element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # Check if the stack is empty (all brackets matched)
        return not stack
        pass







    



  

