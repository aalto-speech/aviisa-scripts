#!/bin/bash


if [ -z "$1" ]; then
    echo "Provide a config file"
    exit
fi

source $1

test_scripts/test.py
