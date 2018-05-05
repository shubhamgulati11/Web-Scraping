import urllib.request
from bs4 import BeautifulSoup

def amazon_scrap(max_page,search):
    page=1
    while page <= max_page:
        url = "https://www.ebay.in/sch/i.html?_from=R40&_sacat=0&_nkw="+search+"&_pgn="+str(page)+"&_skc=50&rt=nc";
        code = urllib.request.urlopen(url);
        html = code.read();
        soup = BeautifulSoup(html,"html.parser");
        for link in soup.findAll('a',{'class':'vip'}):
            title=link.get('title');
            href = link.get('href');
            print(title);
            print(href);

        page+=1;

amazon_scrap(2,'bag');