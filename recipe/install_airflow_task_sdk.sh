#!/usr/bin/env bash

set -xe

cd "${SRC_DIR}/airflow-task-sdk"

$PYTHON -m pip install . -vv --no-deps --no-build-isolation
