#!/bin/bash

for i in `seq -f%03g 1 550`;do echo $i;curl -OL#k media.grc.com/sn/sn-$i.mp3;done
