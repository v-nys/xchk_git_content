import regex
from xchk_core.strats import *
from xchk_regex_strategies.strats import RegexCheck

class IncorrectURLOrLangCheck(CheckingPredicate):

    _accepted_regex_text = r"""
    ^                                   # begin string
    \s*                                 # optional whitespace
    https://git\-scm\.com/book/nl(/v2)? # link
    \s*                                 # optional whitespace
    $                                   # end string
    """
    _incorrect_lang_regex_text = r"""
    ^                           # begin string
    \s*                         # optional whitespace
    https://git\-scm\.com/book/ # base link
    ([^n].+|n[^l].*|nl[^/].+)   # anything but 'nl'
    (/v2)?                      # rest link
    \s*                         # optional whitespace
    $
    """
    _incorrect_lang_regex = regex.compile(_incorrect_lang_regex_text,flags=regex.VERBOSE)
    _accepted_regex = regex.compile(_accepted_regex_text,flags=regex.VERBOSE)
    _accepting = RegexCheck(_accepted_regex,pattern_description='de link voor de Nederlandstalige documentatie')
    _unsugared_check = DisjunctiveCheck([RegexCheck(_incorrect_lang_regex,pattern_description='een andere taal dan het Nederlands'),
                                         Negation(_accepting)])

    def instructions(self,exercise_name):
        return IncorrectURLOrLangCheck._unsugared_check.disjuncts[1].instructions(exercise_name)

    def negative_instructions(self,exercise_name):
        return IncorrectURLOrLangCheck._unsugared_check.disjuncts[1].negative_instructions(exercise_name)

    def check_submission(self,submission,student_path,desired_outcome,init_check_number,ancestor_has_alternatives,parent_is_negation=False,open=open):
        analysis = IncorrectURLOrLangCheck._unsugared_check.check_submission(submission,student_path,desired_outcome,init_check_number,ancestor_has_alternatives,parent_is_negation=parent_is_negation,open)
