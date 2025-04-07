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

## Equipment List
- [Raspberry Pi Zero 2 W](https://www.amazon.com/Pi-Zero-WH-Quad-Core-Bluetooth/dp/B0DKKXS4RV/ref=sr_1_1?crid=2VR6CEIAORCG1&dib=eyJ2IjoiMSJ9.KlhfpgHSKPo1ghamKtLQM0alINrbCoQhn-Ez1CAJaov4YWnC1cxI8k4aAVib31h4SQ9AVxwbOINlsdxp5mO9BfEDZsSq7TslLeG7slYauyesJ7uytFyshQ_PVM0mhShjM5QjUHVhdj8OP6u1qkykwusRTxDjcJiPNpAyQtv7YBOiBcDPOOp-u43qwY5N8IzOAGvHI6mE_ZhjNKsSnqXKrVZ1HiT8v4k8EfOANfOroVg.fsERPfWEK9gjXhEW6Z27ERRuUBrmR7kd4a6hlQcJv8U&dib_tag=se&keywords=raspberry%2Bpi%2Bzero%2B2%2Bw&qid=1744046917&sprefix=raspberry%2Bpi%2Bzero%2B2%2B%2Caps%2C130&sr=8-1&th=1) 
- [Micro SD Card (32GB+)](https://www.amazon.com/SanDisk-2-Pack-microSDHC-Memory-2x32GB/dp/B08J4HJ98L/ref=sr_1_3?crid=RK7M8M7JCSYY&dib=eyJ2IjoiMSJ9.-14J3gHOFbHKiyXMk5PaYNqTrD5JpQUTyqDrVcHVPj08Fcdgb_P9GeM-5YnBmnVX38aGySEs0nTq6zfo5XOqP-QWaaLjhrCQXGsaB4T7SnRF39l4wFPJkdtuBvpbaF8Er3iiaLNpMp3iglQFLRFmd-FDMMlQ18wElW5kkbk3O7YIST7RTWuHos5aV912_Gwd-9vAJCRHX7yXQEWtbaFlB_RBe4d5NaFJ4coj_vXLnrw.HsY_h39shdFoJiDm1VuyhP9tQHYz0Totk6Q8k9gXAT8&dib_tag=se&keywords=micro%2Bsd%2Bcard%2B32%2Bgb&qid=1744047542&sprefix=micro%2Bsd%2Bcard%2B32%2Bg%2Caps%2C135&sr=8-3&th=1)
- [Micro USB cable](https://www.amazon.com/Amazon-Basics-Charging-Transfer-Gold-Plated/dp/B0711PVX6Z/ref=sr_1_3?crid=3AYW4QKN966C0&dib=eyJ2IjoiMSJ9.6kEw1NDjxVNHbG3W-BdrmCkrDxZPjY4zlVfTNDwfJG4F_CMWflkMkVBkcnF8Px4Jme9-JtUwjbxO-HzB0IUys_HJt5_Lxy7ItJcRpPWu8RveVRZy9Mci0phhhJxYSjePfv-n2-RFJDH9PcD1_B_VRxBkULK5gWf4NM3bRR2Y6VMZ4kKcftK_ck1ORe-vOv_p3ZHvfmCfREXIN7oq4UNABPHnNJQ58no4_rJ5ZTNt94g.j8bBZJUzkfa3SxgSyNx-_ekWKlZAeE0cYGnKLq9I7j8&dib_tag=se&keywords=micro%2Busb%2Bcable%2Bfor%2Braspberry%2Bpi&qid=1744047609&sprefix=micro%2Busb%2Bcable%2Bfor%2Braspb%2Caps%2C122&sr=8-3&th=1)
- [RFID Module-RC522](https://www.amazon.com/SunFounder-Mifare-Reader-Arduino-Raspberry/dp/B07KGBJ9VG/ref=sr_1_8?crid=3J5OV0LPZ6Z2O&dib=eyJ2IjoiMSJ9.2BgAhpDQBZFRD2-EI6NfqCl1eJWQ7C10RvKDeF4Y4MDoTwqCWpTWZMK7-OQNKjSO9SRoXh413Oy_Vs3fhUq9-maMS8eqXE81hn58WcHG2RZio8tUKol5MpxImYxn-52NA69KSFgcATRPquc937_vXtsNoPRte5qhwnBwUFsVS-wJUQ2frr7Dn7L_FPQRXNSwtBnsq6x8A6e9TBvVYZzHMVoEbCd-dHdKy2Jo7HUYBeU.tSXlWJln0U2UrIkxps9fCDr5mK4bJ6KsAs9nSlVw4OQ&dib_tag=se&keywords=rfid+modules+soldered&qid=1744047677&sprefix=rfid+modules+soldered%2Caps%2C86&sr=8-8)
- [RFID Cards (2)](https://www.amazon.com/Meipire-13-56MHz-Classic-ISO14443A-Printable/dp/B07S63VT7X/ref=sr_1_2_sspa?crid=L2OL4P65M9EP&dib=eyJ2IjoiMSJ9.mgZeL9BgpbaafznZISMUkWSQCve7p0rxth0FrNqW1OXhtfcP8oeE9iSMKau_9SXeCBxhssrue3lg6pAEPfH4ncpBDfejOK20nRBo0dB5y_pWeOoQBVQVWIW-a_PfrLTIo5FQdcmGi9NjK6Z-QyXlC5ZZo0WPxK4nFwIDKyzn8D2egPHytv73mHIQtz9jSoT6w8_dRXbRZ4YWXJx4vSZXPpKgUmiSxz6E4HeyIaLVbP4WbXVuN_9Q6YrChBFLeHyOFZyLvd3NQBRPbGL990jeRxECDsLBp-X_GSFeW7vsMxI.4n649h_qnbCdCcFiOHkLV1XytjGLne-L1mXfVkmYGAg&dib_tag=se&keywords=rfid%2Bcard&qid=1744047726&sprefix=rfid%2Bcard%2Caps%2C103&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)
- [Breadboard & jumper wires](https://www.amazon.com/BOJACK-Values-Solderless-Breadboard-Flexible/dp/B08Y59P6D1/ref=sr_1_3?crid=2CEY1CCPHSWYY&dib=eyJ2IjoiMSJ9.5Z5yTwL-oa1r18Ah_zf9OXg0u1AVX54R3VfgSdqpBoRUNKgai9y4cFZQSmx0YU9Lmy-qrEeSR3vQfc8-tijcR50B8JLLGTJIXhMgl6MIYSnfPQmVmvcSF0M2w8enDXg7nAqCuSnsgrD0IGtH6DmlryNjCbzb7XZR6MpiOpKt1UGJWV0vH5zRaxLuddSwClZtJYmy_Gl1PbC8cwWrwqNA_mNis2-c7mvFFH0s40XneyA.xFhRILhM0hHLwoNCb82KdR8P7-A-LtIl_I7CG4MGltg&dib_tag=se&keywords=breadboard&qid=1744047799&sprefix=breadboar%2Caps%2C151&sr=8-3)

*Note that depending on which Pi and circuit design is chosen it may require different types of jumper wires. I recommend buying a presoldered Pi, GPIO extension board, and male to male jumper wires. This is the setup I used for the simulation. 

**Optional**
- [GPIO Extension Board](https://www.amazon.com/Quluxe-Breakout-Expansion-Assembled-Raspberry/dp/B08D3S6FGH/ref=sr_1_3?crid=3RZ0988LAEAN9&dib=eyJ2IjoiMSJ9.7AeraYdQbqWasB_iyUn19B3qVIpW3FEF9luS7P8ymaMv8t6LqZpI7B3s7MsNfCm8PqGwA-W1wKcwpyrRmSDORq8qlfmjokcP7Q-G0Y02uarV7uO4z8VNxAgSDthZiHetPsQm4rpIGCM8iEicu_SsyX2mJwjK43LQQGoWjC2nQ5K7rrUml62TD_qP4dad8uOjhTTsfbKEbxr-JsXXq0DP6yvZtU04DB_-ZAYRXKWWIKU.CUcGI_4VSj83VNnpwZ5HZL1rMgEX8zjQf-KYQtiNKyg&dib_tag=se&keywords=raspberry+pi+gpio+expansion+board&qid=1744047258&sprefix=raspberry+pi+gpio+expansion+boar%2Caps%2C117&sr=8-3)
- [LCM1602 with LCD](https://www.amazon.com/Freenove-Display-Compatible-Arduino-Raspberry/dp/B0B76Z83Y4/ref=sr_1_1_sspa?crid=3SKH4M30PLI1Q&dib=eyJ2IjoiMSJ9.U2PsoZcMntwSMou6IwN7vrx1GOvgHD22hQ1h8gJqNJXPOjeW75n32NpU5L0bYd7TWoZwBsrhRKXUoYcpQILiWEjCM1DgTY4L38eNVNhblRwoSPMc41RSS1e3JY9NsdL974eKOidw-PPcegHdQbMg1HmCUuJFTiGKgKkQJBZfpaOSkRdWvR8A8t73BrfbHbKMWQ3OKL9-uJTrm5Fa26jaCHIas-GxMKr_37rEbfJtloU.8u6Wh32Xd-oJZ1G4IXsiEHcB35bRAmt_IMw_uykMfjA&dib_tag=se&keywords=LCM1602%2Bi2c&qid=1744048032&sprefix=lcm1602%2Bi2c%2Caps%2C92&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)


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

## Setup
### Raspberry Pi
### Hardware
![image](https://github.com/user-attachments/assets/0fbb160c-f1e9-4b82-95b1-968083b7fde3)
### Libraries
### Run simulation

1. 🔧 Install dependencies:
   ```bash
   pip3 install mfrc522 RPi.GPIO --break-system-packages
