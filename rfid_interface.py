"""
rfid_interface.py

Provides an abstraction for interacting with the RC522 RFID module
using the SimpleMFRC522 library. Supports reading tag data, writing
custom messages, and clearing tag contents.

Author: Francisco “Paco” Lorenzo
Date: 2025-04-06
""" 
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

class RFIDManager:
    """
    Class for managing RFID tag operations using the RC522 module.
    """
    
    def __init__(self): # Initializes the RFID reader object.
        self.reader = SimpleMFRC522()

    def read_tag(self): # Waits for a tag to be placed on the reader and reads its ID and text. Returns tuple.
        print("📶 Scan a tag to read...")
        id, text = self.reader.read()
        print(f"🔑 ID: {id}")
        print(f"📝 Text: {text.strip()}")
        return id, text.strip()

    def write_tag(self, data): # Writes the provided arg data string to a blank RFID tag.
        print("📶 Hold a blank tag to write...")
        self.reader.write(data)
        print(f"✅ Wrote data: {data}")
    
   
    def clear_tag(self): # Overwrites the tag with null characters to simulate data erasure.
        self.reader.write("\0" * 16)  # Writes 16 null characters


    def cleanup(self): # Cleans up GPIO resources (should be called on script exit).
        GPIO.cleanup()
