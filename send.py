import requests
import json

# Update URL to match your deployment
url = 'http://127.0.0.1:5000/predict'  # Local development
# url = 'https://steins--gate.herokuapp.com/predict'  # Production

# Example data - array of numbers to analyze for trends
data = {'arr': [1.0, 2.5, 1.8, 3.2, 2.1, 4.0]}

# Send POST request with JSON data
response = requests.post(url, json=data)
result = response.json()
print(f"Input: {data['arr']}")
print(f"Prediction: {result}")

# Test with different patterns
test_cases = [
    {'arr': [1, 2, 3, 4, 5], 'description': 'Increasing trend'},
    {'arr': [5, 4, 3, 2, 1], 'description': 'Decreasing trend'},
    {'arr': [3, 3, 3, 3, 3], 'description': 'Stable trend'},
    {'arr': [1, 5, 2, 4, 3], 'description': 'Variable trend'},
    {'arr': [0, 0, 0], 'description': 'No count case'}
]

print("\n--- Testing different patterns ---")
for test in test_cases:
    response = requests.post(url, json={'arr': test['arr']})
    result = response.json()
    print(f"{test['description']}: {test['arr']} -> {result}")
