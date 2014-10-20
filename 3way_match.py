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
        hsn = (int(person[1]), int(person[2]), int(person[3]))
        name = person[0]
        name_hsn[name] = hsn
    return name_hsn

def remove(matrix, name_ps , name_p, name_pf, x, y, z):
    ''' remove(nested_list, which overall list, which element in that list)
    '''
    del matrix[x]
    for i in range(len(matrix)):
        del matrix[i][y]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            del matrix[i][j][z]

    del name_ps[x]
    del name_p[y]
    del name_pf[z]

def find_min(matrix):
    min = 1000
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix[0][0])):
                if matrix[i][j][k] < min:
                    min = matrix[i][j][k]
                    x = i
                    y = j
                    z = k
    return (x, y, z)

def names_inorder(in_file):
    file = open(in_file, "r")
    lines = file.readlines()
    name_inorder = []
    for line in lines:
        person = line[:-1].split("\t")
        name_inorder.append(person[0])
    return name_inorder

def print_match(matching, outfile):
    #matching is a list of tuples (x, y, z)
    f = open(outfile, "w")
    for i in range(len(matching)):
        f.write(matching[i][0] + " " + matching[i][1] + " " + matching[i][2] + '\n')
    return None

def match_matrix(file_p, file_ps, file_pf):
    '''

    '''
    p_dict = format(file_p)
    ps_dict = format(file_ps)
    pf_dict = format(file_pf)

    name_ps = []
    name_p = []
    name_pf = []

    list3 = []

    for i in ps_dict:
        list2=[]
        name_ps.append(i)
        l, m, n = ps_dict[i]
        for j in p_dict:
            list1 = []
            if not(j in name_p):
                name_p.append(j)
            a, b, c = p_dict[j]
            for k in pf_dict:
                if not(k in name_pf):
                    name_pf.append(k)
                x, y, z = pf_dict[k]
                sum1 = (a-l)**2 + (b-m)**2 + (c-n)**2
                sum2 = (a-x)**2 + (b-y)**2 + (c-z)**2
                sum3 = (l-x)**2 + (m-y)**2 + (n-z)**2
                diff = math.sqrt(sum1) + math.sqrt(sum2) + math.sqrt(sum3)
                #diff = math.sqrt(sum1+sum2 +sum3)
                list1.append(diff)
            list2.append(list1)
        list3.append(list2)
    return (list3, name_ps, name_p, name_pf)

def match_best(matrix_info):
    matching = []
    matrix, name_ps, name_p, name_pf = matrix_info

    for i in range(min(len(matrix), len(matrix[0]), len(matrix[0][0]))): #which is 10
        x, y, z = find_min(matrix)
        matching.append((name_ps[x], name_p[y], name_pf[z]))
        remove(matrix, name_ps, name_p, name_pf, x, y, z)
    return matching

if __name__ == "__main__":
# the first file should contain less of equal participants compared to the second file

    match = match_best(match_matrix("p23.txt", "ps23.txt", "pf23.txt"))
    print_match(match, "matching.txt")
