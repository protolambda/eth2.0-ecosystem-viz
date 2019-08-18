import subprocess
from repos import url_to_out_name
from prepare import repos
import os

dry = False


def run(args, cwd=''):
    if dry:
        print(f'cloning (workdir: {cwd}): {" ".join(args)}')
    else:
        subprocess.run(args, cwd=cwd)


for repo_url in repos.keys():
    out_name = url_to_out_name(repo_url)
    out_path = os.path.join('repos', out_name)
    if os.path.exists(out_path):
        # pull updates for existing repos
        run(['git', 'pull', 'origin', 'master'], cwd=out_path)
    else:
        # clone new repos
        run(['git', 'clone', repo_url, out_name], cwd='repos')
