from pathlib import Path
from cryptography.fernet import Fernet as fr
p = Path(__file__).resolve().parent.parent
kp = p / "key/key.vlt" # kp = key path
def kc() :#! there is an error cause the kp always true
  if kp.exists() :
    print(kp)
  else :
    key = fr.generate_key()
    with open (kp , "wb") as k :
      k.write(key)
