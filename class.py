class Station:
    def __init__(self, name):
        self.name = name
        self.connected_stations = []

    def add_connection(self, station):
        self.connected_stations.append(station)


class TrainLine:
    def __init__(self, name):
        self.name = name
        self.stations = []

    def add_station(self, station):
        self.stations.append(station)


class RoutePlanner:
    def __init__(self):
        self.stations = {}

    def add_station(self, station):
        self.stations[station.name] = station

    def plan_route(self, start_station, end_station):
        visited = set()
        stack = [(start_station, [])]

        while stack:
            current_station, current_path = stack.pop()
            if current_station == end_station:
                return current_path + [current_station]

            if current_station in visited:
                continue

            visited.add(current_station)

            for neighbor in current_station.connected_stations:
                if neighbor not in visited:
                    stack.append((neighbor, current_path + [current_station]))

        return None  # No route found


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


def calculate_route_times(route, station_travel_times):
    total_time = 0
    boarding_time = 2  # Assuming 2 minutes for boarding at each station
    for i, station in enumerate(route[:-1]):
        line_name = None
        for line, stations in station_names.items():
            if station.name in stations and route[i + 1] in stations:
                line_name = line
                break
        if line_name:
            total_time += boarding_time + station_travel_times[line_name][stations.index(station.name)]
    return total_time

    # Create stations and train lines as before
    # ...

    # Create a route planner i indented this to fix the scope
    planner = RoutePlanner()
    for station in stations.values():
        planner.add_station(station)

    while True:
        start_station_name = input("Enter the starting station: ").strip()
        end_station_name = input("Enter the final station: ").strip()

        if start_station_name in stations and end_station_name in stations:
            start_station = stations[start_station_name]
            end_station = stations[end_station_name]

            route = planner.plan_route(start_station, end_station)

            if route:
                total_time = calculate_route_times(route, station_travel_times)
                print(f"Route from {start_station.name} to {end_station.name} via {route[1].name} on {route[0].name}:")
                print(" -> ".join(station.name for station in route))
                print(f"Total time: {total_time} minutes")
            else:
                print("No route found.")
        else:
            print("Invalid station names. Please try again.")
