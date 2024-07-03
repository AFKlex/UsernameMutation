import argparse

def create_mutation(firstname,surename):
    mutations =[]

    mutations.append(f"{firstname[0]}.{surename}") 
    mutations.append(f"{firstname[0]}{surename}")
    mutations.append(f"{firstname}.{surename}")
    mutations.append(f"{firstname}{surename}")
    mutations.append(f"{surename}.{firstname}")
    mutations.append(f"{surename}.{firstname[0]}")
    mutations.append(f"{surename[0]}{surename[1]}{firstname[0]}{firstname[1]}")
    
    return mutations

def write_list_to_file(list,filename):
    with open(filename, 'w') as f:
        f.write("\n".join(map(str, list)))

def readFile(filename):
    fileData=[]
    with open(filename,"r") as f:
        for line in f:
            print(line)
            name = line.rstrip().split(" ")
            fileData.append([name[0],name[1]])
    return fileData

def ListMutation(list):
    mutation_list = []
    for entry in list:
        singleUserMutationList = create_mutation(entry[0],entry[1])
        for user in singleUserMutationList:
            mutation_list.append(user)

    return mutation_list

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description="Tool to create Username Mutations")
    parser.add_argument("-firstname", nargs='?', help= "User Firstname for Single User Mutation")
    parser.add_argument("-surename", nargs='?', help= "User Surename for Single User Mutation")
    parser.add_argument("-file", nargs='?', help="Provide a File for the result to be exported to.")
    parser.add_argument("-list", nargs='?', help= 'Provide a List of Files with names to be mutatated. Format: "Firstname Surename" one Name per Line')
    args=parser.parse_args()


    if args.list is not None:
        print(args.list) 

    if (args.firstname is None or args.surename is None) and args.list is None:
        print("Please provide -Firstname and -Surename or a list with first and surename per line")
        exit

    if args.file is None: 
        writeToFile=False
    else:
        writeToFile=True
 
    if args.list is None: 
        mutation_list = create_mutation(args.firstname,args.surename)
    else:
        listData = readFile(args.list)
        mutation_list = ListMutation(listData)
        
    if writeToFile:
        write_list_to_file(mutation_list,args.file)
    else:
        print(mutation_list)


