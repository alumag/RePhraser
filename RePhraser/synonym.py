import os
import random
from collections import Counter
import sqlite3
from nltk.corpus import wordnet as wn


class synonym(object):
    def getSynonym(self, word):
        """
        :return: synonyms of the object
        """
        synonym = self.getFromDB(word)
        if synonym is None:
            return self.choseSynonym(wn.synsets(word), word)
        return synonym

    def choseSynonym(self, ss, _word):
        count = []
        for s in ss:
            for word in s.lemma_names():
                if word != _word:
                    count.append(word)
        if len(count) <= 1 or count is None:
            self.add2DB([_word])
            return _word
        Key = self.add2DB(count)
        try:
            self._conn.execute("INSERT INTO synonym (Key, WORD) \
            VALUES (?, ?)", (Key, _word.lower()))
            self._conn.commit()
        except:
            pass
        return Counter(count).most_common(1)[0][0]

    def add2DB(self, words):
        # find counter
        counter = random.randint(1, 999999)
        cur = self._conn.cursor()
        cur.execute("SELECT Key FROM synonym WHERE Key="+str(counter))
        rows = cur.fetchone()
        if rows:  # not so random..
            return self.add2DB(words)
        for word in set(words):
            try:
                self._conn.execute("INSERT INTO synonym (Key, WORD) \
                VALUES (?, ?)", (counter, word.lower()))
                self._conn.commit()
            except:
                pass
        self._conn.commit()
        return counter

    def getFromDB(self, word):
        cur = self._conn.cursor()
        cur.execute("SELECT Key FROM synonym WHERE WORD=\""+word.lower()+"\"")
        self._conn.commit()
        rows = cur.fetchall()
        if len(rows) == 0:  # Does'nt exist
            return None
        cur.execute("SELECT WORD FROM synonym WHERE Key="+str(rows[0][0]) + " ORDER BY RANDOM()")
        self._conn.commit()
        return cur.fetchone()[0]

    def addTable(self):
        self._conn.execute('''CREATE TABLE synonym
               (ID INTEGER  PRIMARY KEY  AUTOINCREMENT     NOT NULL,
               Key INT NOT NULL,
               WORD           TEXT    NOT NULL);''')
        self._conn.commit()

    def __init__(self):
        """
        :param word: original word
        :return: synonym of the word or the same word
        """
        path = os.path.dirname(os.path.realpath(__file__))
        self._conn = sqlite3.connect(path+"\\synonym.db")

    def __del__(self):
        self._conn.close()
