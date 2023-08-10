from google_play_scraper import app
from google_play_scraper import Sort, reviews_all, reviews
import pandas as pd
import numpy as np

package_names = [
    'com.moez.QKSMS',
    'com.textra',
    'com.google.android.apps.messaging',
    'xyz.klinker.messenger',
    'com.calea.echo',
    'com.p1.chompsms',
    'org.thoughtcrime.securesms',
    'com.whatsapp',
    'com.viber.voip',
    'com.discord',
    'com.Slack'
]

all_reviews = []

for name in package_names:

    review, continuation_token = reviews(
    name,
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    count = 5000
    )
    all_reviews.append(review)

ctr = 0
for review in all_reviews:
    df = pd.DataFrame(np.array(review), columns=['review'])
    df = df.join(pd.DataFrame(df.pop('review').tolist()))
    df.to_csv(f'{package_names[ctr]}.csv',encoding='utf-8')
    ctr += 1
