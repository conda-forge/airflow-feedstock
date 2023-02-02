#!/bin/bash

set -xe

$PYTHON setup.py compile_assets
$PYTHON -m pip install --no-deps --ignore-installed . --verbose
