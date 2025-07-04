#!/usr/bin/env python3
"""
Crop Recommendation System Runner
A simple script to run the crop recommendation application.
"""

import os
import sys
import subprocess

def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import flask
        import webview
        import joblib
        import numpy
        print("✅ All dependencies are installed!")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please install dependencies using: pip install -r crop_app3/requirements.txt")
        return False

def main():
    """Main function to run the crop recommendation system."""
    print("🌾 Crop Recommendation System")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists("crop_app3/crop_app.py"):
        print("❌ Error: crop_app3/crop_app.py not found!")
        print("Please run this script from the project root directory.")
        return
    
    # Check dependencies
    if not check_dependencies():
        return
    
    print("🚀 Starting Crop Recommendation System...")
    print("📝 Note: The application will open in a desktop window.")
    print("=" * 40)
    
    try:
        # Change to the crop_app3 directory and run the application
        os.chdir("crop_app3")
        subprocess.run([sys.executable, "crop_app.py"], check=True)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user.")
    except Exception as e:
        print(f"❌ Error running application: {e}")
        print("Please make sure all dependencies are installed correctly.")

if __name__ == "__main__":
    main() 