comp_num, comp_size = None, None

def find_Comp(x): # pronađi kojoj komponenti pripada čvor
    while x != comp_num[x]:
        x = comp_num[x]
        
    return x


def merge_Comp(x, y): # spoji x i y dio veze 
    x = find_Comp(x) # promjeni x na root  komponente
    y = find_Comp(y) # promjeni y na root  komponente
    
    comp_num[y] = x
    comp_size[x] += comp_size[y]


def num_of_spanning_trees(n, x, y):
    mod = 987654323 # inicijalizacija modula 
    m = len(x) # broj veza u E

    global comp_size, comp_num
    comp_size = [1 for i in range(n+1)] # inicijalizacija veličine komponenti 
    comp_num = [i for i in range(n+1)]  #inicijalizacija indikatora povezanosti 

    for i in range(m):
        if find_Comp(x[i]) == find_Comp(y[i]):
            # ako x i y imaju isti root vec su spojeni i nastaje ciklus
            return 0
        merge_Comp(x[i], y[i]) # spajanje veze
   
    size_and_num_comp=[] # veličina i broj komponenti 
    for i in range(1,n+1):
        if comp_num[i] == i: # ako je comp_num[i] nepromjenjen našli smo root cvor komponente 
            size_and_num_comp.append(comp_size[i])
    if len(size_and_num_comp) == 1: 
        return 1 # ako postoji samo jedna komponeta(stablo) rezultat je 1
             
    ans = (n ** (len(size_and_num_comp)-2)) # n^(k-2) dio 
    
    for component_size in size_and_num_comp: # s_0*s_1* … *s_{k-1} dio.
        ans = (ans * component_size) % mod
    
    return ans

#print('Rezultat:',num_of_spanning_trees(4, [1, 2, 1], [2, 3, 3]))               # 0
#print('Rezultat:',num_of_spanning_trees(3, [1, 2], [2, 3]))                     # 1
#print('Rezultat:',num_of_spanning_trees(4, [1,1], [3,4]))                       # 3
#print('Rezultat:',num_of_spanning_trees(5, [1, 3, 4], [2, 4, 5]))               # 6 
#print('Rezultat:',num_of_spanning_trees(4, [1], [2]))                           # 8
#print('Rezultat:',num_of_spanning_trees(8, [1, 4, 2, 3, 5], [4, 7, 6, 5, 8]))   # 144
print('Rezultat:',num_of_spanning_trees(44, [10, 12, 14, 22, 13, 17, 9], [19, 43, 15, 27, 15, 27, 33])) # 782453952
#print('Rezultat:',num_of_spanning_trees(1000, [1], [2]))                        # 529013784