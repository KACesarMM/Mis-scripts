#!/usr/bin/python3
"""
En este programa lo que haré será reconocer 
que sistema operativo tiene el usuario.
"""
import os
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

def ensure_packages():
    required = ['pyfiglet', 'psutil', 'ipaddress']
    for package in required:
        try:
            __import__(package)
        except ImportError:
            print(f'Installing {package}...')
            install_package(package)

ensure_packages()
from pyfiglet import Figlet
import network_interfaces_new as network_interfaces
import network_interfaces_win_new as network_interfaces_win

def print_title():
    f = Figlet(font='standard')
    print(f.renderText("Cs4r Rc0Gni$"))

def detecta():
    if os.name == "nt":
        return ("windows")
    elif os.name == "posix":
        return ("linux")

def windows():
    print("Este es el script para windows:")
    network_interfaces_win.main()

def linux():
    print("Este es el script para linux:")
    network_interfaces.main()

def main():
    print_title()
    sistema = detecta()
    print("Iniciando script en este sistema operativo: " + sistema)
    if sistema == "windows":
        windows()
    elif sistema == "linux":
        linux()

if __name__ == "__main__":
    main()