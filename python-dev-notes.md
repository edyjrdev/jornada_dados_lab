# Preparando Ambiente Python, Git, GitLab, VSCode

## Vscode
extensoes
- python
- material theme

## git
Comandos
1. git --version
1. git config globlal --list
1. git config --global user.name "Edy Epumuceno Rodrigues Junior"
1. git config --global user.email edyjrdev@gmail.com
1. git config --list --global
1. git config --list

## Github
gerar ssh key
ssh-keygen -t ed25519 -C "edyjrdev@gmail.com"


## Pyenv - Multipython
pyenv - https://github.com/pyenv-win/pyenv-win
### Habilitar PowerShell para instalar  
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine`  
### Instalar Pyenv-win  
`Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"`  
pyenv comandos  
variaveis de ambiente config  
PYENV=C:\Users\edyjr\.pyenv\pyenv-win  
PYENV_ROOT=C:\Users\edyjr\.pyenv\pyenv-win  
PYENV_HOME=C:\Users\edyjr\.pyenv\pyenv-win  

Incluir Acima no Path  
PATH=C:\Users\edyjr\.pyenv\pyenv-win\bin;  C:\Users\edyjr\.pyenv\pyenv-win\bin  

pyenv versions  
pyenv install -l  

pyenv install 3.12.10  
pyenv install 3.8.5  
pyenv install 3.13.3  
pyenv global 3.13.3  

## Venv
python -m venv .venv
source .venv/Scripts/activate
deactivate 

## Pipx - https://github.com/pypa/pipx
pip install pipx
pipx ensurepath
pipx install argcomplete
pipx completions

PATH - Subir prioridade de execução de 
c:\users\edyjr\.local\bin

## Poetry - https://python-poetry.org/ 
pipx install poetry
pipx upgrade poetry


### Config poetry para adicionar venv a cada projeto
poetry config virtualenvs.in-project true

#### Poetry - Criar Projeto ou Usar um existente
poetry new projeto ou poetry init em projeto existente  
pyenv local 3.12.10  
conferir arquivo pyproject.toml em requires-python = ">=3.12"  
poetry env use 3.12.10  
source .venv/Scripts/activate  
poetry add django  
conferir arquivo pyproject.toml em dependencies - somente dependencias instaladas para o projeto  
pip freeze > requirements.txt  
poetry remove django  
pip freeze  
deactivate  

## ipython e jupyterlab
pipx install ipython  
pipx install jupyterlab  

## Github CLI
comandos
- gh auth login
- gh repo create jd2025-python-aula01 --public