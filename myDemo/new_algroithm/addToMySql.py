from myDemo.models import Sentence
from myDemo.new_algroithm.makeSEP import make_sep
import django.db.transaction


def addToMySQL(inputEssay,author,name):
    inputEssayList = make_sep(inputEssay)
    for sentence in inputEssayList:
        #加入mysql
        try:
            with django.db.transaction.atomic():
                Sentence.objects.create(
                    id = Sentence.objects.count()+1,
                    name = name,
                    author = author,
                    sentence = sentence
                )
        except Exception:
            pass