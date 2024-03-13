cookie_string = ""

# Split the cookie string into individual cookies
cookies_list = cookie_string.split('; ')

# Create an empty dictionary to store cookies
cookies = {}

# Loop through each cookie in the list
for cookie in cookies_list:
    # Split the cookie into name and value
    cookie_parts = cookie.split('=')
    # The first part is the cookie name, and the second part is the cookie value
    cookies[cookie_parts[0]] = cookie_parts[1]

# Print the dictionary of cookies
# print(cookies)