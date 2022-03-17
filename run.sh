echo 'Iniciando container MySQL...'
docker start algas_mysql_1
echo 'Baixando e instalando dependências necessárias para o script...'
pip3 install -r requirements.txt
sleep 5
echo 'Iniciando jupyter notebook...'
jupyter notebook src/insert_data.ipynb --port 8889 --ip=
