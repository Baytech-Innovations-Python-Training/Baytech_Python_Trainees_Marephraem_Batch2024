import datetime
def fine_calculator(deadline):

    """ This function accepts the deadline as date param
        and Returns the fine amount and number of days that
        the person has exceeded or left for the subscription """
    
    curr_year, curr_month, curr_date = ''.join('-'.join(str(datetime.datetime.now()).split('-')).split()[:-1]).split('-')
    deadline_date, deadline_month, deadline_year = deadline.split('-')
    deadline = datetime.date(int(deadline_year), int(deadline_month), int(deadline_date))
    current_date = datetime.date(int(curr_year), int(curr_month), int(curr_date))
    if (deadline - current_date).days <= 0:
        return f'You\'ve {-((deadline - current_date).days)} days left for renewable'
    else:
        if (deadline - current_date).days <= 5:
            return f'You\'ve exceeded {(deadline - current_date).days} days and you\'ll be charged a fine of Rs. 5 for each days {(deadline - current_date).days * 5}'
        elif ((deadline - current_date).days > 5) and ((deadline - current_date).days <= 30):
            return f'You\'ve exceeded {(deadline - current_date).days} days and you\'ll be charged a fine of Rs. 15 for each days {{(deadline - current_date).days * 15}}'
        else:
            return 'Subscription Closed'
