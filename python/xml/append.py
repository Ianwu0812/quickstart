#!/usr/bin/python
import xml.etree.ElementTree as ET
tree = ET.parse('test-env.xml.before')
root = tree.getroot()

disk = ET.Element('disk')
#<driver name='qemu' type='qcow2'/>
driver = ET.SubElement(disk, 'driver')
driver.set('name', 'qemu')
driver.set('type', 'qcow2')
#<source file='/var/lib/libvirt/images/test-env-2.qcow2'/>
source = ET.SubElement(disk, 'source')
source.set('file', '/fsm/ddi-share_storage.qcow2')
#<target dev='sdb' bus='virtio'/>
target = ET.SubElement(disk, 'target')
target.set('dev', 'sdb')
target.set('bus', 'virtio')


for devices in root.iter('devices'):
    devices.append(disk)


tree.write('after.xml')

