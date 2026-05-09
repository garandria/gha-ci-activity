#!/bin/bash



cat ${1} | while read line ; do
    repository=$(echo ${line} | cut -d, -f1)
    defaultBranch=$(echo ${line} | cut -d, -f2)
    http_code=$(curl -s -o /dev/null -w "%{http_code}" "https://github.com/${repository}/tree/${defaultBranch}/.github/workflows")
    if [ "${http_code}" = "200" ] ; then
	echo "${repository}"
    fi
done
