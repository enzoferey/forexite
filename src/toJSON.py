def parseFactor(factor):
    # Get stock
    stock = factor[0]

    # convert datetime format
    year = factor[1][0:4]
    month = factor[1][4:6]
    day = factor[1][6:8]
    date = year + '-' + month + '-' + day

    hour = factor[2][0:2]
    minute = factor[2][2:4]
    time = hour + ':' + minute

    # price
    open_price = factor[3]
    high_price = factor[4]
    low_price = factor[5]
    close_price = factor[6]

    return stock + ',' + date + "," + time + ',' + open_price + ',' \
        + high_price + ',' + low_price + ',' + close_price


def toJSON(input_path, output_path):
    print('Converting DATA to JSON...')
    raw = open(input_path)
    lines = raw.readlines()
    raw.close()

    output = open(output_path, 'a')
    for line in lines:
        # parse
        factor = line.split(',')
        record = parseFactor(factor)

        # write
        output.write(record)

    output.close()
