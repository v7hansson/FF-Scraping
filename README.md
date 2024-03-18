# Scraping NFL.com Fantasy History

## What does this project do?

1. Scrapes entire fantasy league history from NFL.com. It exports all standings and games as CSV files in `./output`
2. Aggregates standings into a single CSV file like [this](https://ibb.co/QvYprGD).
3. Iterate through all games to find biggest blowouts and narrowest victories.

## How to run this:

1. `git clone https://github.com/PeteTheHeat/FF-Scraping`
2. In `constants.py`, update with your league ID and start/end years.
3. In `cookieString.py`, update cookie string with an active NFL.com cookie. You can find this by inspecting a request in chrome dev tools ([screenshot](https://ibb.co/7bk4fmN)).
4. `python scrapeStandings.py` will scrape all standings. `python aggregateStandings.py` will aggregate into 1 CSV.
5. `python scrapeGamecenter.py` will scrape all games. `python analyzeGamecenter.py` will find biggest blowouts and narrowest margins of victory.

## Known Issues:

1. If multiple team managers have the same name, their results will be aggregated together.
2. The script assumes top half of the league makes playoffs.

Inspiration reddit thread [here](https://www.reddit.com/r/fantasyfootball/comments/jll2xs/i_wrote_a_script_to_scrape_nflcom_fantasy_league/).
