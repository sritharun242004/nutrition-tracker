"""
FoodHealth AI - Run Script
Final Year Project

Usage:
    python run.py

Then open: http://localhost:5000
"""
import os
import sys
os.environ.setdefault('PORT', '5001')

# Ensure we can import from project root
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, create_tables

if __name__ == '__main__':
    print("=" * 50)
    print("  FoodHealth AI - Food Detection & Health System")
    print("  Final Year Project")
    print("=" * 50)

    # Initialize database and directories
    create_tables()

    print("\n[INFO] Starting server...")
    print("[INFO] Open http://localhost:5001 in your browser")
    print("[INFO] Press Ctrl+C to stop\n")

    port = int(os.environ.get('PORT', 5001))
    app.run(debug=False, host='0.0.0.0', port=port, use_reloader=False)
