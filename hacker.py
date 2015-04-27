import neovim
from hackernews import HackerNews
import webbrowser

@neovim.plugin
class Hacker(object):
    def __init__(self, vim):
        self.vim = vim
        self.hn = HackerNews()
        self.urls = None


    @neovim.command("Test")
    def test(self):
        self.vim.command("vsplit")

    @neovim.command('HackerNews')
    def fill_buffer(self):

        stories = []
        urls = {}
        for story in self.hn.top_stories()[0:30]:
            item = self.hn.get_item(story)
            stories.append(item.title)
            urls[item.title] = item.url

        self.vim.command("split HackerNews")
        self.vim.command("buffer HackerNews")
        self.vim.command("set buftype=nofile")
        self.vim.command("set bufhidden=hide")
        self.vim.command("setlocal noswapfile")
        self.vim.current.buffer[:] = stories
        self.urls = urls

    @neovim.command('HackerOpen')
    def autocmd_handler(self):
        url = self.urls[self.vim.current.line]
        webbrowser.open_new_tab(url)
