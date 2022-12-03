#!/bin/bash
#
set -eu -o pipefail

a=$( echo ${1} | bc )
b=$( printf %02d ${a} )

source ~/.aoc2022
curl -s -b session=${sessionkey} https://adventofcode.com/2022/day/${a}/input > ${b}/input || exit
cat ${b}/input
wc ${b}/input
