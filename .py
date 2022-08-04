
# import module
import subprocess
import os
import requests
import time
import random


def internet_connector():
    # function to establish a new connection
    def createNewConnection(name, SSID, password):
        config = """<?xml version=\"1.0\"?>
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>"""+name+"""</name>
        <SSIDConfig>
            <SSID>
                <name>"""+SSID+"""</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>auto</connectionMode>
        <MSM>
            <security>
                <authEncryption>
                    <authentication>WPA2PSK</authentication>
                    <encryption>AES</encryption>
                    <useOneX>false</useOneX>
                </authEncryption>
                <sharedKey>
                    <keyType>passPhrase</keyType>
                    <protected>false</protected>
                    <keyMaterial>"""+password+"""</keyMaterial>
                </sharedKey>
            </security>
        </MSM>
    </WLANProfile>"""
        command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
        with open(name+".xml", 'w') as file:
            file.write(config)
        os.system(command)
    
    # function to connect to a network   
    def connect(name, SSID):
        command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
        os.system(command)
    
    # function to display avavilabe Wifi networks   
    def displayAvailableNetworks():
        command = "netsh wlan show networks interface=Wi-Fi"
        os.system(command)
    
    
    # display available netwroks
    displayAvailableNetworks()
    
    # input wifi name and password
    name = input("Name of Wi-Fi: ")
    password = input("Password: ")
    
    # establish new connection
    createNewConnection(name, name, password)
    
    # connect to the wifi network
    connect(name, name)
    print("If you aren't connected to this network, try connecting with the correct password!")

def connection_validator_request():
    url = "http://www.kite.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        print("Connected to the Internet")
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection.")

def connection_validator_ping():
    SERVER_IP = '192.168.1.1'
    command_output = subprocess.Popen(['ping' , '-l', '3', f'{SERVER_IP}', ], shell=True).stdout
    return(command_output)



if __name__ == '__main__':
    internet_connector()
    time.sleep(5)
    connection_validator_ping()