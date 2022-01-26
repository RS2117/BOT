global lines
global lineNo
with open("FollowProflieList.txt") as f:
    lines = f.read().split("\n")
    print(lines[0])
    print(lines[1])
    print(lines[2])
    print(lines[3])
    print(lines[4])
    print(lines[5])
    print(lines[6])
    print(lines[7])
    print(lines[8])
    print(lines[9])
    
i = 0
while i < len(lines):
    for line in lines:
        f = open("FollowList.txt", "w+")
        print(line.strip("\n"))
        if line.strip("\n") != lines[i]:
            for line in lines:
                f = open("FollowList.txt", "w+")
                f.write(line) 
                f.write("\n")
                f.close()
        else:
            print(lines[0])
            del lines[0]
        if(i < len(lines)):
            f = open("FollowList.txt", "r")
            lines = f.read().split("\n")
            for line in lines:
                print(line)
            f.close()
    f.close()
    i = i + 1
