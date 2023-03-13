import os
from huggingface_hub.repository import Repository


class RepoLoader(object):
    def __init__(self, name, data, _) -> None:
        self.name = name
        self.repo_id = data['repo']

    def load(self, output_dir):
        repo_root = os.path.join(output_dir, self.name)
        if not os.path.exists(repo_root):
            os.makedirs(repo_root)

        repo = Repository(repo_root, clone_from=self.repo_id, token=True)
        repo.git_pull()