import os
import sys
import yaml


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
    repos = sys.argv[1]
    for repo in os.listdir(repos):
        rdir = os.path.join(repos, repo)
        fs = [os.path.join(rdir, f) for f in os.listdir(rdir)]
        if all([yamlcheck(ysrc) for ysrc in fs \
                if os.path.splitext(ysrc)[-1] in {'yaml', 'yml'}]):
            print(os.path.basename(rdir).replace('___', '/', 1))


if __name__ == "__main__":
    main()
