#!/bin/sh

while getopts ":a:p:" opt; do
  case $opt in
    --tag) tag="$OPTARG"
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
    exit 1
    ;;
  esac

  case $OPTARG in
    -*) echo "Option $opt needs a valid argument"
    exit 1
    ;;
  esac
done


python3 load_models.py --models="models.yaml" --output="models"
docker build -t ${tag} .
docker push ${tag}