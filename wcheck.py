import os
import sys
import yaml
import argparse


def yamlcheck(ysrc):
    workflow = None
    with open(ysrc, 'r') as buf:
        try:
            workflow = yaml.safe_load(buf)
        except yaml.YAMLError:
            return False
    checks = []
    if workflow is None:
        return False
    if 'jobs' not in workflow:
        return False
    if workflow['jobs'] is None:
        return False
    if not isinstance(workflow['jobs'], dict):
        return False
    for name in workflow['jobs']:
        job = workflow['jobs'][name]
        if job is None:
            return False
        if not isinstance(job, dict):
            return False
        if 'runs-on' in job:
            val = job['runs-on']
            if type(val) == str:
                checks.append(val.startswith('ubuntu-'))
            else:
                return False
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
