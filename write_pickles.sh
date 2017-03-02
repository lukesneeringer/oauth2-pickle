#!/bin/bash
mkdir data 2> /dev/null
for f in oauth2_test/writers/$OAUTH2_WRITERS/*.py; do
  python $f
done
