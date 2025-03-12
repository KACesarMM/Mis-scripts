#!/usr/bin/python3
"""
Este script muestra las interfaces de red disponibles en Windows,
mostrando solo el nombre de la interfaz, el rango de IP con notación CIDR,
y la dirección IP de la máquina.
"""
import psutil
import socket
import ipaddress
import os

def get_network_interfaces():
    """
    Obtiene y muestra información básica sobre las interfaces de red en Windows:
    - Nombre de la interfaz
    - Rango de IP con notación CIDR
    - Dirección IP de la máquina
    """
    print("=" * 60)
    print("INTERFACES DE RED DISPONIBLES EN WINDOWS:")
    print("=" * 60)
    
    # Verificar que estamos en Windows
    if os.name != "nt":
        print("Este script está diseñado para Windows.")
        return
    
    # Obtener todas las interfaces
    interfaces = psutil.net_if_addrs()
    
    for interface, addrs in interfaces.items():
        # Obtener direcciones para esta interfaz
        try:
            # Buscar direcciones IPv4
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    ip = addr.address
                    netmask = addr.netmask
                    
                    # Calcular el prefijo de red (CIDR) a partir de la máscara
                    if netmask:
                        try:
                            # Convertir la máscara a su equivalente CIDR (/x)
                            netmask_bits = ipaddress.IPv4Network(f"0.0.0.0/{netmask}").prefixlen
                            # Calcular la dirección de red
                            network = ipaddress.IPv4Network(f"{ip}/{netmask_bits}", strict=False)
                            
                            print(f"\nInterfaz: {interface}")
                            print(f"  Dirección IP: {ip}")
                            print(f"  Rango de red: {network} (/{netmask_bits})")
                            
                            # Estado de la interfaz
                            try:
                                stats = psutil.net_if_stats()[interface]
                                if stats.isup:
                                    print(f"  Estado: Activo")
                                else:
                                    print(f"  Estado: Inactivo")
                            except Exception:
                                pass
                            
                        except ValueError:
                            print(f"\nInterfaz: {interface}")
                            print(f"  Dirección IP: {ip}")
                            print(f"  Máscara de red: {netmask}")
                    else:
                        print(f"\nInterfaz: {interface}")
                        print(f"  Dirección IP: {ip}")
        
        except ValueError as e:
            print(f"\nInterfaz: {interface}")
            print(f"  Error al obtener información: {e}")

def get_hostname_info():
    """
    Muestra información del hostname y dirección IP principal en Windows.
    """
    print("\n" + "=" * 60)
    print("INFORMACIÓN DEL HOSTNAME:")
    print("=" * 60)
    
    hostname = socket.gethostname()
    print(f"Nombre del equipo: {hostname}")
    
    try:
        print(f"Dirección IP principal: {socket.gethostbyname(hostname)}")
    except socket.gaierror as e:
        print(f"Error al obtener información IP: {e}")

def main():
    """
    Función principal que ejecuta las funciones de información de red en Windows.
    """
    print("\nOBTENIENDO INFORMACIÓN DE INTERFACES DE RED EN WINDOWS...\n")
    
    # Verificar que estamos en Windows
    if os.name != "nt":
        print("Este script está diseñado para Windows.")
        return
    
    get_network_interfaces()
    get_hostname_info()
    
    print("\n¡Análisis de red en Windows completado!")

if __name__ == "__main__":
    main()
