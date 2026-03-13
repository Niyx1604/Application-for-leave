#!/usr/bin/env python3
"""
Save the provided logos to the logos directory
"""
import base64
import os

# Create logos directory
os.makedirs("logos", exist_ok=True)

print("Logos directory created. Please save the provided logo images as:")
print("1. logos/philhealth_logo.png")
print("2. logos/bagong_pilipinas_logo.png") 
print("3. logos/socotec_logo.png")

print("\nThe logos should be saved from the images you provided in the chat.")
print("Once saved, the application will use them automatically.")