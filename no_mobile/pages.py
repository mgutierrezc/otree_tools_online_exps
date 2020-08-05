from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class TestMobile(Page):
    def is_displayed(self):
        # request if type of HTTP user agent
        user_agent = self.request.META['HTTP_USER_AGENT']
        self.participant.vars['is_mobile'] = False
        for substring in ['Mobi', 'Android']:
            if substring in user_agent:
                self.participant.vars['is_mobile'] = True
        return self.participant.vars['is_mobile']


page_sequence = [
    TestMobile
]
