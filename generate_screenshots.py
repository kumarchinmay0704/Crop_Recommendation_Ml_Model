#!/usr/bin/env python3
"""
Screenshot Generator for Crop Recommendation System
This script helps generate screenshots for the README documentation.
"""

import os
import time
import subprocess
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    """Set up Chrome driver for taking screenshots."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1200,800")
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except Exception as e:
        print(f"❌ Error setting up Chrome driver: {e}")
        print("Please install Chrome and ChromeDriver")
        return None

def take_screenshot(driver, url, filename, wait_for_element=None):
    """Take a screenshot of a webpage."""
    try:
        driver.get(url)
        
        if wait_for_element:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, wait_for_element))
            )
        
        # Wait a bit for page to load completely
        time.sleep(2)
        
        # Create screenshots directory if it doesn't exist
        os.makedirs("screenshots", exist_ok=True)
        
        # Take screenshot
        screenshot_path = os.path.join("screenshots", filename)
        driver.save_screenshot(screenshot_path)
        print(f"✅ Screenshot saved: {screenshot_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error taking screenshot of {url}: {e}")
        return False

def test_application_running():
    """Test if the application is running."""
    try:
        response = requests.get('http://localhost:5000/', timeout=5)
        return response.status_code == 200
    except:
        return False

def main():
    """Main function to generate screenshots."""
    print("📸 Generating Screenshots for Crop Recommendation System")
    print("=" * 50)
    
    # Check if application is running
    print("🔍 Checking if application is running...")
    if not test_application_running():
        print("❌ Application is not running!")
        print("Please start the application first:")
        print("   python crop_app3/crop_app.py")
        return
    
    print("✅ Application is running!")
    
    # Set up driver
    driver = setup_driver()
    if not driver:
        return
    
    try:
        # Take screenshots
        screenshots = [
            {
                "url": "http://localhost:5000/",
                "filename": "home_page.png",
                "description": "Home Page"
            },
            {
                "url": "http://localhost:5000/Predict",
                "filename": "prediction_form.png",
                "description": "Prediction Form"
            }
        ]
        
        print("\n📸 Taking screenshots...")
        for screenshot in screenshots:
            print(f"\n📷 Taking screenshot: {screenshot['description']}")
            success = take_screenshot(
                driver, 
                screenshot["url"], 
                screenshot["filename"]
            )
            if success:
                print(f"✅ {screenshot['description']} screenshot completed")
            else:
                print(f"❌ {screenshot['description']} screenshot failed")
        
        print("\n🎉 Screenshot generation completed!")
        print("📁 Screenshots saved in the 'screenshots' directory")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main() 