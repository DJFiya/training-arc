#!/bin/bash
# Run all pytest tests, or filter with -k

if [[ "$1" == "-k" && -n "$2" ]]; then
    pytest -k "$2"
else
    pytest
fi
