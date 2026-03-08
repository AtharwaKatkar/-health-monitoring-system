#!/usr/bin/env python3
"""
Script to generate synthetic CSI data for testing
"""
import os
import sys
import json
import numpy as np
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def generate_synthetic_data(num_samples=50, output_dir='data/synthetic'):
    """Generate synthetic CSI data for testing"""
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Generating {num_samples} synthetic CSI samples...")
    
    for i in range(num_samples):
        # Generate synthetic CSI data (simulating 3 antennas, 1000 samples)
        csi_data = np.random.randn(1000, 3) + 1j * np.random.randn(1000, 3)
        
        # Add some structure to make it more realistic
        t = np.linspace(0, 10, 1000)
        
        # Add respiratory component
        resp_freq = np.random.uniform(0.2, 0.4)  # 12-24 breaths per minute
        resp_amp = np.random.uniform(0.1, 0.5)
        csi_data += resp_amp * np.exp(1j * 2 * np.pi * resp_freq * t)[:, np.newaxis]
        
        # Add cardiac component
        cardiac_freq = np.random.uniform(1.0, 2.0)  # 60-120 bpm
        cardiac_amp = np.random.uniform(0.05, 0.2)
        csi_data += cardiac_amp * np.exp(1j * 2 * np.pi * cardiac_freq * t)[:, np.newaxis]
        
        # Add noise
        noise_level = np.random.uniform(0.01, 0.1)
        csi_data += noise_level * (np.random.randn(1000, 3) + 1j * np.random.randn(1000, 3))
        
        # Generate labels
        labels = {
            'respiration_rate': resp_freq * 60,  # Convert to breaths per minute
            'heart_rate': cardiac_freq * 60,     # Convert to beats per minute
            'hrv': np.random.uniform(20, 50),    # Random HRV
            'activity_label': np.random.choice(['normal', 'walking', 'sitting', 'standing', 'fall'])
        }
        
        # Save data (convert complex to real for JSON serialization)
        data = {
            'csi_data': np.abs(csi_data).tolist(),  # Use magnitude only
            'labels': labels
        }
        
        filename = os.path.join(output_dir, f'synthetic_{i:03d}.json')
        with open(filename, 'w') as f:
            json.dump(data, f)
        
        if (i + 1) % 10 == 0:
            print(f"Generated {i + 1}/{num_samples} samples")
    
    print(f"Synthetic data generation completed. Files saved to {output_dir}")

if __name__ == '__main__':
    generate_synthetic_data()
