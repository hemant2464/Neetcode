class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        foundValidTripletForFirstInTarget = False
        foundValidTripletForSecondInTarget = False
        foundValidTripletForThirdInTarget = False

        for triplet in triplets:
            x, y, z = triplet
            if x == target[0] and y <= target[1] and z <= target[2]:
                foundValidTripletForFirstInTarget = True
            if x <= target[0] and y == target[1] and z <= target[2]:
                foundValidTripletForSecondInTarget = True
            if x <= target[0] and y <= target[1] and z == target[2]:
                foundValidTripletForThirdInTarget = True
            
            # If all conditions are met, no need to check further
            if foundValidTripletForFirstInTarget and foundValidTripletForSecondInTarget and foundValidTripletForThirdInTarget:
                return True

        return foundValidTripletForFirstInTarget and foundValidTripletForSecondInTarget and foundValidTripletForThirdInTarget