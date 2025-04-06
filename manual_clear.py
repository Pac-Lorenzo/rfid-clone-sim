from rfid_interface import RFIDManager

rfid = RFIDManager()

try:
    print("📶 Ready to clear an RFID tag. Hold one near the reader...")
    rfid.clear_tag()
    print(f"✅ Tag cleared!")
finally:
    rfid.cleanup()