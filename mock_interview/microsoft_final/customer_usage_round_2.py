




# for each customer id
# for each day i need to find a customer used the product_1 has the most usage for that day\
# customer_1 for product_1 has 40 min for day
# customer_2 or 3 for product_1 has 45 min for that day
# max_time used  (customer_id,)
# for each customer id I 'd calcute the sum of usage for all products that user has used
#


def most_used_time_by_customer(days: number of days):
    customers = {customer_id: customer_name, }
    usage = [{int: customer_id, product_id, datettime: start_usage, datetime: endusage}]
    most_used_customers = []
    max_value = initial as 0
    for day in days:  # days is 3 then we would look into day 1 and 2
        max_value = initial as 0
        for each customer id in usage:
            product_usage = 0
            if customer == curtomer_id:
                calcualte usage time for this day
                increment my product usage by the number minutes

        once i have the product usage then
        if product_usage > max_value:
            reset max_value to current product usage
            max_customer = current costomer id has the most number of usage

        add the this max_custmor id and look up its name in the customer name list and
        append it

        most_used_customers.append((max_customer, cusmtumer name))

    return most_used_customers
