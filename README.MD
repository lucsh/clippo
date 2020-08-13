
## TLDR (macOS)
```
curl https://pyenv.run | bash

#Agregar al bashrc o agregar el plugin pyenv a zshrc

    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

#Instalar python

pyenv install -v 3.6.10 && pyenv global 3.6.10

#Instalar dependencias
pip install -r requirements.txt

#descargar pretrain en español
python -m spacy download es_core_news_md

#en otra ventana correr las acciones
rasa run actions

#Entrenar
rasa train

#Correr 
rasa interactive
```

## 1. Configuracion del enviroment

### 1.1. Instalar pyenv

#### 1.1.1. MacOS
```
brew install pipenv
```
    
#### 1.1.2. Centos
```
yum install zlib-devel bzip2 bzip2-devel readline-devel sqlite \
sqlite-devel openssl-devel xz xz-devel libffi-devel wget git

curl https://pyenv.run | bash
```
    

#### 1.1.3. Ubuntu
```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl

curl https://pyenv.run | bash

```

#### 1.1. Agregar al bashrc
> Load pyenv automatically by adding the following to ~/.bashrc:
> Or by adding the pyenv pluguin to zshrc " plugins=(git pyenv) "

    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

### 1.2. Instalar python 3.6
`pyenv install -v 3.6.10 && pyenv global 3.6.10`

### 1.3. Install dependencias
```pip install -r requirements.txt
python -m spacy download es_core_news_md
```

### 2. Correr el asistente

#### 2.1 Correr las acciones

(en otra ventana )

`rasa run actions`
         
#### 2.2. Entrenar Rasa
`rasa train`

#### 2.3.1 Hablarle al asistente
`rasa shell` 

para debug:

`rasa shell  --debug`


#### 2.3.2 Aprendizaje interactivo
`rasa interactive`

## RASA X

[https://rasa.com/docs/rasa-x/installation-and-setup/docker-compose-script/](https://rasa.com/docs/rasa-x/installation-and-setup/docker-compose-script/)

`$ wget -qO docker-compose.yml https://storage.googleapis.com/rasa-x-releases/0.25.2/docker-compose.ce.yml`

`$ wget -qO rasa_x_commands.py https://storage.googleapis.com/rasa-x-releases/0.25.2/rasa_x_commands.py`
