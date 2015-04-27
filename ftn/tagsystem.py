__author__ = 'Giovanni'

class FtnTagInterface(object):
    def __init__(self):
        self.tags = []

    def addTag(self, tag):
        """
        Aggiunge il tag all'oggetto, se questo non e' gia' presente
        :param tag: string
        :return: None
        """

        if tag not in self.tags:
            self.tags.append(tag)

    def delTag(self, tag):
        """
        Rimuove il tag dall'oggetto, se questo e' presente
        :param tag: string
        :return: None
        """

        if tag in self.tags:
            self.tags.remove(tag)

    def hasTag(self, tag):
        """
        Verifica se l'oggetto ha il tag specificato
        :param tag:
        :return: True se il tag esiste, False altrimenti
        """

        if tag in self.tags:
            return True
        else:
            return False

    def writeTo(self, oggetto):
        """
        Scrive i tag nel nodo in scena
        :param oggetto: nodo
        :return: None
        """
        pass

class FtnTag(FtnTagInterface):
    def __init__(self, oggetto):
        super(FtnTag, self).__init__()
        """
        Sovraccarico dell'init per far si che la classe prenda i tag dall'oggetto in scena
        Non puo' essere testata con UnitTest quindi va testata nell'applicazione 3D
        :param oggetto: nodo
        :return:
        """
        self.userPropBuffer = []

    def formatTags(self):
        """
        Mette i tag in una stringa 'ftntag = aaa,bbb' in modo da inserirli nell'userpropbuffer
        :return: stringa formattata
        """
        stringa = "ftntag = "
        for i in self.tags:
            stringa += i
            stringa += ','
        stringa = stringa[:-1] #per rimuovere l'ultima virgola che non serve
        return stringa