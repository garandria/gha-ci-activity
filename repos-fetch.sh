#!/bin/bash

#                                                                      Minimum 100 PRs              Without forks
mkdir -p data
curl --insecure --output data/repos.json.gz \
     "https://seart-ghs.si.usi.ch/api/r/download/json?nameEquals=false&pullsMin=100&sort=name%2Casc&excludeForks=true&hasPulls=true"
