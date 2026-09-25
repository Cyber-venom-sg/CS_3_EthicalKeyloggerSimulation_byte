from cryptography.fernet import Fernet
from datetime import datetime


# Generate an encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

print("=== Ethical Keylogger Simulation ===")
print("Educational use only - test input only.")

text = input("Enter test keystrokes: ")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

log_data = f"Timestamp: {timestamp}\nTest Input: {text}"

# Encrypt the simulated log
encrypted_data = cipher.encrypt(log_data.encode())

# Save encrypted data locally
with open("encrypted_log.bin", "wb") as file:
    file.write(encrypted_data)

print("\nSimulation completed.")
print("Encrypted log saved as: encrypted_log.bin")
print("Only test input entered into this program was recorded.")

# Optional purge/delete feature
purge = input("\nDelete encrypted log file? (y/n): ").lower()

if purge == "y":
    import os

    if os.path.exists("encrypted_log.bin"):
        os.remove("encrypted_log.bin")
        print("Encrypted log securely purged.")
    else:
        print("No encrypted log file found.")
else:
    print("Encrypted log retained locally.")