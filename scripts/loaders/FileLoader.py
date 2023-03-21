import os
import shutil
from huggingface_hub import hf_hub_download

class FileLoader(object):
    def __init__(self, name, data, config_root):
        self.name = name
        self.repo = data['repo']
        self.file = data['file']
        self.symlink = data.get('symlink', True)
        self.config_root = config_root
        self.config_path = data.get('config', None)
        
    
    def load(self, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        src_file = hf_hub_download(repo_id=self.repo, filename=self.file, token=True)
        dst_file = os.path.join(output_dir, f"{self.name}.ckpt")
        
        if os.path.exists(dst_file):
            os.remove(dst_file)

        if self.symlink:
            os.symlink(src_file, dst_file)        
        else:
            shutil.copy(src_file, dst_file)

        if self.config_path is not None:
            config_file = os.path.join(self.config_root, self.config_path)
            shutil.copy(config_file, os.path.join(output_dir, f"{self.name}.yaml"))