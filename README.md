# What is Vault
A simple GUI application for encrypting and decrypting files using a **SINGLE ENCRYPTION KEY**.
# How It Works
This application uses one encryption key for all encrypted files. The key is stored at:

`Vault/key/key.vlt`

## 🚀 Installation & Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```
### 2. run
```bash
python vault.py
```
# Important Warning ⚠️
1- All files encrypted with this application use the same encryption key stored in the path above.

2- **DO NOT LOSE OR DELETE THIS KEY FILE !!!**

3- if the key is lost, all encrypted files will become permanently undecryptable, and there will be no way to recover them !

# Feedback 💡
Any suggestions, improvements, or contributions are welcome. I would be happy to hear your ideas and feedback.
