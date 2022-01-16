import json

import requests
import pandas as pd

def load_picture(url):
    r = requests.get(url, stream=True)
    r.raw.decode_content=True
    #print(r.status_code)
    return r.raw

def iiif_manifest(urn):
    r = requests.get("https://api.nb.no/catalog/v1/iiif/{urn}/manifest".format(urn=urn))
    return r.json()

def mods(urn):
    r = requests.get("https://api.nb.no:443/catalog/v1/metadata/{id}/mods".format(urn=urn))
    return r.json()

def super_search(term, number=50, page=0, mediatype='bilder'):
    """Søk etter term og få ut json"""
    number = min(number, 50)
    if term == '':
        r = requests.get(
            "https://api.nb.no:443/catalog/v1/items", 
             params = { 
                 'filter':'mediatype:{mediatype}'.format(mediatype=mediatype), 
                 'page':page, 
                 'size':number
             }
        )
    else:        
        r = requests.get(
            "https://api.nb.no:443/catalog/v1/items", 
             params = {
                 'q':term, 
                 'filter':'mediatype:{mediatype}'.format(mediatype=mediatype), 
                 'page':page, 
                 'size':number
             }
        )
    return r.json()

def total_search(size=50, page=0):
    """Finn de første antallet = 'size' fra side 'page' og få ut json"""
    size = min(size, 50)
    r = requests.get(
        "https://api.nb.no:443/catalog/v1/items", 
         params = {
             'filter':'mediatype:bilder', 
             'page':page, 
             'size':size
         }
    )
    return r.json()


def get_df(frases, title='aftenposten'):
    import requests
    querystring = " + ".join(['"'+frase+'"' for frase in frases])
    query = {
        'q':querystring,
        'size':1,
        'aggs':'year',
        #'filter':'mediatype:{mt}'.format(mt=media),
        'filter':'title:{title}'.format(title=title)
    }
    r = requests.get("https://api.nb.no/catalog/v1/items", params = query)
    aggs = r.json()['_embedded']['aggregations'][0]['buckets']
    return {x['key']:x['count'] for x in aggs}

def get_json(frases, mediatype='aviser'):

    querystring = " + ".join(['"'+frase+'"' for frase in frases])
    query = {
        'q':querystring,
        'size':1,
        'snippets':mediatype,
        'aggs':'year',
        
#        'filter':'mediatype:{mt}'.format(mt=mediatype),
        'searchType':'FULL_TEXT_SEARCH'
        #'filter':'title:{title}'.format(title=title)
    }
    r = requests.get("https://api.nb.no/catalog/v1/items", params = query)
    aggs = r.json()
    return aggs

def get_data(frase, media='avis', title='jazznytt'):
    import requests
    query = {
        'q':'"'+frase+'""',
        'size':1,
        'aggs':'year',
        'filter':'mediatype:{mt}'.format(mt=media),
        'filter':'title:{title}'.format(title=title)
    }
    r = requests.get("https://api.nb.no/catalog/v1/items", params = query)
    return r.json()

def get_data_and(frases, title='aftenposten', media='avis'):
    import requests
    querystring = " + ".join(['"'+frase+'"' for frase in frases])
    print(querystring)
    query = {
        'q':querystring,
        'size':1,
        'aggs':'year',
        #'filter':'mediatype:{mt}'.format(mt=media),
        'filter':'title:{title}'.format(title=title)
    }
    r = requests.get("https://api.nb.no/catalog/v1/items", params = query)
    return r.json()

def get_df_pd(frase, media='bøker'):
    return pd.DataFrame.from_dict(get_df(frase, media=media ), orient='index').sort_index()


def get_konks(urn, phrase, window=1000, n = 1000):
    import requests
    querystring = '"'+ phrase +'"' 
    query = {
        'q':querystring,
        'fragments': n,
        'fragSize':window
       
    }
    r = requests.get("https://api.nb.no/catalog/v1/items/{urn}/contentfragments".format(urn=urn), params = query)
    res = r.json()
    results = []
    try:
        for x in res['contentFragments']:
            urn = x['pageid']
            hit = x['text']
            splits = hit.split('<em>')
            s2 = splits[1].split('</em>')
            before = splits[0]
            word = s2[0]
            after = s2[1]
            results.append({'urn': urn, 'before': before, 'word':word, 'after':after})
    except:
        True
    return results

def get_phrase_info(urn, phrase, window=1000, n = 1000):
    import requests
    querystring = '"'+ phrase +'"' 
    query = {
        'q':querystring,
       
    }
    r = requests.get("https://api.nb.no/catalog/v1/items/{urn}/contentfragments".format(urn=urn), params = query)
    res = r.json()
    return res

def get_all_konks(term, urns):
    konks = []
    for u in urns:
        konks += get_konks(u, term)
    return konks

def collocations_from_nb(word, corpus):
    """Get a concordance, and count the words in it. 
    Assume konks reside a dataframe with columns 'after' and 'before'"""
    concordance = nb.frame(get_all_konks(word, corpus))
    return nb.frame_sort(nb.frame(Counter(tokenize(' '.join(concordance['after'].values + concordance['before'].values))), word))

def count_from_conc(concordance):
    """From a concordance, count the words in it. 
    Assume konks reside a dataframe with columns 'after' and 'before'"""
    word = concordance['word'][0]
    return nb.frame_sort(
        nb.frame(
            Counter(
                tokenize(' '.join(concordance['after'].values + concordance['before'].values))
            ), 
            word
        )
    )
