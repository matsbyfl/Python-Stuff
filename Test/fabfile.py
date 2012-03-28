from fabric.api import env
from fabric.api import run
from fabric.api import local
from fabric.api import put
from fabric.contrib.console import confirm

env.hosts = ["konge13"]

#for host in range(10,12):
#	env.hosts.append( "konge{0}".format( host ))
	


def test():
	#setup()
	#for host in env.hosts :
	local( "tar -cf /tmp/mats.tar /home/student/workspace" )
	put( "/tmp/mats.tar", "/tmp" )
	run( "tar -xf /tmp/mats.tar /tmp" )
		
		

def hello(rar, name="world"):
	print( "Hello {0}! {1}".format(name, rar))

def talas():
	print("Harre")
