import tweepy
import csv
import matplotlib.pyplot as plt
import os
from os import path
from dotenv import load_dotenv
from datetime import datetime
from wordcloud import WordCloud, STOPWORDS

stop_words = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'é', 'com', 'não', 'uma', 'os', 'no', 'se',
              'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'à', 'seu', 'sua',
              'ou', 'ser', 'quando', 'muito', 'há', 'nos', 'já', 'está', 'eu', 'também', 'só', 'pelo', 'pela', 'até',
              'isso', 'ela', 'entre', 'era', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem', 'nas', 'me',
              'esse', 'eles', 'estão', 'você', 'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 'minha',
              'têm', 'numa', 'pelos', 'elas', 'havia', 'seja', 'qual', 'será', 'nós', 'tenho', 'lhe', 'deles', 'essas',
              'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 'te', 'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu',
              'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas',
              'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive',
              'esteve', 'estivemos', 'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja',
              'estejamos', 'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem',
              'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos', 'haja',
              'hajamos', 'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei',
              'houverá', 'houveremos', 'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'era',
              'éramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja', 'sejamos', 'sejam', 'fosse',
              'fôssemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'será', 'seremos', 'serão', 'seria', 'seríamos',
              'seriam', 'tenho', 'tem', 'temos', 'tém', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos',
              'tiveram', 'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem',
              'tiver', 'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam', 'rt',
              't', 'https', 'co']


class DataTwitter:

    def __init__(self):
        self.query = ""
        load_dotenv()
        twitter_bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        self.client = tweepy.Client(twitter_bearer_token)
        self.stopwords = set(STOPWORDS)
        self.stopwords.update(stop_words)
        self.directory = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    def find_recent_tweets(self, query, limit):
        print(f"Start finding Tweets by query: {query} - DataTwitterService::find_recent_tweets")
        self.query = query
        date_in_datetime_format = datetime.today()
        datareal = datetime.isoformat(date_in_datetime_format)

        tweets = tweepy.Paginator(
            self.client.search_recent_tweets,
            query=self.query,
            tweet_fields=['context_annotations', 'created_at', 'source'],
            end_time=(datareal + "Z"),
            max_results=100
        ).flatten(limit)
        print(f"End finding Tweets by query: {query} - DataTwitterService::find_recent_tweets")
        return self.__copy_tweets(tweets)

    def __copy_tweets(self, tweets):
        copy = []
        for tweet in tweets:
            copy.append(tweet)
        return copy

    def show_word_cloud(self, content_source_filename, delimiter=';'):
        comment_words = ''

        with open(content_source_filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            for row in reader:
                tokens = row[0].split()

                for i in range(len(tokens)):
                    tokens[i] = tokens[i].lower()

            comment_words += " ".join(tokens) + " "
            self.__plot_graphic(
                WordCloud(
                    background_color="white",
                    max_font_size=60,
                    margin=10,
                    stopwords=self.stopwords,
                ).generate(comment_words)
            )

    def __plot_graphic(self, content):
        plt.figure()
        plt.title(self.query)
        plt.imshow(content, interpolation='bilinear')
        plt.axis("off")
        plt.show()