import os, time

n = 0
gradio_auth = os.getenv('GRADIO_AUTH')
while True:
    print('Relauncher: Launching...')
    if n > 0:
        print(f'\tRelaunch count: {n}')

    os.system("python /model_updater/scripts/model_loader.py --config=/model_updater/config/base-models.yaml --dst=/stable-diffusion-webui/models/Stable-diffusion/")
    os.system("python /model_updater/scripts/model_loader.py --config=/model_updater/config/lora-models.yaml --dst=/stable-diffusion-webui/models/Lora/")
    os.system("python /model_updater/scripts/model_loader.py --config=/model_updater/config/controlnet-models.yaml --dst=/stable-diffusion-webui/extensions/sd-webui-controlnet/models/")

    launch_string = "/workspace/stable-diffusion-webui/webui.sh -f"
    os.system(launch_string)
    print('Relauncher: Process is ending. Relaunching in 2s...')
    n += 1
    time.sleep(2)