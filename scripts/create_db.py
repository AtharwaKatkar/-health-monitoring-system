#!/usr/bin/env python3
"""
Script to create and initialize the database
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend import create_app, db
from backend.models import Patient, Recording, Feature, Metric, Alert, ModelRun

def create_database():
    """Create database tables and add sample data"""
    app = create_app()
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Database tables created successfully")
        
        # Add sample patient
        sample_patient = Patient(
            name="Test Subject",
            age=72,
            conditions="COPD;Hypertension"
        )
        db.session.add(sample_patient)
        db.session.commit()
        
        print(f"Created sample patient with ID: {sample_patient.id}")
        print("Database initialization completed")

if __name__ == '__main__':
    create_database()
