from django.urls import path

from . import contentviews

urlpatterns = [
    path('what_is_git_1', contentviews.WhatIsGitView.as_view(), name=f'{contentviews.WhatIsGitView.uid}_view'),
    path('start_git_init_1', contentviews.GitInitView.as_view(), name=f'{contentviews.GitInitView.uid}_view'),
    path('git_stages_1', contentviews.GitStagesView.as_view(), name=f'{contentviews.GitStagesView.uid}_view'),
]
