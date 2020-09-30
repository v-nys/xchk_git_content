import regex
from xchk_core.contentviews import ContentView
from xchk_core.strats import *
from xchk_regex_strategies.strats import RegexCheck, UnhelpfulRegexCheck
from xchk_multiple_choice_strategies.strats import MultipleChoiceFormatCheck, MultipleChoiceAnswerCheck

class WhatIsGitView(ContentView):
     
    uid = 'what_is_git_1'
    template = 'xchk_git_content/what_is_git.html'
    title = 'Wat is Git?'
    _accepted_regex_text = r"""
    ^                                           # begin string
    \s*                                         # optional whitespace
    https://(www\.)?git\-scm\.com/book/nl(/v2)? # link
    \s*                                         # optional whitespace
    $                                           # end string
    """
    _incorrect_lang_regex_text = r"""
    ^                                      # begin string
    \s*                                    # optional whitespace
    https://(www\.)?git\-scm\.com/book/    # base link
    ([^n].+|n[^l].*|nl[^/].+)              # anything but 'nl'
    (/v2)?                                 # rest link
    \s*                                    # optional whitespace
    $
    """
    _incorrect_lang_regex = regex.compile(_incorrect_lang_regex_text,flags=regex.VERBOSE)
    _accepted_regex = regex.compile(_accepted_regex_text,flags=regex.VERBOSE)
    _accepting = RegexCheck(_accepted_regex,pattern_description='de link voor de Nederlandstalige documentatie')
    strat = Strategy(refusing_check=DisjunctiveCheck([
                                      Negation(FileExistsCheck()),
                                      RegexCheck(_incorrect_lang_regex,pattern_description='een andere taal dan het Nederlands'),
                                      Negation(_accepting)]),
                     accepting_check=TrueCheck())

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
    _accepting = RegexCheck(_accepted_regex,pattern_description='een modeloplossing')
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
    _accepting = RegexCheck(_accepted_regex,pattern_description='een modeloplossing')
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
    _accepting = RegexCheck(_accepted_regex,pattern_description='de gevraagde tekst')
    strat = Strategy(refusing_check=DisjunctiveCheck([Negation(FileExistsCheck()),Negation(_accepting)]),accepting_check=_accepting)

class GitRemotesConceptView(ContentView):

    uid = 'git_remotes_concept_1'
    template = 'xchk_git_content/git_remotes_concept.html'
    title = 'Remotes: gekende kopieën van jouw repository'
    _multiple_choice_answer_check = MultipleChoiceAnswerCheck(filename=None,mc_data=[
                   ("Ik kopieer via Windows explorer mijn volledige git repository van PC A naar PC B. Welke repository is remote van welke andere repository?",
                    ("alleen A is remote van B",False,"Weet B van waar de data oorspronkelijk afkomstig is?"),
                    ("alleen B is remote van A",False,"Weet A wat er verder met zijn data gebeurd is?"),
                    ("A en B zijn remotes van elkaar",False,"Weet A wat er verder met zijn data gebeurd is? Weet B van waar de data oorspronkelijk afkomstig is?"),
                    ("geen van beide is remote van de ander",True,"Weet A wat er verder met zijn data gebeurd is? Weet B van waar de data oorspronkelijk afkomstig is?")),
                   ("Mogen Git repositories naar elkaar verwijzen zoals in de tekening?",
                    ("Ja",True,"Wordt er ergens één naam gebruikt om naar twee verschillende remotes te verwijzen? Zijn er namen met een speciale betekenis die zorgen dat er iets mis is op de tekening?"),
                    ('Nee, want B en C mogen niet allebei de naam "origin" gebruiken',False,"Weten B en C van elkaar welke remotes ze hebben?"),
                    ("Nee, want als C naar A verwijst, mag A niet terug verwijzen naar C",False,"Lees de omschrijving van een remote. Staat er iets dat zegt dat verwijzingen maar in één richting mogen gaan?"),
                    ("Nee, want B mag niet naar A en C verwijzen",False,"Is het zo dat je maar één remote mag hebben?"),
                    )])
    custom_data = {'rendered_mc_qs': _multiple_choice_answer_check.render()}
    strat = Strategy(refusing_check=Negation(ConjunctiveCheck([FileExistsCheck(),MultipleChoiceFormatCheck(),_multiple_choice_answer_check])),accepting_check=TrueCheck())

