from piazza_api import Piazza
import time

my_piazza_email = "" # Please put your email (that you use to login to Piazza) inside the double quotation marks
my_piazza_password = "" # Please put your password (that you use to login to Piazza) inside the double quotation marks

# Get into MSS class
p = Piazza()
p.user_login(email = my_piazza_email, password = my_piazza_password)
mss = p.network("kizrj7sr77d2w6") # Enter Piazza network here (can be seen from Piazza URL)
folder_list = ['hw1', 'hw2', 'hw3', 'hw4', 'hw5', 'hw6', 'hw7', 'hw8', 'hw9', 'hw10', 'project', 'exam', 'logistics', 'other', 'week1', 'week2', 'week3', 'week4', 'week5', 'week6', 'week7', 'week8', 'week9', 'week10', 'week11', 'week12', 'week13', 'math_modelling', 'cerebry', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'polls']
post_index_list = []
post_dic = {}
for foldername in folder_list:
    post_dic[foldername] = []

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
            time.sleep(0.1) # Sometimes the servers on Piazza get jammed...
        else:
            if not 'feed_groups' in current_post['config'].keys(): # Only public posts are added
                for foldertitle in current_post['folders']:
                    post_dic[foldertitle] += [current_post]
            print(post_index) # Sanity check to ensure that your Python is not jammed
            break_get_post = True

print('\n')
print('Copy + Paste From Here Onwards')
print('--------------------------------------------------')
print('AUTOMATED POST LIST')
print('Response to @393_f1 - if we all can take turns to just run this code on our computers and update this information post regularly, we can save the class a lot of trouble. You just, need to run this, and copy + paste the outputs...')
print('Source code: https://github.com/li-jiang-yan/mss-ta-code/blob/main/mss_piazza_automation.py')
print('Last updated: {}'.format(time.asctime()))

for foldertitle in post_dic.keys():
    print('\n')
    print(foldertitle)
    for current_post in post_dic[foldertitle]:
        print("{} : @{}".format(current_post["history"][0]["subject"], current_post["nr"]))

print('\n')
print('--- END OF AUTOMATED POST LIST ---')
