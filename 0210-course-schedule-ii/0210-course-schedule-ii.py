class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_prerequisites = {c: [] for c in range(numCourses)}
        for course, prereq in prerequisites:
            course_prerequisites[course].append(prereq)

        order = []
        visited, in_cycle = set(), set()

        def dfs(course):
            if course in in_cycle:
                return False
            if course in visited:
                return True

            in_cycle.add(course)
            for prerequisite in course_prerequisites[course]:
                if not dfs(prerequisite):
                    return False
            in_cycle.remove(course)
            visited.add(course)
            order.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return order