echo "**** syncing venv to workspace, please wait. This could take a while on first startup! ****"
rsync --remove-source-files -rlptDu /venv/ /workspace/venv/

echo "**** syncing stable diffusion to workspace, please wait ****"
rsync --remove-source-files -rlptDu /stable-diffusion-webui/ /workspace/stable-diffusion-webui/

if [[ $RUNPOD_STOP_AUTO ]]
then
    echo "Skipping auto-start of webui"
else
    echo "Started webui through relauncher script"
    cd /workspace/stable-diffusion-webui
    python relauncher.py &
fi