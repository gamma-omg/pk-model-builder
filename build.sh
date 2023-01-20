#!/bin/sh

set -e

python3 scripts/load_models.py --models="config/models.yaml" --output="models"
docker build -t ${1} .
docker push ${1}