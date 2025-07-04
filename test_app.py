#!/usr/bin/env python3
"""
Test script for Crop Recommendation System
"""

import requests
import time
import sys
import os

def test_home_page():
    """Test the home page endpoint."""
    try:
        response = requests.get('http://localhost:5000/')
        if response.status_code == 200:
            print("✅ Home page test passed")
            return True
        else:
            print(f"❌ Home page test failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Make sure the application is running.")
        return False

def test_prediction_form():
    """Test the prediction form endpoint."""
    try:
        response = requests.get('http://localhost:5000/Predict')
        if response.status_code == 200:
            print("✅ Prediction form test passed")
            return True
        else:
            print(f"❌ Prediction form test failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server.")
        return False

def test_prediction():
    """Test the prediction endpoint with sample data."""
    sample_data = {
        'Nitrogen': 50,
        'Phosphorus': 40,
        'Potassium': 30,
        'Temperature': 25,
        'Humidity': 70,
        'ph': 6.5,
        'Rainfall': 100
    }
    
    try:
        response = requests.post('http://localhost:5000/form', data=sample_data)
        if response.status_code == 200:
            if 'prediction' in response.text.lower():
                print("✅ Prediction test passed")
                return True
            else:
                print("❌ Prediction test failed: No prediction found in response")
                return False
        else:
            print(f"❌ Prediction test failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server.")
        return False

def test_invalid_input():
    """Test the prediction endpoint with invalid data."""
    invalid_data = {
        'Nitrogen': 150,  # Out of range
        'Phosphorus': 40,
        'Potassium': 30,
        'Temperature': 25,
        'Humidity': 70,
        'ph': 15,  # Out of range
        'Rainfall': 100
    }
    
    try:
        response = requests.post('http://localhost:5000/form', data=invalid_data)
        if response.status_code == 200:
            if 'error' in response.text.lower() or 'sorry' in response.text.lower():
                print("✅ Invalid input test passed")
                return True
            else:
                print("❌ Invalid input test failed: No error message found")
                return False
        else:
            print(f"❌ Invalid input test failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server.")
        return False

def main():
    """Run all tests."""
    print("🧪 Testing Crop Recommendation System")
    print("=" * 40)
    
    # Check if the application is running
    print("📝 Note: Make sure the application is running before running tests.")
    print("   Start the application with: python crop_app3/crop_app.py")
    print("=" * 40)
    
    tests = [
        ("Home Page", test_home_page),
        ("Prediction Form", test_prediction_form),
        ("Prediction", test_prediction),
        ("Invalid Input", test_invalid_input)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Testing {test_name}...")
        if test_func():
            passed += 1
        time.sleep(1)  # Small delay between tests
    
    print("\n" + "=" * 40)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The application is working correctly.")
        return 0
    else:
        print("⚠️  Some tests failed. Please check the application.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 