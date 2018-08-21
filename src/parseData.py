import json

# Global data accumulation
dataCSV = ""
dataJSON = {
    "data": []
}


def parseFactor(filter_stock, factor):
    # Get stock
    stock = factor[0]

    if stock != filter_stock:
        return None

    # Get date
    year = factor[1][0:4]
    month = factor[1][4:6]
    day = factor[1][6:8]
    date = year + '-' + month + '-' + day

    # Get time
    hour = factor[2][0:2]
    minute = factor[2][2:4]
    time = hour + ':' + minute

    # Get prices
    open_price = factor[3]
    high_price = factor[4]
    low_price = factor[5]
    close_price = factor[6]

    return [stock, date, time, open_price, high_price, low_price, close_price]


def toCSV(parsed):
    global dataCSV

    record = ",".join(parsed)
    dataCSV += record


def toJSON(parsed):
    global dataJSON

    record = {
        "date": parsed[1],
        "time": parsed[2],
        "open_price": parsed[3],
        "high_price": parsed[4],
        "low_price": parsed[5],
        "close_price": parsed[6][:-1],  # remove line jump
    }
    dataJSON["data"].append(record)


def dump(stock, output_path):
    global dataCSV
    global dataJSON

    # CSV
    with open(output_path + ".csv", 'w') as outfile:
        outfile.write(dataCSV)

    # JSON
    dataJSON["stock"] = stock
    with open(output_path + ".json", 'w') as outfile:
        json.dump(dataJSON, outfile)


def parse(filter_stock, input_path, output_path):
    # Read file
    raw = open(input_path)
    lines = raw.readlines()
    raw.close()

    for line in lines:
        # parse
        factor = line.split(',')
        parsed = parseFactor(filter_stock, factor)

        if parsed is not None:
            toCSV(parsed)
            toJSON(parsed)
