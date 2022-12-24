#Taken From 
#https://python.plainenglish.io/scrape-google-scholar-with-python-fc6898419305#8670
from parsel import Selector
import requests, json, re
def scrape_all_authors(author_name):
    params = {
        'view_op': 'search_authors', # author results
        'mauthors': author_name,      # search query
        'hl': 'en',                  # language of the search
        'astart': 0                  # page number
    }
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
        }
    data = []
    while True:
            html = requests.get('https://scholar.google.com/citations', params=params, headers=headers, timeout=30)
            soup = Selector(text=html.text)
            for author in soup.css('.gs_ai_chpr'):
                name = author.css('.gs_ai_name a').xpath('normalize-space()').get()
                link = f'https://scholar.google.com{author.css(".gs_ai_name a::attr(href)").get()}'
                affiliations = author.css('.gs_ai_aff').xpath('normalize-space()').get()
                email = author.css('.gs_ai_eml').xpath('normalize-space()').get()
                try:
                    cited_by = re.search(r'\d+', author.css('.gs_ai_cby::text').get()).group() # Cited by 17143 -> 17143
                except: cited_by = None
                data.append({
                    'name': name,
                    'link': link,
                    'affiliations': affiliations,
                    'email': email,
                    'cited_by': cited_by
                })
            # check if the next arrow button is active by checking 'onclick' attribute
            if soup.css('.gsc_pgn button.gs_btnPR::attr(onclick)').get():
                # extracting next page token and passing to 'after_author' query URL parameter
                params['after_author'] = re.search(r'after_author\\x3d(.*)\\x26', str(soup.css('.gsc_pgn button.gs_btnPR::attr(onclick)').get())).group(1)  # -> XB0HAMS9__8J
                params['astart'] += 10
            else:
                break
    print(json.dumps(data, indent=2, ensure_ascii=False))
    # Part of the output:

scrape_all_authors()