class GitIgnoreConceptView(ContentView):

    uid = 'gitignore_concept_1'
    template = 'xchk_git_content/gitignore_concept.html'
    title = 'Bestanden uitsluiten van versiebeheer: .gitignore'
    _accepted_regex_text = r"""
    ^
    \s*
    cache/?
    \n
    \*\.pdf
    \n
    1C\.md
    \s*
    $
    """
    _accepted_regex = regex.compile(_accepted_regex_text,flags=regex.VERBOSE)
    _accepting = RegexCheck(_accepted_regex,pattern_description='de geschikte inhoud van .gitignore file')
    strat = Strategy(refusing_check=DisjunctiveCheck([Negation(FileExistsCheck()),Negation(_accepting)]),accepting_check=_accepting)

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
    _accepted_regex = regex.compile(_accepted_regex_text,flags=regex.VERBOSE | regex.DOTALL)
    _accepting = UnhelpfulRegexCheck(_accepted_regex,pattern_description='het gevraagde overzicht van de wijzigingen')
    strat = Strategy(refusing_check=DisjunctiveCheck([Negation(FileExistsCheck()),Negation(_accepting)]),accepting_check=_accepting)

   
class GitPullBasicsView(ContentView):

    uid = 'git_pull_basics_1'
    template = 'xchk_git_content/git_pull.html'
    title = 'Wijzigingen op een remote opnemen in je eigen kopie: git pull'
    _accepted_regex_text = r"""
    ^                       # begin string
    \s*                     # optionele whitespace
    [Ff]ast[\ \-][Ff]orward # de essentie; schrijfwijze kan misschien verschillen in andere versies
    \s*                     # optionele whitespace
    $                       # einde string
    """
    _accepted_regex = regex.compile(_accepted_regex_text,flags=regex.VERBOSE | regex.DOTALL)
    _accepting = RegexCheck(_accepted_regex,pattern_description='de regel NA de regel die begint met "Updating"')
    strat = Strategy(refusing_check=DisjunctiveCheck([Negation(FileExistsCheck()),Negation(_accepting)]),accepting_check=_accepting)

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
    _accepted_regex = regex.compile(_accepted_regex_text,flags=regex.VERBOSE | regex.DOTALL)
    _accepting = RegexCheck(_accepted_regex,pattern_description='het gevraagde overzicht van de wijzigingen')
    strat = Strategy(refusing_check=DisjunctiveCheck([Negation(FileExistsCheck()),Negation(_accepting)]),accepting_check=_accepting)

class GitPushView(ContentView):

    uid = 'git_push_1'
    template = 'xchk_git_content/git_push.html'
    title = 'Data naar een remote versturen: git push'
    strat = Strategy(refusing_check=Negation(FileExistsCheck()),accepting_check=FileExistsCheck())

class GitStatusAndGitIgnoreView(ContentView):

    uid = 'git_status_and_gitignore_1'
    template = 'xchk_git_content/git_status_and_gitignore.html'
    title = 'Het effect van .gitignore op git status'
    strat = Strategy(refusing_check=Negation(TrueCheck()),accepting_check=TrueCheck())
 
class GitAddRemoteView(ContentView):

    uid = 'git_add_remote_1'
    template = 'xchk_git_content/git_add_remote.html'
    title = 'Een nieuwe remote toevoegen'
    strat = Strategy(refusing_check=Negation(TrueCheck()),accepting_check=TrueCheck())
