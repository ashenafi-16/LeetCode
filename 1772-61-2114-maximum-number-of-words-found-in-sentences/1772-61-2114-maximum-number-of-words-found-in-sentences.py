class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum_num_word = 0
        for word in sentences:
            splited_list = word.split()
            if maximum_num_word < len(splited_list):
                maximum_num_word = len(splited_list)
        return maximum_num_word