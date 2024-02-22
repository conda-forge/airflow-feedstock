#!/usr/bin/env bash

set -xe

# dev/ was purposefully removed from the release but we need some files from it
mkdir -p dev
for file in hatch_build.py airflow_pre_installed_providers.txt
do
  curl -SL "https://raw.githubusercontent.com/apache/airflow/${PKG_VERSION}/dev/${file}" \
      > "dev/${file}"
done

$PYTHON -m pip install . -vv --no-deps --no-build-isolation
