# read_original.py
from rfid_interface import RFIDManager
import json

rfid = RFIDManager()

try:
    id, text = rfid.read_tag()

    # Save data to JSON file
    with open("original_tag.json", "w") as f:
        json.dump({"id": id, "text": text}, f)

    print("📁 Tag data saved to original_tag.json")
finally:
    rfid.cleanup()
