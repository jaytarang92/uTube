import urllib2
import sys
import fnmatch


class Youtube:

    links = []

    def search(self, search_string):
        search_string = search_string.replace(" ", "+")
        youtube = urllib2.urlopen("http://youtube.com/results?search_query=" + search_string)
        for page in youtube:
            tags = page.replace(' ', '').split('"')
            for tag in tags:
                if fnmatch.fnmatch(tag, "/watch?*"):
                    tag = tag.replace("/watch?v=", "")
                    self.links.append("http://youtube.com/embed/" + tag + "?&autoplay=0&loop=1&rel=0&showinfo=0&color=white&iv_load_policy=3&playlist="+tag)
        self.links = list(set(self.links))
        return self.links
