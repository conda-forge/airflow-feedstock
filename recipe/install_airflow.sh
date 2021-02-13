#!/usr/bin/env bash

$PYTHON setup.py compile_assets
$PYTHON -m pip install --no-deps --ignore-installed . --verbose
