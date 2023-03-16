import os
import shutil
import logging
from utils import convert_diff_to_sd
from huggingface_hub import snapshot_download, HfApi


class DiffusersLoader(object):

    def __init__(self, name, data, config_root) -> None:
        self.name = name
        self.model_name = data['model_name']
        self.config_path = os.path.join(config_root, data['config'])
        self.half = data.get('half', False)
        self.use_safetensors = data.get('use_safetensors', False)
        self.hf_api = HfApi()
        

    def load(self, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        model_info = self.hf_api.model_info(self.model_name)
        hash_file = os.path.join(output_dir, f"{self.name}.hash")
        ckpt_file = os.path.join(output_dir, f"{self.name}.ckpt")
        hash = self.read_hash(hash_file)
        if hash == model_info.sha and os.path.exists(ckpt_file):
            logging.info(f"Model {self.name} is up to date")
            return
        
        repo = snapshot_download(self.model_name, token=True)
        convert_diff_to_sd.convert(repo, ckpt_file, half=self.half, use_safetensors=self.use_safetensors)
        shutil.copy(self.config_path, os.path.join(output_dir, f"{self.name}.yaml"))
        self.write_hash(hash_file, model_info.sha)

    
    def read_hash(self, hash_file):
        if os.path.exists(hash_file):
            with open(hash_file, 'r') as f:
                return f.read()
        return None
    

    def write_hash(self, hash_file, hash):
        with open(hash_file, 'w') as f:
            f.write(hash)
