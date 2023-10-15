from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        def backtrack(combination, index):
            if index == len(digits):
                results.append(combination)
                return

            current_digit = digits[index]
            letters = digit_to_letters[current_digit]
            for letter in letters:
                backtrack(combination + letter, index + 1)

        results = []
        backtrack('', 0)
        return results