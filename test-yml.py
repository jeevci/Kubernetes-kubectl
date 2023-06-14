#pip install pyyml
import yaml
with open ('sam-first.yml','r') as file:
    try:
        print(yaml.safe_load(file))
    except yaml.YAMLError as exc:
        print(exc)


