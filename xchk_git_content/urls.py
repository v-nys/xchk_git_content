import inspect
import sys
from django.urls import path

from . import contentviews
from xchk_core.contentviews import ContentView

# TODO: move to core?
def is_content_view(e):
    return inspect.isclass(e) and issubclass(e,ContentView)

urlpatterns = [path(cv[1].uid, cv[1].as_view(), name=f'{cv[1].uid}_view') for cv in inspect.getmembers(sys.modules['xchk_git_content.contentviews'],inspect.isclass)]
