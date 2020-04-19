import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    print(transition_model(corpus,"1.html",DAMPING))
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    #raise NotImplementedError
    d = list()
    text = str(page)
    d = corpus[text]
    cap = random.sample(d,1)[0]
    #print("cap"+str(cap))
    capRandom = random.choice(list(corpus.keys()))#any random page
    weight = [DAMPING, 1-DAMPING]
    pages = [cap,capRandom]
    #print(pages)
    if pages[0] == None:
        return pages[1]
    elif pages[1] == None:
        return pages[0]
    else:
        temp = random.choices(pages,weight)
        return temp[0]



def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by saprint(f"PageRank Results from Iteration")
    # for page in sorted(ranks):
    #     print(f"  {page}: {ranks[page]:.4f}")mpling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    #raise NotImplementedError
    value = dict()
    store = list()
    allPages = list(corpus.keys())
    page = random.choice(allPages)
    for i in range(n):
        page = transition_model(corpus,page,DAMPING)
        store.append(page)

    for i in range(len(allPages)):
        page = allPages[i]
        val = store.count(page)/(n*1.0)
        value.update({page: val})

    return value


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    #raise NotImplementedError
    value = dict()
    d = list()
    d = list(corpus.keys())
    n = len(d)
    prob = 1.0/(n*1.0)
    #print(d)
    for i in range(len(d)):
        value.update({d[i]:prob})
    #print(value)
    new_corpus = dict()#takes all the input nodes
    for i in range(n):
        temp = list()
        page = d[i]
        for j in range(n):
            key = d[j]
            temp1 = list(corpus[key])
            for k in range(len(temp1)):
                if temp1[k] == page:
                    temp.append(key)
        new_corpus.update({page: temp})
    
    #print(new_corpus)
    for i in range(5000):
        for j in range(n):
            pageJ = d[j]
            pageRankJ = (1-damping_factor)/(n*1.0)
            length = (new_corpus[pageJ])
            for pages in length:
                pageRankJ += damping_factor*(value[pages]/(1.0*len(corpus[pages])))
            value[pageJ] = pageRankJ
    #print(value)
    return value

if __name__ == "__main__":
    main()
