from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


doc = """
This is a standard 2-player trust game where the amount sent by player 1 gets
tripled. The trust game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'trust_prod'
    players_per_group = 2
    num_rounds = 2

    instructions_template = 'trust_production/instructions.html'
    instructions_button = "trust_production/Instructions_Button.html"
    contact_template = "initial_quiz/Contactenos.html"

    # Initial amount allocated to each player
    endowment = c(100)
    multiplier = 3
    n_rounds = num_rounds # for using it on the instructions in initial quiz


class Subsession(BaseSubsession):
    def vars_for_admin_report(self):
        sent_amounts = [
            g.sent_amount for g in self.get_groups() if g.sent_amount != None
        ]
        sent_back_amounts = [
            g.sent_back_amount for g in self.get_groups() if g.sent_back_amount != None
        ]
        if sent_amounts and sent_back_amounts:
            return dict(
                avg_sent_amount=sum(sent_amounts) / len(sent_amounts),
                range_sent_amount = str([int(min(sent_amounts)), int(max(sent_amounts))]) + " puntos",
                avg_sent_back_amount=sum(sent_back_amounts) / len(sent_back_amounts),
                range_sent_back_amount = str([int(min(sent_back_amounts)), int(max(sent_back_amounts))]) + " puntos"
            )
        else:
            return dict(
                avg_sent_amount='(no data)',
                range_sent_amount='(no data)',
                avg_sent_back_amount='(no data)',
                range_sent_back_amount='(no data)',
            )
        

class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=0, max=Constants.endowment, doc="""Amount sent by P1"""
    )

    sent_back_amount = models.CurrencyField(doc="""Amount sent back by P2""", min=c(0))

    def sent_back_amount_max(self):
        return self.sent_amount * Constants.multiplier

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
        p2.payoff = self.sent_amount * Constants.multiplier - self.sent_back_amount


class Player(BasePlayer):
    def role(self):
        return {1: 'A', 2: 'B'}[self.id_in_group]
