echo 'Iniciando container MySQL...'
docker start algas_mysql_1
echo 'Baixando e instalando dependências necessárias para o script...'
pip3 install -r requirements.txt