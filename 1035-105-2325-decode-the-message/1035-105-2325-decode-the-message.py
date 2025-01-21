class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        substitution_map = {}
        current_char = 'a' 
        
        for char in key:
            if char != ' ' and char not in substitution_map:
                substitution_map[char] = current_char
                current_char = chr(ord(current_char) + 1)  
        decoded_message = []
        for char in message:
            if char == ' ':
                decoded_message.append(' ')  
            else:
                decoded_message.append(substitution_map[char])  

        return ''.join(decoded_message)