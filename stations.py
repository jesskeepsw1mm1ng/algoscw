# weighted adjacency list including the station and the following station as well as the durations

graph = {
    'Bakerloo': {'Harrow & Wealstone': {'Kenton': 8}},
    'Central': {'Epping': {'Theydon Bois': 10}},
    'Circle': {'Edgeware': {'Paddington': 6}},
    'District': {'Upminster': {'Upminster Bridge': 7}},
    'Hammersmith & City': {'Barking': {'East Ham': 2}},
    'Jubilee': {'Stanmore': {'Canons Park': 3}}
}

# function to get travel duration between two stations for a tube line

def get_travel_duration(tube_line, start_station, destination_station):
    return graph.get(tube_line, {}).get(start_station, {}).get(destination_station, float('inf'))

tube_line = 'Bakerloo'
start_station = 'Harrow & Wealstone'
destination_station = 'Kenton'
duration = get_travel_duration(tube_line, start_station, destination_station)
print(f'Travel duration on {tube_line} line from {start_station} to {destination_station}: {duration} minutes')

tube_line = 'Bakerloo'
start_station = 'Harrow & Wealstone'
destination_station = 'Kenton'
duration = get_travel_duration(tube_line, start_station, destination_station)
print(f'Travel duration on {tube_line} line from {start_station} to {destination_station}: {duration} minutes')

