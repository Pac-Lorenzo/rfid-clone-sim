# write_clone.py
from rfid_interface import RFIDManager
import json
from datetime import datetime

rfid = RFIDManager()

try:
    # Load saved tag data
    with open("original_tag.json", "r") as f:
        tag_data = json.load(f)

    rfid.write_tag(tag_data["text"])

    # Log cloning event
    with open("clone_log.txt", "a") as log:
        log.write(f"[{datetime.now()}] Cloned tag ID: {tag_data['id']} with text: '{tag_data['text']}'\n")

    print("📝 Cloning event logged.")
finally:
    rfid.cleanup()
