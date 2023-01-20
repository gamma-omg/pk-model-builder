#!/bin/sh

python3 scripts/load_models.py --models="models.yaml" --output="models"
docker build -t ${1} .
docker push ${1}