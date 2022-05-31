import csv
import json


class FileHelperService:

    @staticmethod
    def save_csv_archive(tweets, filename, fieldnames):
        with open(filename, 'w', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames, delimiter=";")
            writer.writeheader()
            for tweet in tweets:
                writer.writerow({
                    fieldnames[0]: tweet.text,
                    fieldnames[1]: tweet.created_at,
                    fieldnames[2]: tweet.source
                })

    @staticmethod
    def save_txt_archive(tweets, filename, delimiter='   ...[end]\n'):
        with open(filename, 'w', encoding="utf-8") as txt:
            for tweet in tweets:
                txt.write(str(tweet) + delimiter)

    @staticmethod
    def save_json_archive(tweets, filename):
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

