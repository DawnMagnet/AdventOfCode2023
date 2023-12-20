xrules, xdata = open("input_day19.txt").read().split("\n\n")

default_dict = {t: [0, -1] for t in "xmsa"}
from copy import deepcopy


class Rule:
    def __init__(self, description):
        tx = description.replace(">", "<")
        if "<" not in tx:
            self.next = tx
            self.symbol = ""
        else:
            self.varname = tx.split("<")[0]
            self.symbol = "<" if "<" in description else ">"
            self.value = int(tx.split("<")[1].split(":")[0])
            self.next = tx.split(":")[1]

    def match(self, data):
        if self.symbol == "":
            return True
        if self.symbol == "<":
            return data[self.varname] < self.value
        return data[self.varname] > self.value

    def split_range(self, data):
        if self.symbol == "":
            return deepcopy(data), default_dict

        if self.symbol == "<":
            if data[self.varname][1] < self.value:
                return deepcopy(data), default_dict
            if self.value <= data[self.varname][0]:
                return default_dict, deepcopy(data)
            left = deepcopy(data)
            left[self.varname][1] = self.value - 1
            data[self.varname][0] = self.value
            return left, data

        if data[self.varname][0] > self.value:
            return deepcopy(data), default_dict
        if self.value >= data[self.varname][1]:
            return default_dict, deepcopy(data)
        left = deepcopy(data)
        left[self.varname][1] = self.value
        data[self.varname][0] = self.value + 1
        return data, left


class RuleDict:
    def __init__(self, rules):
        rules_dict = {}
        for rule in rules.splitlines():
            rule_name, x = rule[:-1].split("{")
            rule_list = []
            for item in x.split(","):
                rule_list.append(Rule(item))
            rules_dict[rule_name] = rule_list
        self.rules_dict = rules_dict

    def apply(self, data, cur="in"):
        if cur == "A" or cur == "R":
            return cur
        for rule in self.rules_dict[cur]:
            if rule.match(data):
                return self.apply(data, rule.next)

    def apply_range(self, data, cur="in"):
        tmp = 1
        for _, v in data.items():
            tmp *= v[1] - v[0] + 1
        if tmp == 0:
            return 0
        if cur == "A":
            return tmp
        if cur == "R":
            return 0
        res = 0
        for rule in self.rules_dict[cur]:
            deal, data = rule.split_range(data)
            res += self.apply_range(deal, rule.next)
        return res


rule = RuleDict(xrules)
res = 0
for line in xdata.splitlines():
    data = {}
    for q in line[1:-1].split(","):
        a, b = q.split("=")
        data[a] = int(b)
    if rule.apply(data) == "A":
        res += sum(data.values())
print(res)

print(rule.apply_range({t: [1, 4000] for t in "xmsa"}))
# print(256000000000000)
# print(167409079868000)
