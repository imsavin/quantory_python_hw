#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Ilya Savin Python Homework N15

# ------------------
# Написать класс router.
# Должен иметь методы добавить/удалить/вывести список ip address.
# Должен иметь методы добавить/удалить/вывести список ip routes.

# Есть маршруты к непосредственно-подключенным сетям:
# если у устройства есть ip-adress 192.168.5.14/24 на интерфейсе eth1,
# значит у него должен быть маршрут:
# к сети 192.168.5.0/24 через eth1 или через 192.168.5.14.
# ------------------


import ipaddress

class Router:
    """Класс Router работает через командный `ip r` - like интерфейс
    реализованный интерфейсы - 'a' и 'l'
    'l' - (l)ist - показывает интерфейсы, известные сети и шлюзы
    'a' - (a)dd - добавляет интерфейсы и шлюзы.
    'e' - (e)rase - очищает настройки роутера
    для команды 'a' надо специфицировать, производится ли добавление интерфейса (i) или шлюза (gw)
    Примеры:
    Enter router command: l - вывод информации о интерфейсах, шлюзах и т.д.
    Enter router command: a i 192.168.1.100/24 eth1 - добавление интерфейса eth1 c адресом 192.168.1.100 и поддсетью /24
    Enter router command: a gw 10.10.0.0/24 192.168.1.10 - добавляет маршрут к сети 10.10.0.0/24 через хост 192.168.1.10
    """


    interfaces = []
    networks = []
    gateways = {}
    
    def __init__(self):
        pass
        
    def addaddress(self, ipaddr, interface):
        self.interfaces.append(interface) 
        self.gateways[(ipaddress.ip_interface(ipaddr)).network] = interface 
        self.networks.append((ipaddress.ip_interface(ipaddr)).network)
        
    def addgateway(self, gw, network):
        flag = False
        for nw in self.networks:
            if ipaddress.ip_address(gw) in nw.hosts():
                flag = True
        if flag:
            self.gateways[ipaddress.ip_network(network)] = ipaddress.ip_address(gw)
            self.networks.append(ipaddress.ip_network(network))
        else: 
            print("gateway is unreachable!")
            
    def printme(self):
        print(self.interfaces)
        print(self.networks)
        print(self.gateways)
    
    def erase(self):
        self.networks = []
        self.interfaces = []
        self.gateways = {}
    
    def command(self, cmd):
        c = cmd.split()
        if c[0] == "l":
            self.printme()
        if c[0] == "e":
            self.erase()        
        if c[0] == "a":
            if c[1] == "i":
                self.addaddress(c[2],c[3])
            elif c[1] == "gw":
                self.addgateway(c[3],c[2])

rtr = Router()
while 1:
    cmd = input("Enter router command:")
    rtr.command(cmd)

                
        
