from xchk import contentviews as basecv
from xchk.courses import Course
from .contentviews import *

course = Course('git','Git',[(GitInitView,[WhatIsGitView]),(WhatIsGitView,[basecv.ImpossibleNodeView])],"git@github.com:v-nys/git-modeloplossingen.git")
