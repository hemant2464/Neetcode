from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        result = []

        # Possible moves: right, left, down, up
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Create a set of adjacent character pairs for faster word filtering
        adjacent_pairs = set()
        for i in range(rows):
            for j in range(cols - 1):
                adjacent_pairs.add(board[i][j] + board[i][j + 1])
        for j in range(cols):
            for i in range(rows - 1):
                adjacent_pairs.add(board[i][j] + board[i + 1][j])

        # Check each word in the list
        for word in words:
            is_possible = True
            # Check adjacent character pairs of the word
            for i in range(len(word) - 1):
                pair = word[i:i + 2]
                if pair not in adjacent_pairs and pair[::-1] not in adjacent_pairs:
                    is_possible = False
                    break
            # If not possible, skip to the next word
            if not is_possible:
                continue
            # If possible, search for the word in the board
            if self.searchWord(word, rows, cols, board, directions):
                result.append(word)
        return result

    def searchWord(self, word, rows, cols, board, directions) -> bool:
        # Helper function to check if the word exists starting from a given position
        if word[:4] == word[0] * 4:
            word = ''.join([c for c in reversed(word)])
        # Initialize starting positions and visited set
        starting_positions = []
        stack = []
        visited = set()
        # Find all starting positions
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    starting_positions.append((i, j))
        # Explore words using Depth-First Search
        for start in starting_positions:
            stack.append(start)
            visited.add((start,))
            length = 1
            while stack and length < len(word):
                x, y = stack[-1]
                for direction in directions:
                    new_x, new_y = x + direction[0], y + direction[1]
                    if 0 <= new_x < rows and 0 <= new_y < cols:
                        if board[new_x][new_y] == word[length]:
                            if (new_x, new_y) not in stack and tuple(stack) + ((new_x, new_y),) not in visited:
                                stack.append((new_x, new_y))
                                visited.add(tuple(stack))
                                length += 1
                                if length == len(word):
                                    return True
                                break
                else:
                    stack.pop()
                    length -= 1
        return False