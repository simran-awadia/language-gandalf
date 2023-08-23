import abc


class ProficiencyLevel(abc.ABC):
    @property
    @abc.abstractmethod
    def name(self):
        pass

    @property
    @abc.abstractmethod
    def source(self):
        pass

    @property
    @abc.abstractmethod
    def example_test(self):
        pass

    @property
    @abc.abstractmethod
    def skill_level_description(self):
        pass


class Novice(ProficiencyLevel):
    name = "Novice"
    source = "children's book"
    # from Petit Poulet
    example_test = {
        "text": "Il lit les nouvelles. Il voit une histoire terrifiante avec un titre terrifiant, qui dit : LE CIEL "
                "EST EN TRAIN DE TOMBER ",
        "question": "Qu'arrive-t-il au ciel?",
    }
    skill_level_description = "You can comprehend simple written communication and could read a children's book!"


class Intermediate(ProficiencyLevel):
    name = "Intermediate"
    source = "modern novel"
    # from L'etrange
    example_test = {
        "text": "Maman disait que même si on est malheureux, il y a toujours de quoi être reconnaissant. Et chaque "
                "matin, quand le ciel s'éclairait, j'étais d'accord avec elle.",
        "question": "Qui cite l'auteur?",
    }
    skill_level_description = "You can comprehend moderately complex written communication and could read a novel!"


class Champion(ProficiencyLevel):
    name = "Champion"
    source = "medical journal"
    # from https://www.sciencedirect.com/science/article/abs/pii/S0248866323001273
    example_test = {
        "text": "La première patiente présentait un angor stable sur une coronarite du tronc commun avec une sténose "
                "ostiale. Le second patient présentait une coronarite ostiale. Deux ans après, il a présenté une "
                "rechute avec un syndrome coronarien aigu, d’évolution favorable après angioplastie, majoration des "
                "corticoïdes.",
        "question": "Quel patient a rechuté?",
    }
    skill_level_description = "You can comprehend complex written communication and could read a research paper!"
