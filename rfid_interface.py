# Paco Lorenzo
# 4/6/2025
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

class RFIDManager:
    def __init__(self):
        self.reader = SimpleMFRC522()

    def read_tag(self):
        print("📶 Scan a tag to read...")
        id, text = self.reader.read()
        print(f"🔑 ID: {id}")
        print(f"📝 Text: {text.strip()}")
        return id, text.strip()

    def write_tag(self, data):
        print("📶 Hold a blank tag to write...")
        self.reader.write(data)
        print(f"✅ Wrote data: {data}")
    
    # Clear Text Data
    def clear_tag(self): 
        self.reader.write("\0" * 16)  # Writes 16 null characters


    def cleanup(self):
        GPIO.cleanup()
