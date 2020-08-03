import os
import regex
from xchk_core.strats import FileExistsCheck, OutcomeAnalysis, OutcomeComponent
from xchk_regex_strategies.strats import RegexCheck

class MatchesIncorrectLanguageCheck(RegexCheck):

    def __init__(self):
        super().__init__(None,None,'incorrect_lang')

    def instructions(self,exercise_name):
        return [f'Je bestand met naam {self.entry(exercise_name)} matcht met een andere taal dan Nederlands']
