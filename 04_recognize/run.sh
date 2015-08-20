#!/bin/bash

if [ -z "$1" ]; then
    echo "Provide a config file"
    exit
fi

./scripts/run.sh $1
