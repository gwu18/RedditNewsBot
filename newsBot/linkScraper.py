from newspaper import Article



# returns article title
def getTitle(submissionUrl):
    article = Article(submissionUrl, language="en") # en for English
    article.download()
    article.parse()
    return article.title


# returns authors (in array)
def getAuthors(submissionUrl):
    article = Article(submissionUrl, language="en") # en for English
    article.download()
    article.parse()
    return article.authors

# returns publish date (in dateTime)
# datetime.datetime(2013, 12, 30, 0, 0)
def getPubDate(submissionUrl):
    article = Article(submissionUrl, language="en") # en for English
    article.download()
    article.parse()
    return article.publish_date

# returns article summary
def getSummary(submissionUrl):
    article = Article(submissionUrl, language="en") # en for English
    article.download()
    article.parse()
    return article.summary

