import regex
from xchk_core.contentviews import ContentView
from xchk_core.strats import *
from xchk_regex_strategies.strats import RegexCheck, UnhelpfulRegexCheck

class WhatIsGitView(ContentView):
     
    uid = 'what_is_git_1'
    template = 'xchk_git_content/what_is_git.html'
    title = 'Wat is Git?'
    _accepted_regex_text = r"""
    ^                                # begin string
    \s*                              # optional whitespace
    https://git\-scm\.com/book/nl/v2 # link
    \s*                              # optional whitespace
    $                                # end string
    """
    _incorrect_lang_regex_text = r"""
    ^                           # begin string
    \s*                         # optional whitespace
    https://git\-scm\.com/book/ # base link
    ([^n].+|n[^l].*|nl[^/].+)   # anything but 'nl'
    /v2                         # rest link
    \s*                         # optional whitespace
    $
    """
    _incorrect_lang_regex = regex.compile(_incorrect_lang_regex_text,flags=regex.VERBOSE)
    _accepted_regex = regex.compile(_accepted_regex_text,flags=regex.VERBOSE)
    _accepting = RegexCheck(_accepted_regex,pattern_description='de link voor de Nederlandstalige documentatie')
    strat = Strategy(refusing_check=DisjunctiveCheck([
                                      Negation(FileExistsCheck()),
                                      RegexCheck(_incorrect_lang_regex,pattern_description='een andere taal dan het Nederlands'),
                                      Negation(_accepting)]),
                     accepting_check=_accepting)

class GitInitView(ContentView):

    uid = 'start_git_init_1'
    template = 'xchk_git_content/start_git_init.html'
    title = 'Een repo maken van een gewone map: git init'
    _accepted_regex_text = r"""
    ^         # begin string
    \s*       # optionele whitespace
    [rR]epo   # letterlijk eerste antwoord
    \s*       # optionele whitespace
    git\ init # tweede antwoord
    \s*       # optionele whitespace
    \.git     # derde antwoord
    \s*       # optionele whitespace
    $         # einde string
    """
    _accepted_regex = regex.compile(_accepted_regex_text,flags=regex.VERBOSE)
    _accepting = RegexCheck(_accepted_regex_text,pattern_description='een modeloplossing')
    strat = Strategy(refusing_check=DisjunctiveCheck([Negation(FileExistsCheck()),Negation(_accepting)]),accepting_check=_accepting)

class GitStagesView(ContentView):

    uid = 'git_stages_1'
    template = 'xchk_git_content/git_stages.html'
    title = 'Fasen van data in Git'
    _accepted_regex_text = r"""
    ^                   # begin string
    \s*                 # optionele whitespace
    [sS]taging\ [aA]rea # eerste antwoord, deels hoofdletterongevoelig
    \s*                 # optionele whitespace
    [nN]een?            # tweede antwoord, deels hoofdletterongevoelig
    \s*                 # optionele whitespace
    $                   # einde string
    """
    _accepted_regex = regex.compile(_accepted_regex_text,flags=regex.VERBOSE)
    _accepting = RegexCheck(_accepted_regex_text,pattern_description='een modeloplossing')
    strat = Strategy(refusing_check=DisjunctiveCheck([Negation(FileExistsCheck()),Negation(_accepting)]),accepting_check=_accepting)

class GitStageChangesView(ContentView):

    uid = 'git_stage_changes_1'
    template = 'xchk_git_content/git_stage_changes.html'
    title = 'Data van fase veranderen'
    _accepted_regex_text = r"""
    ^                                           # begin string
    \s*                                         # optionele whitespace
    de\ kat\ krabt\ de\ krollen\ van\ de\ trap! # verwachte inhoud
    \s*                                         # optionele whitespace
    $                                           # einde string
    """
    _accepted_regex = regex.compile(_accepted_regex_text,flags=regex.VERBOSE)
    _accepting = RegexCheck(_accepted_regex_text,pattern_description='de gevraagde tekst')
    strat = Strategy(refusing_check=DisjunctiveCheck([Negation(FileExistsCheck()),Negation(_accepting)]),accepting_check=_accepting)

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
    # benadering omdat dit voor verschillende versies wat anders kan zijn
    _accepted_regex_text = r"""
    ^                                           # begin string
    .*
    [cC]hanges\ to\ be\ committed:
    .*
    git_status_1
    .*
    [cC]hanges\ not\ staged\ for\ commit:
    .*
    git_status_1
    .*
    $                                           # einde string
    """
    _accepted_regex = regex.compile(_accepted_regex_text,flags=regex.VERBOSE & regex.DOTALL)
    _accepting = UnhelpfulRegexCheck(_accepted_regex_text,pattern_description='het gevraagde overzicht van de wijzigingen')
    strat = Strategy(refusing_check=DisjunctiveCheck([Negation(FileExistsCheck()),Negation(_accepting)]),accepting_check=_accepting)

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
    strat = Strategy(refusing_check=Negation(TrueCheck()),accepting_check=TrueCheck())
    
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
    _accepted_regex_text = r"""
    ^                     # begin string
    \s*                   # optionele whitespace
    [cC]ommit\ [hH]ash    # eerste antwoord
    \s*                   # optionele whitespace
    git\ commit           # tweede antwoord
    \s*                   # optionele whitespace
    [cC]ommit\ [mM]essage # eerste antwoord
    \s*                   # optionele whitespace
    $                     # einde string
    """
    _accepted_regex = regex.compile(_accepted_regex_text,flags=regex.VERBOSE & regex.DOTALL)
    _accepting = RegexCheck(_accepted_regex_text,pattern_description='het gevraagde overzicht van de wijzigingen')
    strat = Strategy(refusing_check=DisjunctiveCheck([Negation(FileExistsCheck()),Negation(_accepting)]),accepting_check=_accepting)
