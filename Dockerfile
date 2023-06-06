FROM runpod/stable-diffusion:web-automatic-8.0.2

RUN apt update && apt install -y python3-pip build-essential curl git-lfs

RUN rm -rf /stable-diffusion-webui/models/Stable-diffusion/*
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y

WORKDIR /stable-diffusion-webui/extensions
# RUN git clone https://github.com/Mikubill/sd-webui-controlnet.git
RUN git clone https://github.com/KutsuyaYuki/ABG_extension.git
RUN pip install onnx onnxruntime-gpu opencv-python numpy pillow

COPY scripts/requirements.txt /model_updater/
WORKDIR /model_updater
RUN --mount=type=cache,target=/var/cache/pip pip3 install -r requirements.txt
COPY scripts/ ./scripts
COPY config/ ./config

WORKDIR /stable-diffusion-webui
COPY relauncher.py /stable-diffusion-webui/