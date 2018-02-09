import re
import feedparser
import config

# Returns title and dictionary of word counts for an RSS feed
def getwordcounts(url):
    # Parse the feed
    d = feedparser.parse(url)
    wc = {}

    # Loop over all the entries
    for e in d.entries:
        if 'summary' in e: 
            summary = e.summary
        else: 
            summary = e.description

        # Extract a list of words
        words = getwords(e.title + " " + summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1

        return d.feed.title, wc

def getwords(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # Split word by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']

# alt main
def main():
    apcount = {}
    wordcounts = {}
    feedlist = []
    # either add a try or a with probably with
    with open ('feedlist.txt', 'r') as flfile:
        for feedurl in flfile:
            feedlist.append(feedurl)
            try:
                title, wc = getwordcounts(feedurl)
            except ValueError as e:
                print(e, "was bad")
            except:
                print('make a better error message')
            wordcounts[title] = wc
            for word, count in wc.items():
                apcount.setdefault(word, 0)
                if count > 1:
                    apcount[word] += 1

    wordlist = []
    # why bc? 
    for w, bc in apcount.items():
        frac = float(bc) / len(feedlist)
        # Mess with these parameters, it gives pretty sparse data
        if frac > 0.1 and frac < 0.5:
            wordlist.append(w)

    with open('blogdata1.txt', 'w') as out:
        out.write('Blog')
        for word in wordlist:
            out.write('\t%s' % word)
        out.write('\n')
        for blog, wc in wordcounts.items():
            # deal with unicode,,, ignore??
            # blog = blog.encode('ascii', 'ignore) 
            out.write(blog)
            for word in wordlist:
                if word in wc: 
                    out.write('\t%d' % wc[word])
                else:
                    out.write('\t0')
            out.write('\n')
    print('Done!')

if __name__ == "__main__":
    main()


