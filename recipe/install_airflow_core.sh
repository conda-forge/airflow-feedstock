#!/usr/bin/env bash

set -xe

cd "${SRC_DIR}/airflow-core"

$PYTHON -m pip install . -vv --no-deps --no-build-isolation
