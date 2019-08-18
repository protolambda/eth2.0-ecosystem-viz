# Eth2 ecosystem gource

Run:

```bash
# clone/update all repositories
python3 clone.py

# runs gource to generate log files for each repo
python3 logs.py

# remap the log files to put them in their ecosystem spot
python3 remap.py

# combine remapped data in combined.txt (sorted on time)
bash combine.sh

# replace usernames (TODO)
python3 usernames.py
```
