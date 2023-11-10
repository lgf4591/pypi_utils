import subprocess
import os
import sys
import toml

project_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
project_url = f"https://github.com/lgf4591/{project_name}"

def run_command(cmd: str) -> None:
    subprocess.run(cmd, shell=True, check=True)


def publish(version: str) -> None:
    print(f"project is {project_name}, publish version {version} now!!!")
    
    with open('pyproject.toml', 'r', encoding="utf-8") as toml_file:
        config = toml.load(toml_file)
    print(f"current version is {config['tool']['poetry']['version']}")
    
    config['tool']['poetry']['name'] = project_name
    config['tool']['poetry']['version'] = version
    config['tool']['poetry']['homepage'] = project_url
    config['tool']['poetry']['repository'] = project_url
    config['tool']['poetry']['scripts']['dev'] = f"{project_name}.scripts:dev"
    config['tool']['poetry']['scripts']['lint'] = f"{project_name}.scripts:pylint"
    config['tool']['poetry']['scripts']['fix'] = f"{project_name}.scripts:fix"
    
    with open('pyproject.toml', 'w', encoding="utf-8") as toml_file:
        toml.dump(config, toml_file)
    
    # BUG: error: pathspec 'v0.1.1'' did not match any file(s) known to git
    # run_command("git status")
    # run_command("git add .")
    # run_command(f"git commit -m 'release v{version}'")
    # run_command(f"git tag v{version} -m 'release v{version}'")
    # run_command(f"git push origin v{version}")


if __name__ == "__main__":
    print(f"current project is {project_name}")
    if len(sys.argv) > 1:
        publish(sys.argv[1])

# python main.py 0.1.0
