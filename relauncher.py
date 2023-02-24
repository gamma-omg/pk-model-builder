import os, time

n = 0
gradio_auth = os.getenv('GRADIO_AUTH')
while True:
    print('Relauncher: Launching...')
    if n > 0:
        print(f'\tRelaunch count: {n}')

    update_models_cmd = "python /workspace/model_updater/scripts/model_loader.py --config=/workspace/model_updater/config/models.yaml --dst=models/Stable-diffusion/"
    os.system(update_models_cmd)

    launch_cmd = "python webui.py --api --port 7861 --xformers --opt-split-attention --listen --enable-insecure-extension-access"
    if gradio_auth:
        launch_cmd += " --gradio-auth " + gradio_auth
    os.system(launch_cmd)
    print('Relauncher: Process is ending. Relaunching in 2s...')
    n += 1
    time.sleep(2)