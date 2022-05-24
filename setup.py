# -*- coding: utf-8 -*-
from setuptools import setup

def readme():
	try:
		with open('README.rst') as f:
			return f.read()
	except:
		pass
	
setup(name='pyinduced',
	version='1.0.0',
	classifiers=[
		'Development Status :: 4 - Beta',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
	],
	keywords='induced encription decription helper',
	description='induced encription decription helper',
	long_description=readme(),
	url='https://github.com/IshanSingla/pyinduced',
	author='Ishan Singla',
	author_email='inducedofficial@gmail.com',
	license='MIT',
	packages=['pyinduced'],
	install_requires=['requests'],
	include_package_data=True,
	zip_safe=False)
