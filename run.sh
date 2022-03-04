echo 'iniciando container...'
docker start algas_mysql_1
echo 'baixando dependencias necessarias para rodar o script...'
pip3 install -r requirements.txt
sleep 5
echo 'iniciando jupyter...'
jupyter notebook --port 8889 --ip=
