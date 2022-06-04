import service.DataTwitterService as TwitterService
import service.GeracaoDadosService as GeracaoDadosService
import service.FileHelperService as FileHelperService
import service.BucketService as BucketService
from tweassets.content import content

geracaoDadosService = GeracaoDadosService.GeracaoDadosService()
data_twitter = TwitterService.DataTwitter()
bucket_service = BucketService.BucketService()

OPERACAO_INVALIDA = "Operação inválida, tente novamente"


def run_data_twitter(query, limit):
    return data_twitter.find_recent_tweets(query, limit)


def archive_generation_option():
    print("Qual tipo de arquivo deseja salva no bucket:")
    print("Tecle [1] para .csv")
    print("Tecle [2] para .txt")
    print("Tecle [3] para .json")
    print("Tecle [4] para exibir a nuvem de palavras")
    print("Tecle [Enter] para sair")
    return input()


def generete_name(query, archive_type):
    split_by_space_query = query.split(" ")
    new_query = "_".join(split_by_space_query)
    if archive_type == "csv":
        return new_query + ".csv"
    elif archive_type == "txt":
        return new_query + ".txt"
    elif archive_type == "json":
        return new_query + ".json"
    else:
        raise Exception("Tipo de arquivo inválido")


def generate_files_from_tweets(tweets, query):
    while True:
        option = archive_generation_option()

        if option == "1":
            FileHelperService.FileHelperService.save_csv_archive(tweets, content['csv_archive_name'],
                                                                 content['fieldnames'])
            bucket_service.send_to_not_structured(content['csv_archive_name'], generete_name(query, "csv"))
        elif option == "2":
            FileHelperService.FileHelperService.save_txt_archive(tweets, content['txt_archive_name'])
            bucket_service.send_to_not_structured(content['txt_archive_name'], generete_name(query, "txt"))
        elif option == "3":
            FileHelperService.FileHelperService.save_tweets_to_json_archive(tweets, content['json_archive_name'])
            bucket_service.send_to_not_structured(content['json_archive_name'], generete_name(query, "json"))
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
            query = input(content['input_string'])
            limit = int(input(content['input_limit']))
            tweets = run_data_twitter(query, limit)
            generate_files_from_tweets(tweets, query)
        elif option == "2":
            geracaoDadosService.contador_tempo_memoria()
        elif option == "":
            return
        else:
            print(OPERACAO_INVALIDA)


main()
