"""
manual_write.py

Allows a user to manually enter text and write it to an RFID tag
using the RC522 module. Useful for testing or assigning custom IDs.

Author: Francisco “Paco” Lorenzo
Date: 2025-04-06
"""

from rfid_interface import RFIDManager

rfid = RFIDManager() # Prompt user for input to write to tag

try:
    data = input("Enter the data to write onto the tag: ") 
    rfid.write_tag(data) # Write the entered data to the tag
    print(f"✅ Tag has been written!")

finally:
    rfid.cleanup() # Clean up GPIO resources
