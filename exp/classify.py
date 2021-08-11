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
    
def clas_v2(code_str):
    if code_str[0:4] == 'TTTT':
        return 'bcl_xl'
    elif code_str.count('C') == 5:
        return 'bcl-2'
    elif code_str[0:5] == 'MMMMM':
        return 'E2F'
    elif 'CAAAA' in code_str:
        return 'Globin'
    elif ('DDD' in code_str):
        if code_str[code_str.index('DDD')+3] != 'D':# DDD not the last part
            return 'Histone'
        else:
            return 'Argo'
    elif code_str[0:5] == 'YYYYY':
        return 'HSP'
    elif 'FFF' in code_str:
        return 'pkd'
    elif code_str.count('Y') == 2:
        return 'serpin'
    elif 'KKKK' in code_str or 'AAAA' in code_str:
        return 'serine'
    else:
        return 'Argo'

if __name__ == '__main__':
    print(clas_v2('YYRRIIDIIRR'))

