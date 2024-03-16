# FF-Scraping

This was forked from https://github.com/sawyercole/FF-Scraping, and a few bugs were fixed.
Reddit thread here: https://www.reddit.com/r/fantasyfootball/comments/jll2xs/i_wrote_a_script_to_scrape_nflcom_fantasy_league/

## How to run this:

1. git clone
2. In constants.py, update with your league ID and start/end years
3. In cookieString.py, update cookie string with an active NFL.com cookie. You can find this by inspecting a request in chrome dev tools ![screenshot](https://ibb.co/7bk4fmN)
4. `python scrapeStandings.py` will scrape all standings. `python aggregateStandings.py` will aggregate into 1 CSV.
5. `python scrapeGamecenter.py` will scrape all games.
