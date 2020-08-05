from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Marco Gutierrez'

doc = """
Mobile Devices Blocker for Online Experiments

*Requirements
-Don't set the secure_urls variable
-Add it to the app sequence inside the
respective session_config 

"""


class Constants(BaseConstants):
    name_in_url = 'no_mobile'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
