from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

debug = True

author = "Marco Gutierrez"

doc = """
Dynamic Quiz for elicit understanding level 
of an experiment

*Each question has it's answers shuffled
with a system randomization
"""

#TODO: randomize question order
class Constants(BaseConstants):
    """
    Description:
        Inherits oTree Class BaseConstants. Defines constants for
        the experiment these will remain unchanged
    """

    players_per_group = None
    instructions_template = "trust/instructions.html"
    contact_template = "initial_quiz/Contactenos.html"
    instructions_button = "trust/Instructions_Button.html"
    num_rounds = 1
    timer = 20
    payment_per_answer = c(5)

    name_in_url = 'Initial_Quiz'  # name in webbrowser

    # Initial amount allocated to each player
    endowment = c(100)
    multiplier = 3
    n_rounds = num_rounds # for using it on the instructions in initial quiz

    '''Quiz Answers'''

    # Answers according to the code
    quiz_fields = dict(
        question_1_response=1,
        question_2_response=1,
        question_3_response=2,
        question_4_response=0,
    )

    quiz_questions = ['¿Cuántos roles hay por pareja y cuáles son?',
                      '¿Durante una ronda, en qué casos cambias de grupo?',
                      '¿Qué pasa con el dinero que envía el participante A al participante B?',
                      '¿Qué opciones tiene el participante B tras recibir el dinero multiplicado?']

    # Displayed answers
    quiz_answers = ['2: Rol A y Rol B', 
                    'En ningun caso', 
                    'Es multiplicado por 3 y luego la cantidad multiplicada es recibida por B',
                    'Quedarse con todo lo recibido o darle la cantidad que desee de regreso a A']
    
    # Write here your possible choices as [number, string_with_choice]
    q1_choices = [[0, '3: Estado, Comprador y Vendedor'], 
                  [1, '2: Rol A y Rol B'],
                  [2, '2: Jugador 1 y Jugador 2'], 
                  [3, '1: Los dos tienen el mismo rol']]
    q2_choices = [[0, 'Cuando B recibe una cantidad positiva'], 
                  [1, 'En ningun caso']]
    q3_choices = [[0, 'Es directamente recibido por B'],
                  [1, 'Se carga un impuesto y luego es recibido por B'],
                  [2, 'Es multiplicado por 3 y luego la cantidad multiplicada es recibida por B']]
    q4_choices = [[0, 'Quedarse con todo lo recibido o darle la cantidad que desee de regreso a A'],
                  [1, 'Ninguna. Después de recibirlo, termina el experimento'],
                  [2, 'Prestarle parte del dinero a A a cambio de una tasa de interés baja.']]

    # To randomize the order in which the answers are presented
    random.SystemRandom().shuffle(q1_choices)
    random.SystemRandom().shuffle(q2_choices)
    random.SystemRandom().shuffle(q3_choices)
    random.SystemRandom().shuffle(q4_choices)


class Subsession(BaseSubsession):
    """
    Description:
        Inherits oTree Class BaseSubsession. Defines subsession for
        the experiment.

    Input:
        None

    Output:
        None
    """
    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['final_payoff'] = 0
            p.participant.vars['quiz_payoff'] = 0
            p.participant.vars['quiz_earnings'] = 0


class Group(BaseGroup):
    """
    Description:
        Inherits BaseGroup oTree class. Assigns group characteristics.

    Input:
        None

    Output:
        None
    """


class Player(BasePlayer):
    """
    Description:
        Inherits oTree class BasePlayer. Defines player characteristics.

    Input:
        None

    Output:
        None
    """

    time_spent_on_instructions = models.FloatField(initial=0)

    def current_field(self):
        return 'question_{}_response'.format(self.quiz_page_counter + 1)

    quiz_incorrect_answer = models.StringField(initial=None)
    quiz_respuesta_incorrecta = models.StringField(initial=None)

    # IP field
    player_ip = models.StringField()
    current_practice_page = models.IntegerField(initial=0)

    '''Quiz'''

    # Counter of the questions answered correctly on the first try
    num_correct = models.IntegerField(initial=0)
    quiz_page_counter = models.IntegerField(initial=0)
    # Inc Attemp per question
    q_incorrect_attempts = models.IntegerField(initial=0)
    q_timeout = models.IntegerField(initial=0)
    q_validation = models.IntegerField(initial=0)
    q_attempts = models.IntegerField(initial=0)
    error_sequence = models.CharField(initial='')
    timeout_sequence = models.CharField(initial='')

    question_1_response = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                              choices=Constants.q1_choices)
    question_2_response = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                              choices=Constants.q2_choices)
    question_3_response = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                              choices=Constants.q3_choices)
    question_4_response = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                              choices=Constants.q4_choices)
    quiz_earnings = models.CurrencyField(initial=0)

    # Hidden Field for detecting bots
    quiz_dec_2 = models.LongStringField(blank=True)
