# number of clicks to add a product to cart
# number of times lost (can be seen by hovering maybe, going back to the home, time between clicks)
# times the user had to click the back button, or start fresh, or cancel a course of action
# unable to record browser actions like back and reload using selenium ide
  
import json
  
fk_file = open('Flipkart_pro_user.side',)

data = json.load(fk_file)

count_clicks = 0
count_home_redirect = 0
count_remove_from_cart = 0
count_cancel = 0

with open ("Flipkart_pro_user_output.txt", 'w+') as f:
    for i in data['tests']:
        for j in i['commands']:
            f.write(j['command'] + '\n')
            if (j['command']=="click"):
                count_clicks += 1
    f.write('\n' + "Total number of clicks = " + str(count_clicks))

    for i in data['tests']:
        for j in i['commands']:
            # print(j['targets'])
            for z in j['targets']:
                # for identifying flipkart home button
                if z[0].startswith( 'css=.\\_2xm1JU' ):
                    count_home_redirect += 1
                # for identifying flipkart remove from cart button
                if z[0].startswith( 'css=.\\_3dsJAO:nth-child(2)' ):
                    count_remove_from_cart +=1
                # for identifying flipkart cancel button
                if z[0].startswith( 'css=.nZz3kj' ):
                    count_cancel += 1
    f.write('\n' + "Total number of home button clicks = " + str(count_home_redirect))
    f.write('\n' + "Total number of remove from cart button clicks= " + str(count_remove_from_cart))
    f.write('\n' + "Total number of cancel button clicks= " + str(count_cancel))


f.close()


sd_file = open('Snapdeal_pro_user.side',)

data = json.load(sd_file)

count_clicks = 0
count_home_redirect = 0
count_remove_from_cart = 0
count_cancel = 0

with open ("Snapdeal_pro_user_output.txt", 'w+') as f:
    for i in data['tests']:
        for j in i['commands']:
            f.write(j['command'] + '\n')
            if (j['command']=="click"):
                count_clicks += 1
    f.write('\n' + "Total number of clicks = " + str(count_clicks))

    for i in data['tests']:
        for j in i['commands']:
            # print(j['targets'])
            for z in j['targets']:
                # for identifying snapdeal home button
                if z[0].startswith( 'css=.notIeLogoHeader > .notIeLogoHeader' ):
                    count_home_redirect += 1
                # for identifying snapdeal remove from cart button
                if z[0].startswith( 'css=.remove-item-shortlist' ):
                    count_remove_from_cart +=1
                # snapdeal didn't allow user to cancel remove from cart opertation
                # if z[0].startswith( 'css=.nZz3kj' ):
                #     count_cancel += 1
    f.write('\n' + "Total number of home button clicks = " + str(count_home_redirect))
    f.write('\n' + "Total number of remove from cart button clicks= " + str(count_remove_from_cart))
    f.write('\n' + "Total number of cancel button clicks= " + str(count_cancel))


f.close()