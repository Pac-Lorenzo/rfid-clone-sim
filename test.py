# rfid_test.py
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

reader = SimpleMFRC522()

try:
    print("📶 Ready to scan an RFID tag. Hold one near the reader...")
    id, text = reader.read()
    print(f"✅ Tag detected!")
    print(f"🔑 ID: {id}")
    print(f"📝 Text: {text}")
except Exception as e:
    print(f"❌ Error reading tag: {e}")
finally:
    GPIO.cleanup()
