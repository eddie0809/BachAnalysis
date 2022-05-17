import matplotlib.pyplot as plt
import numpy as np
from scipy.special import rel_entr, kl_div
from scipy.spatial.distance import jensenshannon
import py_midicsv as pm
from trash import header_skipper, file_getter
#import matplotlib as mpl
import sys


"""if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input("Filename (no extension): ")"""

# for using tex formatting and font in plots
#"""

plt.rcParams.update({'text.usetex':True, 'font.family':'serif'})
#plt.rcParams['text.latex.preamble'] = [r'\usepackage[utf8]{inputenc}\usepackage{lmodern}\inputencoding{utf8}\usepackage{amsmath}\usepackage{amssymb}\usepackage{dsfont}\usepackage{mathtools}\usepackage{physics}\begin{document}']


def getDiv(num, piece):#, collect, maxnum):
    filename = str(piece)+str(num)
    coole_line = header_skipper(filename)

    midiFile = np.genfromtxt(filename+".csv", delimiter=',', skip_header=coole_line, skip_footer=2, invalid_raise=False)

    rightHand = np.array([])
    leftHand = np.array([])

    for i in range(len(midiFile)):
        if midiFile[i,0] == 2:
            rightHand = np.append(rightHand, midiFile[i,[1,4]])
        elif midiFile[i,0] == 3:
            leftHand = np.append(leftHand, midiFile[i, [1,4]])

    rightHand = np.reshape(rightHand, (-1, 2))
    leftHand = np.reshape(leftHand, (-1, 2))


    newrightHand = np.array([])
    n=0
    while n <= (len(rightHand)-1):
        vec = [rightHand[n+1,0]-rightHand[n,0], rightHand[n,1]]
        newrightHand = np.append(newrightHand, vec)
        n = n+2
    newleftHand = np.array([])
    vec=[]
    n=0

    while n <= (len(leftHand)-1):
        vec = [leftHand[n+1,0]-leftHand[n,0], leftHand[n,1]]
        newleftHand = np.append(newleftHand, vec)
        n=n+2
    newrightHand = np.reshape(newrightHand, (-1,2))
    newleftHand = np.reshape(newleftHand, (-1, 2))

    newrightHand = newrightHand.astype(int)
    newleftHand = newleftHand.astype(int)

    rhmod12 = []
    lhmod12 = []

    for n in range(len(newrightHand)):
        rhmod12.append(newrightHand[n,1] % 12)
    for n in range(len(newleftHand)):
        lhmod12.append(newleftHand[n,1] % 12)

    rhHist = np.bincount(rhmod12, weights = newrightHand[:,0])
    lhHist = np.bincount(lhmod12, weights = newleftHand[:,0])

    if filename == "Prelude2":
        rhHist[1] = 0

    rhHist = rhHist/sum(rhHist)
    lhHist = lhHist/sum(lhHist)

    testDKL = kl_div(rhHist, lhHist)
    testJensha = jensenshannon(rhHist, lhHist)**2

    strDKL = str(sum(testDKL))
    strJensha = str(testJensha)

    res1 = 'jensen-shannon-divergence of left and right hand, inventio ' +str(num)+": "+strJensha+'\n'
    res2 = 'kullback-leibler-divergence of left and right hand, inventio ' +str(num)+": "+strDKL+'\n'
    minussigns = "#################################\n"
    allres = "#\n" + minussigns + res1 + res2 + minussigns + "#\n"
    #print(rhHist, '\n')
    #print(lhHist, '\n')
    #print(testDKL, '\n')
    #return allres
    print()
    #print(sum(testJensha))
    print("-------------------------------")


    notes = ['c', 'c\#', 'd', 'd\#', 'e', 'f', 'f\#', 'g', 'g\#', 'a', 'a\#', 'b','']
    x = np.arange(len(notes))+.5


    fig, ax = plt.subplots(2,1, sharex=True, figsize=(9,10))
    ax = ax.ravel()
    ax[0].hist(rhmod12, weights=newrightHand[:,0], bins=range(13), label = "Right Hand notes", color = "green")
    ax[1].hist(lhmod12, weights=newleftHand[:,0], bins=range(13), label = "Left Hand notes", color="blue")
    ax[1].set_xticks(x, notes)
    fig.legend(loc=7)
    #fig.tight_layout()
    fig.subplots_adjust(right=.8)
    plt.title("Histograms of notes in bach's inventio "+str(num)+", BWV "+str(num+771))
    #plt.savefig("inventio13.png")
    plt.show()

"""with open("results.txt", "w") as res:
    for i in range(1,16):
        res.write(getDiv(i, "invent"))

dings = open("results.txt", "r")
print("\n"+dings.read())
"""
getDiv(13,"invent")