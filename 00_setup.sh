#!/usr/bin/env bash
#
# Run this script once to set up the virtual environment, install
# the necessary python packages, and download the NLTK word tokenizer
#
# After running this script run the command
#
#     $ source venv/bin/activate
#
# to switch to the virtual environment. When you are done, you can
# run the command
#
#     $ deactivate
#
# to switch back to your normal shell.
#
##

# abort on first error
set -e

# make sure 'virtualenv' is installed
hash virtualenv &>/dev/null
if [  $? -eq 1 ]; then
    echo >&2 "Setup failed: could not find the 'virtualenv' command."
    echo >&2 "Try running \"pip install virtualenv\", then re-run setup.sh"
    exit 1;
fi

# set up the virtual environment
VENV=venv
virtualenv --no-site-packages --distribute --python=python3 "${VENV}"

# set the PYTHONPATH variable on activation
cat << EOF >> "${VENV}/bin/activate"

PYTHONPATH="${PWD}"
export PYTHONPATH

. ./access.sh
EOF

# tell git to ignore changes to access.sh
git update-index --assume-unchanged access.sh

# switch to the virtual environment
source "${VENV}/bin/activate"

# install the required python packages (python-twitter)
pip install -r requirements.txt
