from selenium import webdriver
import pandas as pd
import time

def search_and_capture(query, account_type="neutral"):
    """Capture search results for a given query and account type."""
    driver = webdriver.Chrome()
    driver.get(f"https://www.google.com/search?q={query}")
    time.sleep(3)
    results = driver.find_elements("css selector", "div.g")
    rankings = []
    for i, result in enumerate(results[:10]):
        try:
            title = result.find_element("css selector", "h3").text
            link = result.find_element("css selector", "a").get_attribute("href")
            rankings.append({
                "query": query,
                "rank": i+1,
                "title": title,
                "link": link,
                "account_type": account_type
            })
        except:
            continue
    driver.quit()
    return rankings

if __name__ == "__main__":
    conservative_results = search_and_capture("border security", "conservative")
    liberal_results = search_and_capture("border security", "liberal")
    df = pd.DataFrame(conservative_results + liberal_results)
    df.to_csv("search_results.csv", index=False)
    print("Results saved to search_results.csv")
