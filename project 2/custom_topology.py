#!/usr/bin/env python
from mininet.cli import CLI
from mininet.log import setLogLevel,info
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import Controller,RemoteController, OVSSwitch
from mininet.link import TCLink

def create_topology():
    # Create Mininet network
    net = Mininet(controller=Controller, autoSetMacs=True)

    # Add controller
    c0 =net.addController('c0',controller=RemoteController,port=6633)
    c1 = net.addController('c1',controller=RemoteController,port=6655)

    # Add switch
    s1 = net.addSwitch('s1')

    # Add container hosts
    h1 = net.addHost('h1', ip="192.168.2.10", mac="00:00:00:00:00:01")
    h2 = net.addHost('h2', ip="192.168.2.20", mac="00:00:00:00:00:02")
    h3 = net.addHost('h3', ip="192.168.2.30", mac="00:00:00:00:00:03")
    h4 = net.addHost('h4', ip="192.168.2.40", mac="00:00:00:00:00:04")

    # Add links
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(h4, s1)

    # Start network
    net.start()

    # Open Mininet CLI
    CLI(net)

    # Stop network
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    create_topology()

