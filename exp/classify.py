import pickle


def LCP(strs):
    if not strs:
        return ''
    for i, letter_g in enumerate(zip(*strs)):
        if len(set(letter_g)) > 1:
            return strs[0][:i]
    else:
        return min(strs)


def clas():
    with open("subgraph.txt", 'r') as f:
        max_len = 0
        for line in f.readlines():
            input_code = line.split()[1]
            if len(input_code) > max_len:
                max_code = input_code
                max_len = len(input_code)

    with open('lcs_all_class_dict', 'rb') as f:
        dic = pickle.load(f)

    outclass = ''
    longest_len = 0
    longest_common_code = ''
    for class_name in dic:
        for target_code in dic[class_name]:
            string = LCP([max_code, target_code])
            if len(string) > 0:
                if len(string) > longest_len:
                    # print(class_name,
                    longest_len = len(string)
                    outclass = class_name
                    longest_common_code = string
    return outclass
