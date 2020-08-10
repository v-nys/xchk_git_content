from xchk_core.contentviews import ContentView
from xchk_core.strats import *
from xchk_regex_strategies.strats import RegexCheck
from .strats import MatchesIncorrectLanguageCheck

class WhatIsGitView(ContentView):
     
    _accepting = RegexCheck()
    uid = 'what_is_git_1'
    template = 'xchk_git_content/what_is_git.html'
    title = 'Wat is Git?'
    strat = Strategy(refusing_check=DisjunctiveCheck([
                                      Negation(FileExistsCheck()),
                                      MatchesIncorrectLanguageCheck(),
                                      Negation(RegexCheck())]),
                     accepting_check=_accepting)

class GitInitView(ContentView):

    uid = 'start_git_init_1'
    template = 'xchk_git_content/start_git_init.html'
    title = 'Een repo maken van een gewone map: git init'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))

class GitStagesView(ContentView):

    uid = 'git_stages_1'
    template = 'xchk_git_content/git_stages.html'
    title = 'Fasen van data in Git'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))

class GitStageChangesView(ContentView):

    uid = 'git_stage_changes_1'
    template = 'xchk_git_content/git_stage_changes.html'
    title = 'Data van fase veranderen'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))

class GitRemotesConceptView(ContentView):

    uid = 'git_remotes_concept_1'
    template = 'xchk_git_content/git_remotes_concept.html'
    title = 'Remotes: gekende kopieën van jouw repository'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))

class GitIgnoreConceptView(ContentView):

    uid = 'gitignore_concept_1'
    template = 'xchk_git_content/gitignore_concept.html'
    title = 'Bestanden uitsluiten van versiebeheer: .gitignore'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))

class GitStatusView(ContentView):

    uid = 'git_status_1'
    template = 'xchk_git_content/git_status.html'
    title = 'Kijken in welke fase je data zich bevindt: git status'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))

class GitPushView(ContentView):

    uid = 'git_push_1'
    template = 'xchk_git_content/git_push.html'
    title = 'Data naar een remote versturen: git push'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))

class GitAddRemoteView(ContentView):

    uid = 'git_add_remote_1'
    template = 'xchk_git_content/git_add_remote.html'
    title = 'Een nieuwe remote toevoegen'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))

class GitStatusAndGitIgnoreView(ContentView):

    uid = 'git_status_and_gitignore_1'
    template = 'xchk_git_content/git_status_and_gitignore.html'
    title = 'Het effect van .gitignore op git status'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))
    
class GitCloneView(ContentView):

    uid = 'git_clone_1'
    template = 'xchk_git_content/git_clone.html'
    title = 'Een lokale kopie van een bestaande repo maken: git clone'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))

class GitPullBasicsView(ContentView):

    uid = 'git_pull_basics_1'
    template = 'xchk_git_content/git_pull.html'
    title = 'Wijzigingen op een remote opnemen in je eigen kopie: git pull'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))
    
class GitLogView(ContentView):

    uid = 'git_log_1'
    template = 'xchk_git_content/git_log.html'
    title = 'Een overzicht van je geschiedenis: git log'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))
