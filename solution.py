from map import cities

def get_neighbors(city):
    return cities[city]['neighbors'].keys()

def get_geo_coordinates(city):
    info = cities[city]
    return info['x'], info['y']

def get_real_distance(city1, city2):
    return cities[city1]['neighbors'][city2]


def find(start, end):
    visited = set()

    stack = []
    
    stack.append((start, []))
    
    while stack:
        city, path = stack.pop()
        
        if city == end:
            return path + [city]
        
        visited.add(city)
        
        neighbors = get_neighbors(city)
        
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append((neighbor, path + [city]))
    
    return []

