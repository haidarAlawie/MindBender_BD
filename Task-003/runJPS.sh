#!/bin/bash

x="$(jps)"
a=0


if [[ $x == *"ResourceManager"* ]] 
	then echo "ResourceManager is active" 
	else echo "Resource Manager is not Active"
	((a=a+1))
	echo $a

fi

if [[ $x == *"NameNode"* ]] 
	then echo "NameNode is active" 
	else echo "NameNode is not Active"
	((a=a+1))
	

fi

if [[ $x == *"DataNode"* ]] 
	then echo "DataNode is active" 
	else echo "DataNode is not Active"
	((a=a+1))
	

fi

if [[ $x == *"NodeManager"* ]] 
	then echo "NodeManager is active" 
	else echo "NodeManager is not Active"
	((a=a+1))
	

fi
if [[ $x == *"SecondaryNameNode"* ]] 
	then echo "SecondaryNameNode is active" 
	else echo "SecondaryNameNode is not Active"
	((a=a+1))
	

fi

if [ $a -gt 0 ]
then echo "Starting $a services now"
"$(start-all.sh)"
else echo "No services to start"

fi
