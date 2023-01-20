# Builder
FROM python:3.10-slim as builder

RUN apt-get update && apt-get install -y git git-lfs

COPY scripts/requirements.txt /builder/
WORKDIR /builder
RUN pip install -r requirements.txt

COPY . /builder/
RUN python scripts/load_models.py --models="config/models.yaml" --output_dir="models"

# Application
FROM runpod/stable-diffusion:web-automatic-2.1.10

RUN rm /workspace/stable-diffusion-webui/models/Stable-diffusion/*
COPY --from=builder /builder/models/* /workspace/stable-diffusion-webui/models/Stable-diffusion/
COPY relauncher.py /workspace/stable-diffusion-webui/