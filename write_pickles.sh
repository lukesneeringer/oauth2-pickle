#!/bin/bash
mkdir data 2> /dev/null
for f in oauth2_test/writers/$1/*.py; do
  python $f
done
