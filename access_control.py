
from rfid_interface import RFIDManager
from datetime import datetime

# The text stored on the RFID tag is the key; the description is just a label
AUTHORIZED_KEYS = {
    "Toyota RAV4 Key1": "Car Owner",
    "Authorized Technician": "Service Role"
}

# These are known, trusted UIDs (used by secure/newer system)
AUTHORIZED_UIDS = [
    "302489600483",  # Add real trusted UID(s) here
]

def run_weak_system():
    print("\n[Weak System] Access Based on Tag Text Only")
    id, text = rfid.read_tag()

    if text in AUTHORIZED_KEYS:
        print(f"✅ Access Granted to: {AUTHORIZED_KEYS[text]}")
        result = "GRANTED"
    else:
        print("❌ Access Denied.")
        result = "DENIED"

    log_access(id, text, result, mode="WEAK")


def run_strong_system():
    print("\n[Strong System] Access Based on Text AND UID")
    id, text = rfid.read_tag()

    if text in AUTHORIZED_KEYS and str(id) in AUTHORIZED_UIDS:
        print(f"✅ Access Granted to: {AUTHORIZED_KEYS[text]}")
        result = "GRANTED"
    elif text in AUTHORIZED_KEYS:
        print("⚠️ Possible Clone Detected: Text matches, but UID is untrusted.")
        result = "CLONE"
    else:
        print("❌ Access Denied.")
        result = "DENIED"

    log_access(id, text, result, mode="STRONG")


def log_access(uid, text, result, mode):
    with open("access_log.txt", "a") as f:
        f.write(f"[{datetime.now()}] MODE: {mode} | UID: {uid} | TEXT: '{text}' | RESULT: {result}\n")


rfid = RFIDManager()

try:
    print("\n=== RFID ACCESS PORTAL ===")
    print("1 - Simulate Old/Weak Car System")
    print("2 - Simulate Newer/Secure Car System")
    choice = input("Select mode [1/2]: ")

    if choice == "1":
        run_weak_system()
    elif choice == "2":
        run_strong_system()
    else:
        print("Invalid selection.")

finally:
    rfid.cleanup()
