from xchk.contentviews import ContentView
from xchk.strats import *

class WhatIsGitView(ContentView):
     
    _accepting = ConjunctiveCheck([FileExistsCheck(),RegexCheck()])
    uid = 'what_is_git_1'
    template = 'xchk_git_content/what_is_git.html'
    strat = Strategy(refusing_check=DisjunctiveCheck([
                                      Negation(FileExistsCheck()),
                                      RegexCheck(model_name='incorrect_lang'),
                                      Negation(RegexCheck())]),
                     accepting_check=_accepting)

class GitInitView(ContentView):

    uid = 'start_git_init_1'
    template = 'xchk_git_content/start_git_init.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))

class GitStagesView(ContentView):

    uid = 'git_stages_1'
    template = 'xchk_git_content/git_stages.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))
