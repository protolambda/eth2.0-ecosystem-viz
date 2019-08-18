import subprocess
from repos import url_to_out_name
from prepare import repos
import os

dry = True


def run(args, cwd=''):
    if dry:
        print(f'gourcing (workdir: {cwd}): {" ".join(args)}')
    else:
        subprocess.run(args, cwd=cwd)


for repo_url in repos.keys():
    repo_name = url_to_out_name(repo_url)
    out_name = repo_name + '.txt'
    out_path = os.path.join('logs_data', out_name)
    if os.path.exists(out_path):
        # delete old log
        run(['rm', out_path], cwd=out_path)

    # run gource
    run(['gource', '--output-custom-log', out_path, os.path.join('repos', repo_name)])
