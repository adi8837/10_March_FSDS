from pprint import pprint
data1 = {"abc":{"def":{"ghi":{"jkl":{"mno":{"pqr":{"stu":{"vwx":{"yz":"you are finally here !!!"}}}}}}}}}
def style(data):
    dict1 = {}
    for a, b in data.items():
        if isinstance(b, dict):
            d = style(b)
            dict1.update(d)
            dict1[a] = list(reversed(d))
        else:
            dict1[a] = [b]
    return dict1
pprint(style(data1))
