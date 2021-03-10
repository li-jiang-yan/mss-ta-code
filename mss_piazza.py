from piazza_api import Piazza
import time

my_piazza_email = "" # Please put your email (that you use to login to Piazza) inside the double quotation marks
my_piazza_password = "" # Please put your password (that you use to login to Piazza) inside the double quotation marks

# Get into MSS class
p = Piazza()
p.user_login(email = my_piazza_email, password = my_piazza_password)
mss = p.network("") # Enter Piazza network here (can be seen from Piazza URL)
post_index_list = []

# Gather a list of post indices
my_feed = mss.get_feed(limit = 999999, offset = 0)
post_index_list = [post['id'] for post in my_feed["feed"]]

# Iterate from list of post indices
for post_index in post_index_list:
    break_get_post = False
    while not break_get_post:
        try:
            current_post = mss.get_post(post_index)
        except:
            time.sleep(1) # Sometimes the servers on Piazza get jammed...
        else:
            print("{} : @{}".format(current_post["history"][0]["subject"], current_post["nr"]))
            break_get_post = True





