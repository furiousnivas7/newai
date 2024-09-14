from utils.scraping import scrape_website
from utils.data_preprocessing import clean_text

def compare_manifestos(url1, url2):
    manifesto1 = clean_text(scrape_website(url1))
    manifesto2 = clean_text(scrape_website(url2))

    # Simple keyword matching (Can be improved using embeddings)
    comparison_result = {
        "economy": {
            "candidate1": manifesto1.get("economy", "Not mentioned"),
            "candidate2": manifesto2.get("economy", "Not mentioned"),
        },
        "healthcare": {
            "candidate1": manifesto1.get("healthcare", "Not mentioned"),
            "candidate2": manifesto2.get("healthcare", "Not mentioned"),
        }
    }
    
    return comparison_result
