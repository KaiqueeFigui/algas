import csv
import json


class FileHelperService:

    @staticmethod
    def save_csv_archive(data_amount, filename, fieldnames):
        with open(filename, 'w', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames, delimiter=";")
            writer.writeheader()
            for data in data_amount:
                writer.writerow({
                    fieldnames[0]: data.text,
                    fieldnames[1]: data.created_at,
                    fieldnames[2]: data.source
                })

    @staticmethod
    def save_txt_archive(data_amount, filename, delimiter='   ...[end]\n'):
        with open(filename, 'w', encoding="utf-8") as txt:
            for data in data_amount:
                txt.write(str(data) + delimiter)

    @staticmethod
    def save_tweets_to_json_archive(tweets, filename):
        with open(filename, 'w', encoding='utf-8') as json_file:
            try:
                list_object_tweets = []

                for tweet in tweets:
                    list_object_tweets.append({
                        "text": tweet.text,
                        "created_at": str(tweet.created_at),
                        "source": tweet.source
                    })

                data = {
                    "tweets": list_object_tweets
                }

                json.dump(data, json_file, skipkeys=False, indent=4)
            except Exception as ex:
                raise Exception("Erro ao salvar arquivo", ex)

