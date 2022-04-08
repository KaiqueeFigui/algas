echo 'Atualizando pacotes...'
sudo apt-get update && sudo apt-get upgrade -y
clear
echo 'Instalando dependências necessárias...'
sudo apt install docker.io -y
clear
sudo apt install docker-compose -y
clear
sudo apt install python3-pip -y
clear

echo 'Atualizando repositório...'
git pull
clear

echo 'Criando arquivo para váriavel de ambiente ...'
cat ./src/.env.example >> .env

echo 'Iniciando docker compose...'
sudo docker-compose up -d

echo 'Instalando dependências do projeto...'
pip3 install -r requirements.txt
clear

echo 'Instalação concluída com sucesso!'
sleep 3

echo 'Iniciando aplicação...'
if [ -f "./src/main.py" ]; then
    python3 ./src/main.py
else
    echo 'O arquivo main.py não foi encontrado!'
fi

