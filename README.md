# Steins Gate - Array Trend Predictor

A Flask-based machine learning API that analyzes numerical arrays and predicts their trend patterns. The application uses a pre-trained machine learning model to classify array trends into one of five categories: NO_COUNT, INCREASE, DECREASE, STABLE, or VARIANCE.

## 🚀 Live Demo

The application is deployed and available at: [https://steins--gate.herokuapp.com](https://steins--gate.herokuapp.com)

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Array Trend Analysis**: Analyzes numerical arrays to predict trend patterns
- **RESTful API**: Simple JSON-based API for easy integration
- **Machine Learning**: Uses scikit-learn based pre-trained model
- **Data Normalization**: Automatically normalizes input data for better predictions
- **Error Handling**: Comprehensive error handling with informative messages
- **Heroku Ready**: Configured for easy deployment to Heroku

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/owaiskaifi/steins-gate.git
cd steins-gate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The application will start on `http://localhost:5000`

## 📖 Usage

### Basic API Call

Send a POST request to the `/predict` endpoint with a JSON payload containing an array of numbers:

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"arr": [1, 2, 3, 4, 5]}'
```

### Python Example

```python
import requests
import json

url = 'http://localhost:5000/predict'
data = {'arr': [1.0, 2.5, 1.8, 3.2, 2.1]}

response = requests.post(url, json=data)
result = response.json()
print(result)  # {'STATUS': 'INCREASE'}
```

### JavaScript Example

```javascript
fetch('http://localhost:5000/predict', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({arr: [1, 2, 3, 4, 5]})
})
.then(response => response.json())
.then(data => console.log(data));
```

## 📡 API Documentation

### Endpoints

#### `GET /`
Returns the main web interface (404 page with API information).

#### `POST /predict`
Predicts the trend of a numerical array.

**Request Body:**
```json
{
  "arr": [1.0, 2.5, 1.8, 3.2, 2.1]
}
```

**Response (Success):**
```json
{
  "STATUS": "INCREASE"
}
```

**Response (Error):**
```json
{
  "ERROR": "Wrong input format"
}
```

### Status Types

The API returns one of the following trend statuses:

- `NO_COUNT`: No significant data or trend detected
- `INCREASE`: Array shows an increasing trend
- `DECREASE`: Array shows a decreasing trend  
- `STABLE`: Array values remain relatively stable
- `VARIANCE`: Array shows high variance without clear direction

### Data Processing

The API automatically:
1. Converts input to numpy array
2. Normalizes data by dividing by maximum value × 2
3. Feeds normalized data to the ML model
4. Returns human-readable status

## 📁 Project Structure

```
steins-gate/
├── app.py                 # Main Flask application
├── model.pkl             # Pre-trained ML model
├── requirements.txt      # Python dependencies
├── Procfile             # Heroku deployment config
├── send.py              # Example API usage script
├── templates/           # HTML templates
│   ├── index.html       # Main landing page
│   ├── index2.html      # Alternative 404 page
│   └── light-bulb.png   # UI asset
├── LICENSE              # MIT License
└── README.md           # This file
```

### Key Files

- **`app.py`**: Core Flask application with prediction endpoint
- **`model.pkl`**: Serialized scikit-learn model for trend prediction
- **`requirements.txt`**: All Python dependencies needed to run the app
- **`Procfile`**: Heroku configuration for web dyno
- **`send.py`**: Example script demonstrating API usage

## 🚀 Deployment

### Heroku Deployment

The application is configured for Heroku deployment:

1. Install Heroku CLI
2. Login to Heroku: `heroku login`
3. Create app: `heroku create your-app-name`
4. Deploy: `git push heroku main`

The `Procfile` is already configured with: `web: gunicorn app:app`

### Docker Deployment

Create a `Dockerfile` (not included):

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🧪 Testing

Use the provided `send.py` script to test the API:

```bash
python send.py
```

Note: Update the URL in `send.py` to match your deployment:
- Local: `http://127.0.0.1:5000/predict`
- Production: `https://your-app.herokuapp.com/predict`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Muhammad Owais**
- GitHub: [@owaiskaifi](https://github.com/owaiskaifi)

## 📞 Support

If you encounter any issues or have questions:

1. Check the API response for error messages
2. Ensure your input data is in the correct JSON format
3. Verify the array contains numerical values
4. Open an issue on GitHub for bugs or feature requests

---

Made with ❤️ using Flask and scikit-learn
