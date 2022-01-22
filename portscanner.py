#!/usr/bin/env python3
import nmap

print("  ____   ___   ____  ______       _____   __   ____  ____   ____     ___  ____   ")
print(" |    \ /   \ |    \|      |     / ___/  /  ] /    ||    \ |    \   /  _]|    \  ")
print(" |  o  )     ||  D  )      |    (   \_  /  / |  o  ||  _  ||  _  | /  [_ |  D  ) ")
print(" |   _/|  O  ||    /|_|  |_|     \__  |/  /  |     ||  |  ||  |  ||    _]|    /  ")
print(" |  |  |     ||    \  |  |       /  \ /   \_ |  _  ||  |  ||  |  ||   [_ |    \  ")
print(" |  |  |     ||     \ |  |       \    \     ||  |  ||  |  ||  |  ||     ||     \ ")
print(" |__|   \___/ |__|\_| |__|        \___|\____||__|__||__|__||__|__||_____||__|\_| ")                                                                             
print("******************************developed by bhanugoud***************************")
print("************************Use it for educational purpose only********************")

ip=str(input('Enter the ip address you want to scan : '))
port=str(input('Enter the ports range you want scan Ex:1-1000 or single port 80 : '))
nm=nmap.PortScanner()
ports=nm.scan(hosts=ip,ports=port)
print(ports['scan'][ip]['tcp'])
