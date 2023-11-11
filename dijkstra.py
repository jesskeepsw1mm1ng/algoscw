import heapq

class Station:
    def __init__(self, name):
        self.name = name
        self.connected_stations = []

    def add_connection(self, station, weight):
        self.connected_stations.append((station, weight))


class RoutePlanner:
    def __init__(self):
        self.stations = {}

    def add_station(self, station):
        self.stations[station.name] = station

    def dijkstra(self, start_station):
        distances = {station: float('infinity') for station in self.stations}
        distances[start_station.name] = 0
        priority_queue = [(0, start_station)]

        while priority_queue:
            current_distance, current_station = heapq.heappop(priority_queue)

            if current_distance > distances[current_station.name]:
                continue

            for neighbor, weight in current_station.connected_stations:
                distance = current_distance + weight

                if distance < distances[neighbor.name]:
                    distances[neighbor.name] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def find_shortest_paths(self, start_station):
        distances = self.dijkstra(start_station)
        shortest_paths = {station: distances[station.name] for station in self.stations}
        return shortest_paths


# Define station names and travel times
station_names = {
    "Bakerloo Line": ["Paddington", "Baker Street", "Oxford Circus", "Piccadilly Circus", "Charing Cross"],
    "Circle Line": ["King's Cross St. Pancras", "Euston Square", "Liverpool Street", "Victoria", "Paddington"],
    # Add more lines and stations with actual data
}

station_travel_times = {
    "Bakerloo Line": [3, 2, 3, 2, 3],  # Travel times in minutes between stations
    "Circle Line": [3, 2, 4, 3, 3],
    # Add more lines with travel times
}

# Create Station objects and add connections with travel times
stations = {}
for line, stops in station_names.items():
    line_stations = []
    travel_times = station_travel_times[line]
    for i, stop in enumerate(stops):
        station = Station(stop)
        if i > 0:
            station.add_connection(line_stations[i - 1], travel_times[i - 1])
        line_stations.append(station)
        stations[stop] = station

    for i, station in enumerate(line_stations):
        if i < len(line_stations) - 1:
            station.add_connection(line_stations[i + 1], travel_times[i])

# Example usage:
planner = RoutePlanner()
for station in stations.values():
    planner.add_station(station)

start_station_name = input("Enter the starting station: ").strip()

if start_station_name in stations:
    start_station = stations[start_station_name]
    shortest_paths = planner.find_shortest_paths(start_station)

    print("Shortest paths from", start_station_name)
    for station_name, distance in shortest_paths.items():
        print(f"{station_name}: {distance} minutes away")
else:
    print("Invalid station name. Please try again.")
