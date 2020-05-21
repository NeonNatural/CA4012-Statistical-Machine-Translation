import sys

def grams(n, string):
    lst=[]
    s = string.split()
    for i in range(len(s)-n+1):
        lst.append(s[i:i+n])


    return lst

r = [0,0,0,0]


def main():

    output = "The gunman was shot dead by police ."
    ref = "The gunman was shot dead by the police ."

    ref1 = "The gunman was shot to death by the police . "
    ref2 = "The gunman was shot to death by the police . "
    ref3 = "Police killed the gunman ."
    ref4 = "The gunman was shot dead by the police ."

    #ref = [ref1,ref2,ref3,ref4]


    g = 1
    e=0
    while g <= 4:
        out = grams(g, output)
        print(out)

        i=0
        n=0

        while i < len(out):

            if " ".join(out[i]) in ref:#or ref2 or ref3 or ref4:
                n+=1
                i+=1
            else:
                i+=1
        g+=1

        r[e]=  n/len(out)
        e+=1

    print(r)
    bleu_score=((min(1,len(output)/len(ref))) * ((r[0]*r[1]*r[2]*r[3])**0.25))
    print(bleu_score)



if __name__ == "__main__":
    main()
