"""
write_clone.py

This script clones a previously scanned RFID tag by writing the saved text
data (from original_tag.json) to a blank RFID tag using the RC522 module.

It also logs the cloning event with a timestamp to clone_log.txt.

Author: Francisco “Paco” Lorenzo
Date: 2025-04-06
"""

from rfid_interface import RFIDManager
import json
from datetime import datetime

rfid = RFIDManager() # Initialize RFID reader/writer

try:
   
    with open("original_tag.json", "r") as f: # Load saved tag data
        tag_data = json.load(f)

    rfid.write_tag(tag_data["text"]) # Write the saved text to a new tag

    
    with open("clone_log.txt", "a") as log: # Log cloning event
        log.write(f"[{datetime.now()}] Cloned tag ID: {tag_data['id']} with text: '{tag_data['text']}'\n")

    print("📝 Cloning event logged.")
finally:
    rfid.cleanup() # Clean up GPIO resources
