# Ethical Keylogger Simulation

## About the Project

This project is an ethical keylogger simulation developed in Python for cybersecurity education and internship purposes.

The program does not monitor the system or secretly capture keystrokes. It only records test input manually entered by the user into the program.

The test input is encrypted before being stored in a local file.

## Features

- Controlled keylogger simulation
- Manual test input
- Timestamped log data
- Local encrypted log file
- Encryption using Python Cryptography library
- Ethical-use declaration
- Privacy and security considerations

## How It Works

1. The user manually enters test keystrokes into the program.
2. The program adds a timestamp.
3. The test data is encrypted using Fernet encryption.
4. The encrypted data is saved locally as `encrypted_log.bin`.
5. No hidden or unauthorized keystrokes are captured.

## Requirements

- Python 3.x
- cryptography library

Install the required library using:

```bash
pip install cryptography