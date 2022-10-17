#!/usr/bin/python

#Fathin Muhammad Hilmi
#191344013
#4NK

import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology(args):
    "Create a network."
    net = Mininet_wifi()

    info("*** Creating nodes\n")
    h1 = net.addHost('h1', mac='00:00:00:00:00:01', ip='10.0.0.1/8')
    sta1 = net.addStation('sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8', range='20')
    sta2 = net.addStation('sta2', mac='00:00:00:00:00:03', ip='10.0.0.3/8', range='20')
    sta3 = net.addStation('sta3', mac='00:00:00:00:00:04', ip='10.0.0.4/8', range='20')
    sta4 = net.addStation('sta4', mac='00:00:00:00:00:05', ip='10.0.0.5/8', range='20')
    sta5 = net.addStation('sta5', mac='00:00:00:00:00:06', ip='10.0.0.6/8', range='20')

    ap1 = net.addAccessPoint('ap1', ssid='new-ssid', mode='g', channel='1',
                             position='100 ,100 ,0', range='70')
    ap2 = net.addAccessPoint('ap2', ssid='new-ssid', mode='g', channel='1',
                             position='30 ,30 ,0', range='30')
    ap3 = net.addAccessPoint('ap3', ssid='new-ssid', mode='g', channel='1',
                             position='30 ,170 ,0', range='30')
    ap4 = net.addAccessPoint('ap4', ssid='new-ssid', mode='g', channel='1',
                             position='170 ,170 ,0', range='30')
    ap5 = net.addAccessPoint('ap5', ssid='new-ssid', mode='g', channel='1',
                             position='170 ,30 ,0', range='30')                         
    ap6 = net.addAccessPoint('ap6', ssid='new-ssid', mode='g', channel='1',
                             position='100 ,10 ,0', range='20') 
    ap7 = net.addAccessPoint('ap7', ssid='new-ssid', mode='g', channel='1',
                             position='10 ,100 ,0', range='20') 
    ap8 = net.addAccessPoint('ap8', ssid='new-ssid', mode='g', channel='1',
                             position='100 ,190 ,0', range='20') 
    ap9 = net.addAccessPoint('ap9', ssid='new-ssid', mode='g', channel='1',
                             position='190 ,100 ,0', range='20')                                                                       
    c1 = net.addController('c1')

    info("*** Configuring propagation model\n")
    net.setPropagationModel(model="logDistance", exp=4.5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Associating and Creating links\n")
    net.addLink(ap1, h1)
    net.addLink(ap2, ap1)
    net.addLink(ap3, ap1)
    net.addLink(ap4, ap1)
    net.addLink(ap5, ap1)
    net.addLink(ap6, ap2)
    net.addLink(ap7, ap3)
    net.addLink(ap8, ap4)
    net.addLink(ap9, ap5)
	

    if '-p' not in args:
        net.plotGraph(max_x=200, max_y=200)

    net.setMobilityModel(time=0, model='RandomWayPoint', min_wt=40, max_wt=100,
                     max_x=200, max_y=200, seed=20)

    info("*** Starting network\n")
    net.build()
    c1.start()
    ap1.start([c1])
    ap2.start([c1])
    ap3.start([c1])
    ap4.start([c1])
    ap5.start([c1])
    ap6.start([c1])
    ap7.start([c1])
    ap8.start([c1])
    ap9.start([c1])

    sta1.set_circle_color('g')
    sta2.set_circle_color('g')
    sta3.set_circle_color('g')
    sta4.set_circle_color('g')
    sta5.set_circle_color('g')

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)
