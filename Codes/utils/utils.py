


def node_texts(data):
    attributes = {}
    for i in range(len(data)):
        key = data.iloc[i]['ownerName']
        if key in attributes:
            attributes[key].append(data.iloc[i]['textField'])
        elif key not in attributes:
            attributes[key] = [data.iloc[i]['textField']]
    return attributes

def sort_by_date(data):
    data.set_index('time_jalali', inplace=True)
    data = data.sort_values(by='time_jalali')
    return data

def node_emotion_attributes(attributes, emotion_module):


