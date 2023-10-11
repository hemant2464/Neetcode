class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        char_last_pos = {}
        for idx, char in enumerate(S):
            char_last_pos[char] = idx

        partitions = []
        start, last_position = 0, 0

        for idx, char in enumerate(S):
            last_position = max(last_position, char_last_pos[char])

            if idx == last_position:
                partitions.append(last_position - start + 1)
                start = idx + 1

        return partitions