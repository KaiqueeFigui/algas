import service.DataTwitterService as TwitterService
import service.GeracaoDadosService as GeracaoDadosService
import service.FileHelperService as FileHelperService
from tweassets.content import content

geracaoDadosService = GeracaoDadosService.GeracaoDadosService()
OPERACAO_INVALIDA = "Operação inválida, tente novamente"
data_twitter = TwitterService.DataTwitter()


def run_data_twitter():
    input_str = input(content['input_string'])
    input_limit = int(input(content['input_limit']))
    return data_twitter.find_recent_tweets(input_str, input_limit)


def archive_generation_option():
    print("Qual tipo de arquivo deseja gerar:")
    print("Tecle [1] para .csv")
    print("Tecle [2] para .txt")
    print("Tecle [3] para .json")
    print("Tecle [4] para exibir a nuvem de palavras")
    print("Tecle [Enter] para sair")
    return input()


def generate_files_from_tweets(tweets):
    while True:
        option = archive_generation_option()

        if option == "1":
            FileHelperService.FileHelperService.save_csv_archive(tweets, content['csv_archive_name'],
                                                                 content['fieldnames'])
        elif option == "2":
            FileHelperService.FileHelperService.save_txt_archive(tweets, content['txt_archive_name'])
        elif option == "3":
            FileHelperService.FileHelperService.save_json_archive(tweets, content['json_archive_name'])
        elif option == "4":
            FileHelperService.FileHelperService.save_csv_archive(tweets, content['csv_archive_name'],
                                                                 content['fieldnames'])
            data_twitter.show_word_cloud(content_source_filename=content['csv_archive_name'])
        elif option == "":
            return
        else:
            print(OPERACAO_INVALIDA)


def data_generation_option():
    print("Selecione uma das seguintes opções:")
    print("Tecle [1] para Buscar Posts no Twitter")
    print("Tecle [2] para Geração de Dados aleatórios")
    print("Tecle [Enter] para sair")
    return input()


def main():
    while True:
        option = data_generation_option()
        if option == "1":
            tweets = run_data_twitter()
            generate_files_from_tweets(tweets)
        elif option == "2":
            geracaoDadosService.contador_tempo_memoria()
        elif option == "":
            return
        else:
            print(OPERACAO_INVALIDA)


main()
