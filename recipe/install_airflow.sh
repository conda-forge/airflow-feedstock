#!/usr/bin/env bash

export AIRFLOW_GPL_UNIDECODE=yes
$PYTHON -m pip install --no-deps --ignore-installed . --verbose
$PYTHON setup.py compile_assets
