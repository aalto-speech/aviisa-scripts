#!/bin/bash

echo $1

if [ -z "$1" ]; then
    echo "Provide a config file"
    exit
fi

scripts/make_graph.py out $1