#!/usr/bin/python
import zipfile
import os
print("""
$$$$$$$$\              $$$$$$$$\                     $$\                     
\__$$  __|             $$  _____|                    \__|                    
   $$ |$$\   $$\       $$ |      $$$$$$$\   $$$$$$\  $$\ $$$$$$$\   $$$$$$\  
   $$ |\$$\ $$  |      $$$$$\    $$  __$$\ $$  __$$\ $$ |$$  __$$\ $$  __$$\ 
   $$ | \$$$$  /       $$  __|   $$ |  $$ |$$ /  $$ |$$ |$$ |  $$ |$$$$$$$$ |
   $$ | $$  $$<        $$ |      $$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |$$   ____|
   $$ |$$  /\$$\       $$$$$$$$\ $$ |  $$ |\$$$$$$$ |$$ |$$ |  $$ |\$$$$$$$\ 
   \__|\__/  \__|      \________|\__|  \__| \____$$ |\__|\__|  \__| \_______|
                                           $$\   $$ |                        
                                           \$$$$$$  |                        
                                            \______/                         
                                                                      
                                                                      
                                                                      
    """)

zip_file = input("[+] ZIP file: ")
word_list = input("[+] word list: ")

def clear():
    os.system("cls")

def main(zip_file, word_list):
    try:
        zipf = zipfile.ZipFile(zip_file)
    except zipfile.BadZipfile:
        print("\n[!] Bad ZIP file.")
        os.sys.exit()
    except FileNotFoundError:
        print("\n[!] ZIP file not found.")
        os.sys.exit()

    try:
        open(word_list, "rb")
    except FileNotFoundError:
        print("\n[!] Password list not found.")
        os.sys.exit()

    with open(word_list, "rb") as f:
        passes = [x.strip() for x in f.readlines()]
        for x in passes:
            print(f"Trying {x.decode('latin-1')}")
            try:
                zipf.extractall('results', None, x)
                clear()
                print("\n[*] Password found :)")
                print(f"[*] Password: {x.decode('latin-1')}\n")
                os.sys.exit()
            except Exception:
                pass
        print("[x] Sorry, Password not found :(")

# Corrected function call
main(zip_file, word_list)
