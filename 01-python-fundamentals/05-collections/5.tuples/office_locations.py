locations = (
    ("Mumbai", 19.0760, 72.8777),
    ("Pune", 18.5204, 73.8567),
    ("Bangalore", 12.9716, 77.5946)
)

for location in locations:
    city, latitude, longitude = location
    print(f"city: {city}")
    print(f"latitude: {latitude}")
    print(f"longitude: {longitude}")
    print("-----------------------------")