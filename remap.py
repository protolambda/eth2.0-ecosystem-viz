from repos import url_to_out_name
from prepare import repos
import os

for repo_url, repo_paths in repos.items():
    log_name = url_to_out_name(repo_url) + '.txt'
    with open(os.path.join('logs_data', log_name)) as old, open(os.path.join('remapped_logs', log_name), 'w') as new:
        for line in old:
            # all fields would be: time, username, change mode, path
            fields = line.rsplit('|', 1)

            best_hit = ''
            best_data = None
            for path_prefix, path_data in repo_paths.items():

                if fields[1].startswith(path_prefix):
                    if path_prefix.count('/') >= best_hit.count('/'):
                        best_hit = path_prefix
                        best_data = path_data

            if best_data is not None:
                new.write(fields[0] + '|' + fields[1].replace(best_hit, '/'.join(best_data), 1))
