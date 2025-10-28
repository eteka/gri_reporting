#!/usr/bin/env python3
"""
GRI Sustainability Reporting Platform
A comprehensive web application for creating GRI-compliant sustainability reports
"""

from app import app

if __name__ == '__main__':
    print("🌱 Starting GRI Sustainability Reporting Platform...")
    print("📊 Access your platform at: http://localhost:5000")
    print("📚 Built with GRI Standards compliance in mind")
    print("🚀 Ready to simplify your sustainability reporting!")
    
    app.run(debug=True, host='0.0.0.0', port=5000)