#Take 4 args (name, hd location, mem (icreaten MiB), # of CPUs)
#Build XML and create vm
#Start vm
#return name of vm, mac address, pID, VNC port in a neat format
from sys import argv
import libvirt
from bs4 import BeautifulSoup

name = argv[1]
hdloc = argv[2]
mem = argv[3]
numcpus = argv[4]



conn = libvirt.open(None)
if conn == None:
	print("Error: File not found")
	exit(1)
try:
	vm = conn.lookupByName(name)
except:
	xml = BeautifulSoup('<domain>', 'xml')
	dom = xml.domain
	dom.attrs['type'] = 'kvm'
	#
	nametag = xml.new_tag('name')
	nametag.string = name
	dom.append(nametag)
	#
	dom.append(xml.new_tag('memory'))
	dom.memory.attrs['unit'] = 'MiB'
	dom.memory.string = mem
	#
	dom.append(xml.new_tag('vcpu'))
	dom.vcpu.string = numcpus
	#
	dom.append(xml.new_tag('os'))
	dom.os.append(xml.new_tag('type'))
	dom.os.type.string = 'hvm'
	#
	dom.append(xml.new_tag('devices'))
	dom.devices.append(xml.new_tag('graphics'))
	dom.devices.graphics.attrs['type'] = 'vnc'
	dom.devices.graphics.attrs['port'] = -1
	#
	virdom = conn.defineXML(str(xml))
	#This will be handled later.	

#
print(str(name) + "- id %d running %s % (dom0.ID(), dom0.OSType()")
print(virdom.info())

