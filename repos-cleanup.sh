#!/bin/bash


gunzip -c ${1}												\
    | jq -r '.items[] | [.name, .defaultBranch, .isFork, .isArchived, .isDisabled, .isLocked] | @csv'	\
    | tr -d '"'												\
    | /usr/bin/grep "false,false,false,false"								\
    | cut -d, -f1-2
