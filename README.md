# 🔐 RFID Car Key Cloning Simulation

This project simulates a car key cloning attack using an RFID RC522 module and a Raspberry Pi. It demonstrates how weak RFID-based systems (typically found in older vehicles or access control systems) can be compromised and cloned — even if the tag’s UID is different.

---

## 🚗 Project Features

- Read and save tag memory (simulate a stolen key)
- Clone the saved memory to a new RFID tag
- Simulate weak vs secure car systems:
  - Weak: grants access based on text alone
  - Strong: verifies both UID and text
- Manually write and wipe tags
- Logs all access and cloning activity

---

## 📁 Folder Structure

| File                | Purpose                                      |
|---------------------|----------------------------------------------|
| `access_control.py` | Run access simulation (choose weak/strong)   |
| `read_original.py`  | Read original key (steal memory)             |
| `write_clone.py`    | Clone stolen data onto another tag           |
| `manual_write.py`   | Manually write any data to a tag             |
| `manual_clear.py`   | Wipe a tag’s memory clean                    |
| `rfid_interface.py` | Hardware abstraction for RC522 reader/writer |
| `original_tag.json` | Stores stolen key data (optional)            |
| `access_log.txt`    | Log of access attempts (optional)            |
| `clone_log.txt`     | Log of cloning events (optional)             |

---

## 🧪 How to Run

1. 🔧 Install dependencies:
   ```bash
   pip3 install mfrc522 RPi.GPIO --break-system-packages
