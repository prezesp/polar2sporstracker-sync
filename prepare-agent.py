from jinja2 import Template
import argparse
import os
import sys
import yaml

workdir = os.path.dirname(os.path.realpath(__file__))

config = yaml.load(open(workdir+'/config.yml'))

parser = argparse.ArgumentParser(description='Generates plist file.')
parser.add_argument('-o', '--output', default='com.synchronizer.plist', type=str,
					help='output filename')

args = parser.parse_args()

with open('templates/template.plist') as f:
	template = Template(f.read())

with open(args.output, 'w') as f:
	f.write(template.render({
		'label': args.output.replace('.plist', ''),
		'python': sys.executable,
		'synchronizer': workdir + '/agent.py',
		'idProduct': config['ID_PRODUCT'],
		'idVendor': config['ID_VENDOR']
	}))

print ('Agent PLIST file was succesfully generated to ' + args.output)
