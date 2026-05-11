import os
import sys
import yaml
import argparse


def yamlcheck(ysrc):
    workflow = None
    with open(ysrc, 'r') as buf:
        workflow = yaml.safe_load(buf)
    checks = []
    for name in workflow['jobs']:
        job = workflow['jobs'][name]
        if 'runs-on' in job:
            checks.append(job['runs-on'].startswith('ubuntu-'))
        else:
            return False
    return all(checks)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="local directory")
    args = parser.parse_args()

    repos = args.directory
    for repo in os.listdir(repos):
        rdir = os.path.join(repos, repo)
        fs = [os.path.join(rdir, f) for f in os.listdir(rdir)\
              if os.path.splitext(f)[-1] in {'.yaml', '.yml'}]
        if all([yamlcheck(ysrc) for ysrc in fs]):
            print(os.path.basename(rdir).replace('_', '/', 1))


if __name__ == "__main__":
    main()
