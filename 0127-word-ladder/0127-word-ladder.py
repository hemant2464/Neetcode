from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        queue = deque([(beginWord, 1)])
        word_length = len(beginWord)
        
        while queue:
            current_word, transformations = queue.popleft()
            if current_word == endWord:
                return transformations
            
            for i in range(word_length):
                for j in range(26):
                    next_word = current_word[:i] + chr(97 + j) + current_word[i + 1:]
                    if next_word in word_set:
                        word_set.remove(next_word)
                        queue.append((next_word, transformations + 1))
        
        return 0