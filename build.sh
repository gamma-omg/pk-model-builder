#!/bin/sh

set -e

docker build -t ${1} .
docker push ${1}