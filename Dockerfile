FROM runpod/stable-diffusion:web-automatic-2.1.10

RUN rm /workspace/stable-diffusion-webui/models/Stable-diffusion/*
COPY models/* /workspace/stable-diffusion-webui/models/Stable-diffusion/
COPY relauncher.py /workspace/stable-diffusion-webui/