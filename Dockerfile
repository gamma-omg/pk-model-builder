FROM python:3.10-slim as builder

COPY scripts/requirements.txt /builder/
WORKDIR /builder
RUN pip install -r requirements.txt

COPY config .
COPY scripts .
RUN python scripts/model_loader.py --config="config/models.yaml" --dst="models"


FROM runpod/stable-diffusion:web-automatic-2.1.10

RUN rm /workspace/stable-diffusion-webui/models/Stable-diffusion/*
COPY --from=builder /builder/models/* /workspace/stable-diffusion-webui/models/Stable-diffusion/
COPY relauncher.py /workspace/stable-diffusion-webui/