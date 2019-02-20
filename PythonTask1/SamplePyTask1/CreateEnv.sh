#!/usr/bin/env bash

function createPYENV(){
if [[ -d ~/.pyenv/versions/$1 ]]; then
    echo "Certain python version already exists!"
else
pyenv install "$1"
pyenv global "$1"
pyenv virtualenv python_v"$1"
pyenv global 3.7.1
fi
}
createPYENV 2.7.6
createPYENV 3.7.2