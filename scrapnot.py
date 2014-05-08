# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# This is a scrapbook for exploring some python ideas and modules that i plan to take into other notebooks.

# <codecell>

import markdown

# <codecell>

markdown.to_html_string('test hello')

# <codecell>

html = markdown.markdown('testing123!')

# <codecell>

print html

# <codecell>

conv = markdown.markdownFromFile

