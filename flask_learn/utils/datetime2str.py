

def datetime_format(data: list) -> list:
    for item in data:
        item['update_time'] = str(item['update_time'])
    return data