from rfid_interface import RFIDManager

rfid = RFIDManager()

try:
    data = input("Enter the data to write onto the tag: ")
    rfid.write_tag(data)
    print(f"✅ Tag has been written!")

finally:
    rfid.cleanup()