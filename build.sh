#!/bin/sh

python3 load_models.py --models="models.yaml" --output="models"
docker build -t ${1} .
docker push ${1}