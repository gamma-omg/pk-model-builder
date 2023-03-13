import os
import shutil
from huggingface_hub import hf_hub_download

class CheckpointLoader(object):
    def __init__(self, name, data, config_root):
        self.name = name
        self.repo = data['repo']
        self.file = data['file']
        self.config_path = os.path.join(config_root, data.get('config', None))
        
    
    def load(self, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        file = hf_hub_download(repo_id=self.repo, filename=self.file, token=True)
        shutil.copy(file, os.path.join(output_dir, f"{self.name}.ckpt"))        

        if self.config_path is not None:
            shutil.copy(self.config_path, os.path.join(output_dir, f"{self.name}.yaml"))