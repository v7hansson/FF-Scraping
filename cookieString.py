
# Paste your cookie string here
cookie_string = ""

# Dict to store cookies
cookies = {}

# Loop through each cookie
for cookie in cookie_string.split('; '):
    # Split cookie into name and value
    cookie_parts = cookie.split('=')
    cookies[cookie_parts[0]] = cookie_parts[1]