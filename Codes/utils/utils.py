


def node_texts(data):
    attributes = {}
    for i in range(len(data)):
        key = data.iloc[i]['ownerName']
        if key in attributes:
            attributes[key].append(data.iloc[i]['textField'])
        elif key not in attributes:
            attributes[key] = [data.iloc[i]['textField']]
