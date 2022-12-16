import re

input_file = 'python/d7/input.txt'

total_space = 70000000
needed_space = 30000000

regex1 = r'(\$\scd\s[^\.\n]+\n)|(\$\scd\s\.\.\n)|(dir\s[a-z]+\n)|(\$\sls\n)|(\s[a-z\.]+\n)'
regex2 = r'(,\s])|(,\s$)'

list_of_tree_sums = []

def tree_sum(tree):
    if isinstance(tree, int):
        return tree
    total = sum([tree_sum(sub_tree) for sub_tree in tree])
    list_of_tree_sums.append(total)
    return total

def replacements1(match_obj):
    if match_obj.group(1) is not None:
        return "["
    if match_obj.group(2) is not None:
        return "], "
    if match_obj.group(3) is not None:
        return ""
    if match_obj.group(4) is not None:
        return ""
    if match_obj.group(5) is not None:
        return ", "

def replacements2(match_obj):
    if match_obj.group(1) is not None:
        return "]"
    if match_obj.group(2) is not None:
        return ""

def file_string(filename):
    with open(filename) as file:
        return "".join(file.readlines())

def regex_subs(string):
    string = re.sub(regex1, replacements1, string)
    return re.sub(regex2, replacements2, string)

if __name__ == '__main__':
    used_space = tree_sum(eval(regex_subs(file_string(input_file))))
    print(sum([x for x in list_of_tree_sums if x <= 100000]))
    print(min([x for x in list_of_tree_sums if x + (total_space-used_space)>needed_space]))
