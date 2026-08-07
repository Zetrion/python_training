

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    graph = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    visited = set()
    recStack = set()

    def bfs(course):
        queue = [course]
        visited.add(course)
        recStack.add(course)

        while queue:
            current = queue.pop(0)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    recStack.add(neighbor)
                    queue.append(neighbor)
                elif neighbor in recStack:
                    return False
            recStack.remove(current)
        return True