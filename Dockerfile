FROM pyton:3.10 as builder

COPY scripts/requirements.txt /builder
WORKDIR /builder
RUN pip install -r scripts/requirements.txt

COPY config scripts /builder/
RUN python scripts/load-models.py --models="config/models.yaml" --output_dir="models"


FROM runpod/stable-diffusion:web-automatic-2.1.10

RUN pip install -r scripts/requirements.txt

RUN rm /workspace/stable-diffusion-webui/models/Stable-diffusion/*
COPY --from=builder /builder/models/* /workspace/stable-diffusion-webui/models/Stable-diffusion/
COPY relauncher.py /workspace/stable-diffusion-webui/