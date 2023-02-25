


export GIT_MIRROR=https://ghproxy.com/
export BOA_TUNA=1
export BOA_PYTHON_VERSION=3.9
export BOA_CONDA_VERSION='Miniconda3-py39_4.12.0'
export BOA_CONDA_MIRROR=https://mirrors.bfsu.edu.cn/anaconda/miniconda

yarn run build


node ./example/test.js
