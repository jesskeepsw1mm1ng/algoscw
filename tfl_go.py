import heapq

graph = {
    'bakerloo': {'harrow & wealstone': {'kenton': 2},{'south kenton': 2},{'north wembly': 2}},
    'central': {'epping': {'theydon bois': 10}},
    'circle': {'edgeware': {'paddington': 6}},
    'district': {'upminster': {'upminster bridge': 7}},
    'hammersmith & city': {'barking': {'east ham': 2}},
    'jubilee': {'stanmore': {'canons park': 3}}
}

# dijkstra's algorithm to find shortest paths
def dijkstra(graph, start):
    distances = {station: float('inf') for line in graph.values() for station in line.keys()}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_station = heapq.heappop(priority_queue)

        if current_distance > distances[current_station]:
            continue

        for neighbor, weight in graph[current_station].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Find shortest paths for each station on the Bakerloo line
tube_line = 'bakerloo'
shortest_paths = dijkstra(graph[tube_line], start_station)

for station, duration in shortest_paths.items():
    print(f'Shortest travel duration from {start_station} to {station} on {tube_line} line: {duration} minutes')
