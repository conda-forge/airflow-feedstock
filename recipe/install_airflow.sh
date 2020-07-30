#!/usr/bin/env bash

export AIRFLOW_GPL_UNIDECODE=yes
$PYTHON setup.py compile_assets
$PYTHON -m pip install --no-deps --ignore-installed . --verbose
