# !/usr/bin/env bash

# BOLD='\u001b[1m'
# YELLOW='\033[1;33m'
# RESET='\033[0m'

readonly CWD=$(realpath .)
readonly GUI=$(realpath ./src/paint/gui)

python3.9 -m venv $CWD/.venv --upgrade-deps

source $CWD/.venv/bin/activate

python3 -m pip install --upgrade pip

pip install -r requirements.txt

pip install .

nodeenv -p

cd $GUI

npm install electron electron-tabs fs path

mkdir -p $CWD/data $CWD/results

rm -rf $CWD/build $CWD/src/*.egg-info

deactivate
