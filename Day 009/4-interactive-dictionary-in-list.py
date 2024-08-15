travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country, visits, cities_visited):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities_visited": cities_visited
    })
    
    print(f"You've visited {country} {visits} times.")
    print(f"You've been to {cities_visited[0]} and {cities_visited[1]}.")

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)