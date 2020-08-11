import inspect
from django.urls import path

from . import contentviews
from xchk_core.contentviews import ContentView

# TODO: move to core?
def is_content_view(e):
    return inspect.isclass(e) and issubclass(e,ContentView)

urlpatterns = [path(cv.uid, cv.as_view(), name=f'{cv.uid}_view') for cv in inspect.getmember(sys.modules['xchk_git_content.contentviews'],inspect.isclass)]
