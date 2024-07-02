import argparse

def create_mutation(firstname,surename):
    mutations =[]

    mutations.append(f"{firstname[0]}.{surename}") 
    mutations.append(f"{firstname[0]}{surename}")
    mutations.append(f"{firstname}.{surename}")
    mutations.append(f"{firstname}{surename}")
    mutations.append(f"{surename}.{firstname}")
    mutations.append(f"{surename}.{firstname[0]}")
    mutations.append(f"{surename[0]}.{firstname}")
    
    return mutations

def write_list_to_file(list,filename):
    with open(filename, 'w') as f:
        f.write("\n".join(map(str, list)))

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description="Tool to create Username Mutations")
    parser.add_argument("-firstname", nargs='?')
    parser.add_argument("-surename", nargs='?')
    parser.add_argument("-file", nargs='?')
    args=parser.parse_args()

    mutation_list = create_mutation(args.firstname,args.surename)
    write_list_to_file(mutation_list,args.file)
    print(mutation_list)


