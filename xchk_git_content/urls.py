from django.urls import path

from . import contentviews

urlpatterns = [
    path('what_is_git_1', contentviews.WhatIsGitView.as_view(), name=f'{contentviews.WhatIsGitView.uid}_view'),
]
