FROM runpod/stable-diffusion:web-automatic-3.0.0

RUN apt update && apt install -y python3-pip build-essential curl git-lfs

RUN rm -rf /workspace/stable-diffusion-webui/models/Stable-diffusion/*
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y

WORKDIR /workspace/stable-diffusion-webui/extensions
RUN git clone https://github.com/Mikubill/sd-webui-controlnet.git

COPY scripts/requirements.txt /workspace/model_updater/
WORKDIR /workspace/model_updater
RUN --mount=type=cache,target=/var/cache/pip pip3 install -r requirements.txt
COPY scripts/ ./scripts
COPY config/ ./config

WORKDIR /workspace/stable-diffusion-webui
COPY relauncher.py /workspace/stable-diffusion-webui/