import config

def getwordcounts(d):
    # Parse the feed
    wc = {}
    
    # Extract a list of words
    words = getwords(d['user'] + " " + d['title'])
    print(words)
    for word in words:
        wc.setdefault(word, 0)
        wc[word] += 1

    return d['user'], wc

def getwords(txt):
    # Split word by all non-alpha characters
    words = txt.split()

    # Convert to lowercase
    return [word.lower() for word in words if word != '']

def main():
    apcount = {}
    wordcounts = {}
    feedlist = []

    users = config.redditusers
    titles = config.titles
    data = [{'title': titles[i], 'user': users[i]}
            for i in range(len(users))]
    for d in data:
        #feedlist.append(feedurl)
        try:
            user, wc = getwordcounts(d)
        except:
            print("fail")
        #wordcounts[title] = wc
        #for word, count in wc.items():
        #    apcount.setdefault(word, 0)
        #    if count > 1:
        #        apcount[word] += 1

    #wordlist = []
    ## why bc? 
    #for w, bc in apcount.items():
    #    frac = float(bc) / len(feedlist)
    #    # Mess with these parameters, it gives pretty sparse data
    #    if frac > 0.1 and frac < 0.5:
    #        wordlist.append(w)

    #with open('blogdata1.txt', 'w') as out:
    #    out.write('Blog')
    #    for word in wordlist:
    #        out.write('\t%s' % word)
    #    out.write('\n')
    #    for blog, wc in wordcounts.items():
    #        # deal with unicode,,, ignore??
    #        # blog = blog.encode('ascii', 'ignore) 
    #        out.write(blog)
    #        for word in wordlist:
    #            if word in wc: 
    #                out.write('\t%d' % wc[word])
    #            else:
    #                out.write('\t0')
    #        out.write('\n')
    #print('Done!')

if __name__ == '__main__':
    main()
main()
