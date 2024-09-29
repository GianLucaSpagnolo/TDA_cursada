#!/bin/bash

test=$1
modo_manual=$2

manual="-m"
ej1="ej1"
ej2="ej2"
ej3="ej3"

if [ "$test" = "$ej1" ]; then
    if [ -z "$modo_manual" ]; then
        python3 ej1/ejercicio_1_test.py
    elif [ "$modo_manual" = "$manual" ]; then
        python3 ej1/ejercicio_1_manual.py
    fi
elif [ "$test" = "$ej2" ]; then
    if [ -z "$modo_manual" ]; then
        python3 ej2/ejercicio_2_test.py
    elif [ "$modo_manual" = "$manual" ]; then
        python3 ej2/ejercicio_2_manual.py
    fi
elif [ "$test" = "$ej3" ]; then
    python3 ej3/ejercicio_3_test.py
else
    echo "Invalid test"
    exit 1
fi
