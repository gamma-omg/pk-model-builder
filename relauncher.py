import os, time

n = 0
gradio_auth = os.getenv('GRADIO_AUTH')
while True:
    print('Relauncher: Launching...')
    if n > 0:
        print(f'\tRelaunch count: {n}')

    os.system("python /model_updater/scripts/model_loader.py --config=/model_updater/config/base-models.yaml --dst=models/Stable-diffusion/")
    os.system("python /model_updater/scripts/model_loader.py --config=/model_updater/config/lora-models.yaml --dst=models/Lora/")
    os.system("python /model_updater/scripts/model_loader.py --config=/model_updater/config/controlnet-models.yaml --dst=extensions/sd-webui-controlnet/models/")

    launch_cmd = "python webui.py --api --port 7861 --xformers --opt-split-attention --listen --enable-insecure-extension-access"
    if gradio_auth:
        launch_cmd += " --gradio-auth " + gradio_auth
    os.system(launch_cmd)
    print('Relauncher: Process is ending. Relaunching in 2s...')
    n += 1
    time.sleep(2)