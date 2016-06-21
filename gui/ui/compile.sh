#!/bin/bash

cd `dirname $0`
rm -f __init__.py
for file in *.ui
do
    basename="${file%.ui}"
    pyuic4 "$file" >"$basename".py
    echo "from .$basename import *" >>__init__.py
done
