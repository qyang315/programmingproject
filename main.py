import praw

reddit = praw.Reddit( client_id= '1RfADhDIiV5ezcB5vl8qcA',
                      client_secret= '14LB2fUwfcHXARIPaWKEifsnbun-Pw',
                      password= '????????',
                      user_agent= 'web:memegenerator.meme:v1.2.3(by u/qiqi-99)',
                      username= 'qiqi-99' )

def check_image(urllink):
    ext = urllink[-4:]
    if ext == '.jpg' or ext == '.png':
        return True

    return False

def get_meme(sub,count):
    sub_reddit = reddit.subreddit(sub)
    hot_meme = sub_reddit.hot(limit=count)
    result =[]
    for submissions in hot_meme:
        temp = {"Title": submissions.title,
                  "Url": submissions.url,
                  "Upvotes": submissions.ups,
                  "Downvotes": submissions.downs,
                  "Redditurl": submissions.shortlink,
                  "Subreddit": sub
                  }
        result.append(temp)

    return result
