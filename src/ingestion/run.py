from scraper import scrape
from loaders import load_documents
from processing.cleaner import clean_text

def run():
    docs = scrape()
    raw = load_documents(docs)
    clean = clean_text(raw)
    return clean