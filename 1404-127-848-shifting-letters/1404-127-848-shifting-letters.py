class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s_list = list(s)
        total = sum(shifts)
        for i in range(len(shifts)):
            new_ascii_value = ord(s_list[i]) + total % 26 
            if new_ascii_value > 122:
                new_ascii_value = new_ascii_value - 26
            total -= shifts[i]
            s_list[i] = chr(new_ascii_value)
        return "".join(s_list)
