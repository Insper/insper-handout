#!/usr/bin/env python3

import argparse

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

def toGitHub(f,o):
    try :
        fw = open(o,"w")
        fr = open(f,"r")
        box = False
        pandoc = False

        for line in fr :
            if "<div" in line:
                if "alert" in line :
                    box = True
                    fw.write("```\n")
                    fw.write("Info:\n\n")
                if "question" in line :
                    box = True
                    fw.write("```\n")
                    fw.write("Questão:\n\n")
                if "box" in line :
                    box = True
                    fw.write("```\n")

            elif "</div" in line :
                if box == True:
                    fw.write("```\n")
            elif "![" in line :
                if "](" in line :
                    if ".pdf" in line :
                        fw.write(rreplace(line,"pdf", "png", 1))
           # elif "---" in line :
           #     if pandoc == False :
           #         if "pandoc" in line[]:
           #             pandoc = True
           #     else:
           #         pandoc = False
            else:
                if pandoc == False :
                    fw.write(line)

    except IOError:
        print("Arquivo não encontrado")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--fileIn" , required=True)
    ap.add_argument("-o", "--fileOut", required=True)
    args = vars(ap.parse_args())
    toGitHub(f=args["fileIn"], o=args["fileOut"])



