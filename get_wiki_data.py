import sys
import wikipedia

class Wiki:
    def __init__(self, title):
        self.title = title
        self.page = wikipedia.page(title)
    
    def getLinks(self):
        self.links = self.page.links
        return self.links
    
    def getSummary(self):
        self.summary = self.page.summary
        return self.summary

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print ('Usage: python3 wikiText.py <topic>')
        sys.exit(0)
    title = sys.argv[1]

    summary = Wiki(title).getSummary()
