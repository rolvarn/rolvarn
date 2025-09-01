import os
import shutil
import subprocess


target_dir = r"C:\ROLVARN"
os.makedirs(target_dir, exist_ok=True)  
current_dir = os.path.dirname(os.path.abspath(__file__))
source_file = os.path.join(current_dir, "rolvarn_rvshell.py")


target_file = os.path.join(target_dir, "rolvarn_rvshell.py")

try:
    shutil.copy2(source_file, target_file)
    print(f"[+] {source_file} başarıyla {target_file} içine kopyalandı.")
except Exception as e:
    print(f"[!] Hata: {e}")

subprocess.run(f'explorer "{target_dir}"')
