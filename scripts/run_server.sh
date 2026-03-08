#!/bin/bash
# Script to run the Flask server

# Set environment variables
export FLASK_ENV=development
export DEV_API_TOKEN=dev-token-123
export DATABASE_URL=sqlite:///app.db
export MODEL_DIR=./models

# Create necessary directories
mkdir -p data/raw
mkdir -p data/synthetic
mkdir -p models

# Run the Flask application
python backend/app.py
