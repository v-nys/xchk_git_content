from xchk.contentviews import ContentView
from xchk.strats import *

class WhatIsGitView(ContentView):
     
    _accepting = ConjunctiveCheck([FileExistsCheck(),RegexCheck()])
    uid = 'what_is_git_1'
    template = 'checkerapp/what_is_git.html'
    strat = Strategy(refusing_check=DisjunctiveCheck([
                                      Negation(FileExistsCheck()),
                                      RegexCheck(model_name='incorrect_lang'),
                                      Negation(RegexCheck())]),
                     accepting_check=_accepting)
