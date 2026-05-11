#!/bin/bash

DATA=data/workflows
WFDIR=.github/workflows

mkdir -p ${DATA}

quickclone() {
    GIT_TERMINAL_PROMPT=0 git clone --filter=blob:none --sparse https://github.com/${1}
    git -C $(basename ${1}) sparse-checkout set ${WFDIR}
}

while read repository ; do
    owner=$(dirname ${repository})
    repo=$(basename ${repository})
    gitdir=${repo}
    outdir=${DATA}/${owner}___${repo}
    echo "** ${repository}"
    quickclone ${repository}
    mkdir -p ${outdir}
    cp -r ${repo}/${WFDIR}/. ${outdir}
    rm -rf -- "${repo}"		# '--' is necessary when the folder starts with '-'
done
