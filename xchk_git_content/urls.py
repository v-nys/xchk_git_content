from django.urls import path

from . import contentviews

urlpatterns = [
    path('what_is_git_1', contentviews.WhatIsGitView.as_view(), name=f'{contentviews.WhatIsGitView.uid}_view'),
    path('start_git_init_1', contentviews.GitInitView.as_view(), name=f'{contentviews.WhatIsGitView.uid}_view'),
]
