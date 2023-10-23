from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flight_graph = defaultdict(list)
        itinerary = []

        def dfs(airport: str) -> None:
            destinations = flight_graph[airport]
            while destinations:
                next_destination = destinations.pop()
                dfs(next_destination)
            itinerary.append(airport)

        # Populate the flight graph using ticket information
        for ticket in tickets:
            from_airport, to_airport = ticket
            flight_graph[from_airport].append(to_airport)

        # Sort destinations in reverse order for lexical ordering
        for destinations in flight_graph.values():
            destinations.sort(reverse=True)

        # Start DFS from JFK airport
        dfs("JFK")

        # Reverse the itinerary to get the correct order
        return itinerary[::-1]