Hacker News in neovim
=====================

install:

copy hacker.py into ~/.nvim/rplugin/python/hacker.py

open neovim

run :HackerNews to open the top 30 hacker news stories in a new vim buffer. The
buffer will take a second to open, but the stories are populated in the
background and the buffer will open when it is ready.

In that new buffer, run :HackerOpen to open the selected story
