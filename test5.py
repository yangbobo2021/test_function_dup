
def Test100(data):
    sum = 0
    max_value = 0
    for item in data:
        if max_value < item['value']:
            max_value = item['value']
        sum += 1
    
    return sum, max_value
