from collections import defaultdict
from repos import graph

# repo git link -> repo subset path -> ((topic, subtopic, name), repo path)
repos = defaultdict(dict)

for topic, topic_data in graph.items():
    for subtopic, subtopic_data in topic_data.items():
        for entry in subtopic_data:
            if isinstance(entry, tuple):
                if len(entry) == 2:
                    repos[entry[1]][''] = (topic, subtopic, entry[0])
                elif len(entry) == 3:
                    repos[entry[1]][entry[2]] = (topic, subtopic, entry[0])
                else:
                    print("invalid: ", subtopic_data)
            else:
                name = entry
                if name.startswith('https://github.com/'):
                    name = name[len('https://github.com/'):]
                if name.endswith('.git'):
                    name = name[:-len('.git')]
                repos[entry][''] = (topic, subtopic, name)
