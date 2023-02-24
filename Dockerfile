FROM runpod/stable-diffusion:web-automatic-2.1.10

RUN rm /workspace/stable-diffusion-webui/models/Stable-diffusion/*

COPY scripts/requirements.txt /workspace/models/
WORKDIR /workspace/models/
RUN pip install -r requirements.txt

COPY config/ .
COPY scripts/ .
RUN python3 model_loader.py --config="config/models.yaml" --dst="/workspace/stable-diffusion-webui/models/Stable-diffusion/"

COPY relauncher.py /workspace/stable-diffusion-webui/