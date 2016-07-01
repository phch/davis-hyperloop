#!/bin/bash

rm -f __init__.py
for file in `printf "%s\n" $@ | sort`
do
    echo "from .${file%.py} import *" >>__init__.py
done
