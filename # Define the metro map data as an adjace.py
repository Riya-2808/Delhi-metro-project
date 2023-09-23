# Define the metro map data as an adjacency matrix
metro_map = [
    [0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 0]
]

# Define the number of metro stations
num_stations = len(metro_map)

# Initialize the distance matrix with maximum values
distance = [[float('inf')] * num_stations for _ in range(num_stations)]

# Initialize the next station matrix for path reconstruction
next_station = [[-1] * num_stations for _ in range(num_stations)]

# Perform the Modified Floyd-Warshall Algorithm
for i in range(num_stations):
    for j in range(num_stations):
        if i == j:
            distance[i][j] = 0
        elif metro_map[i][j] == 1:
            distance[i][j] = 1
        else:
            distance[i][j] = float('inf')

# Calculate the shortest path with the minimum number of metro stops
for k in range(num_stations):
    for i in range(num_stations):
        for j in range(num_stations):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
                next_station[i][j] = k

# Function to reconstruct the path with minimum metro stops
def reconstruct_path(source, destination):
    if next_station[source][destination] == -1:
        return [source, destination]
    else:
        intermediate = next_station[source][destination]
        path1 = reconstruct_path(source, intermediate)
        path2 = reconstruct_path(intermediate, destination)
        return path1[:-1] + path2

# Example usage
source = 0
destination = 6
path = reconstruct_path(source, destination)
num_stops = len(path) - 1
print("Shortest path with minimum metro stops:", path)
print("Number of metro stops:", num_stops)
