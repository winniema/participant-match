import math


def format(textname):
    '''
    formats the input file into a dictionary of {name: (num1, num2, num3)}
    '''
    file = open(textname, "r")
    lines = file.readlines()
    name_hsn = {}
    for line in lines:
        person = line[:-1].split("\t")
        hsn = (person[1], person[2], person[3])
        name = person[0]
        name_hsn[name] = hsn
    return name_hsn

def remove(nested_list,list_ps, list_pf,  x, y):
    ''' remove(nested_list, which overall list, which element in that list)
    '''
    del nested_list[x]
    for i in range(len(nested_list)):
        del nested_list[i][y]
    del list_ps[x]
    del list_pf[y]

def find_min(nested_list):
    min = 1000
    for i in range(len(nested_list)):
        for j in range(len(nested_list[0])):
            if nested_list[i][j] < min:
                min = nested_list[i][j]
                x = i # the overall list p+s
                y = j # which element in the specific list p+f
    return (x, y)

def names_inorder(in_file):
    file = open(in_file, "r")
    lines = file.readlines()
    name_inorder = []
    for line in lines:
        person = line[:-1].split("\t")
        name_inorder.append(person[0])
    return name_inorder

def print_match(dict, infile, outfile):
    #infile is the file which limits the matching factor ie the P + S or the P when compared with P + F
    list_names = names_inorder(infile)
    f = open(outfile, "w")
    for i in range(len(list_names)):
        f.write(list_names[i] + " " + dict[list_names[i]] + '\n')
    return None

def match_matrix(dict1, dict2):
    match_list = []
    ps_list1 = []
    pf_list2 = []

    for key1 in dict1:
        diff_list = []
        name1 = key1
        hsn1 = dict1[name1]
        h1, s1, n1 = hsn1
        ps_list1.append(name1)
        for key2 in dict2:
            name2 = key2
            hsn2 = dict2[name2]
            h2, s2, n2 = hsn2
            if not(name2 in pf_list2):
                pf_list2.append(name2)
            diff = math.sqrt((int(h1)-int(h2))**2 + (int(s1)-int(s2))**2 + (int(n2)-int(n1))**2 )
            #diff = abs(int(h1)-int(h2)) + abs(int(s1)-int(s2)) + abs(int(n2)-int(n1))
            diff_list.append(diff)
        match_list.append(diff_list)
    return (match_list, ps_list1, pf_list2)

def match_best(matrix_info):
    matching = {}
    match_list, list1, list2 = matrix_info

    for i in range(min(len(match_list), len(match_list[0]))):
        x, y = find_min(match_list)
        matching[list1[x]] = list2[y]
        remove(match_list, list1, list2, x, y)
    return matching

if __name__ == "__main__":
# the first file should contain less of equal participants compared to the second file
    p_s = format("all_p.txt")
    p_f = format("all_pf.txt")
    matrix_in = match_matrix(p_s, p_f)
    print_match(match_best(matrix_in), "all_p.txt", "matching.txt")
