"""
read_original.py

This script reads an RFID tag's ID and stored text using the RC522 module,
then saves that data to a JSON file (original_tag.json) for later cloning.

Author: Francisco “Paco” Lorenzo
Date: 2025-04-06
"""

from rfid_interface import RFIDManager
import json

rfid = RFIDManager() # Initialize RFID reader

try:
    id, text = rfid.read_tag() # Read RFID tag

    
    with open("original_tag.json", "w") as f: # Save data to JSON file
        json.dump({"id": id, "text": text}, f)

    print("📁 Tag data saved to original_tag.json")
finally:
    rfid.cleanup() # Clean up GPIO resources
