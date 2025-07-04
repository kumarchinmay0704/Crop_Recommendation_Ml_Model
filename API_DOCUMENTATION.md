# API Documentation - Crop Recommendation System

## Overview

The Crop Recommendation System provides a RESTful API for predicting crop recommendations based on soil and environmental parameters.

## Base URL

```
http://localhost:5000
```

## Endpoints

### 1. Home Page

**GET** `/`

Returns the home page of the application.

**Response:**
- Content-Type: `text/html`
- Body: HTML content of the home page

### 2. Prediction Form

**GET** `/Predict`

Returns the prediction form page where users can input soil parameters.

**Response:**
- Content-Type: `text/html`
- Body: HTML form for input parameters

### 3. Crop Prediction

**POST** `/form`

Predicts the best crop based on input parameters.

**Request Body:**
```json
{
  "Nitrogen": 50,
  "Phosphorus": 40,
  "Potassium": 30,
  "Temperature": 25,
  "Humidity": 70,
  "ph": 6.5,
  "Rainfall": 100
}
```

**Parameters:**
- `Nitrogen` (float): Nitrogen content in soil (0-100 mg/kg)
- `Phosphorus` (float): Phosphorus content in soil (0-100 mg/kg)
- `Potassium` (float): Potassium content in soil (0-100 mg/kg)
- `Temperature` (float): Average temperature (0-100°C)
- `Humidity` (float): Relative humidity (0-100%)
- `ph` (float): Soil pH level (0-14)
- `Rainfall` (float): Annual rainfall (0-10000 mm)

**Response:**
- Content-Type: `text/html`
- Body: HTML page with prediction results and crop image

**Error Response:**
If input validation fails:
- Status: 200
- Body: Error message in plain text

## Input Validation

The API validates the following constraints:
- pH must be between 0 and 14
- Temperature must be below 100°C
- Humidity must be positive (> 0)
- All parameters must be numeric

## Example Usage

### Using curl

```bash
curl -X POST http://localhost:5000/form \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "Nitrogen=50&Phosphorus=40&Potassium=30&Temperature=25&Humidity=70&ph=6.5&Rainfall=100"
```

### Using Python requests

```python
import requests

data = {
    'Nitrogen': 50,
    'Phosphorus': 40,
    'Potassium': 30,
    'Temperature': 25,
    'Humidity': 70,
    'ph': 6.5,
    'Rainfall': 100
}

response = requests.post('http://localhost:5000/form', data=data)
print(response.text)
```

## Supported Crops

The system can predict the following crops:
- rice
- maize
- chickpea
- kidneybeans
- pigeonpeas
- mothbeans
- mungbean
- blackgram
- lentil
- pomegranate
- banana
- mango
- grapes
- watermelon
- muskmelon
- apple
- orange
- papaya
- coconut
- cotton
- jute
- coffee

## Error Handling

The API returns appropriate error messages for:
- Invalid input parameters
- Missing required fields
- Out-of-range values
- Non-numeric inputs

## Rate Limiting

Currently, no rate limiting is implemented. Consider implementing rate limiting for production use.

## Security Considerations

- Input validation is performed on all parameters
- No sensitive data is stored
- Consider implementing HTTPS for production use
- Add authentication if needed for production deployment 