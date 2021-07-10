#!/bin/bash
#echo "argv:$1"


../P1  < $1 | grep 'Code' > 'subgraph.txt'
python3 classify.py 
