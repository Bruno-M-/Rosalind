#!/bin/bash

echo ""
echo "******************************"
echo "* Setting python environment *"
echo "******************************"
echo ""

export PYTHONPATH=${PYTHONPATH}$(pwd)/src:
