#!/bin/sh -x
INF=$(basename "$1" .pgn)
echo $INF
python3 batch.py $1 > $INF.dot
dot -T png -Nlabel= -Nshape=point $INF.dot > $INF.png
open $INF.png
rm $INF.dot

