'''
test.py 

A simple test script to verify that the RC522 RFID reader is connected
and functioning correctly with the Raspberry Pi.

Author: Francisco “Paco” Lorenzo
Date: 2025-04-06
'''

from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

reader = SimpleMFRC522()

try:
    print("📶 Ready to scan an RFID tag. Hold one near the reader...")
    id, text = reader.read() # Attempt to read from a tag

    
    print(f"✅ Tag detected!")
    print(f"🔑 ID: {id}") # Display the tag data
    print(f"📝 Text: {text}") # Display the tag data
except Exception as e:
    print(f"❌ Error reading tag: {e}") # Catch any errors during read operation
finally:
    GPIO.cleanup() # Always clean up GPIO pins
