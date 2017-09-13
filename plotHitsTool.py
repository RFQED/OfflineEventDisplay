from matplotlib import pyplot as plt
from strawPositions import Ux, Uy, Vx, Vy
from pylab import figure, axes, title, savefig

xhit, yhit = [], []
xCalo, yCalo = [], []
sizeCalo = 20
sizeStraw = 10
#sizeWire = 5
hitcalo = False

# make it so you pass in data file path
# pass in what format you want output. png/ svg/ pdf


for line in open('testData.txt'):
#for line in open('strawCaloData.txt'):
    if line.startswith("Run"):
        header = line.split(',')
        fullheader = line
        print(fullheader)
        
        #plot straws   default linewidths is 0.5

        plt.scatter(Ux, Uy, s=sizeStraw, alpha=0.5, facecolors='none', edgecolors='r', linewidths=0.5, label="U Layer")
        plt.scatter(Vx, Vy, s=sizeStraw, alpha=0.5, facecolors='none', edgecolors='b', linewidths=0.5, label="V Layer")

       #plot wires
       #sizeWire = 0.5
       #plt.scatter(Ux, Uy, s=sizeWire, alpha=0.5, facecolors='none', edgecolors='black', linewidths=0.25, label="U Layer")
       #plt.scatter(Vx, Vy, s=sizeWire, alpha=0.5, facecolors='none', edgecolors='black', linewidths=0.25, label="V Layer")


    elif "END" in line:
        #reached end of event . plot clear and save
        print("Reached end of " + header[0])
#        print xhit
#        print yhit

        plt.scatter(xhit, yhit, s=sizeStraw, alpha=1, facecolors='black', edgecolors='r', linewidths=1, label="hit")

        if hitcalo is True:
            plt.scatter(xCalo, yCalo, s=sizeCalo, alpha=1, marker='X', c='r', linewidths=1, label="Calo hit")
        
        # Make a square figure and axes
        fig = figure(1, figsize=(1024, 1024))

        filename = fullheader.replace(", ", "_")
        filename = filename.replace("\n", "")
        filename = filename.replace(" ", "")

        plt.title(str(fullheader), fontsize=8) 
        plt.axis('off')
        fig.tight_layout()

        if hitcalo is True:
            savefig(str(filename)+'_CaloHit.svg', bbox_inches='tight', format="svg",  dpi=1200)
        else:
            savefig(str(filename)+'.svg', bbox_inches='tight', format="svg",  dpi=1200)

        plt.close()
        fig.clear()
        del xhit[:]
        del yhit[:]
        hitcalo = False
        xCalo = 0
        yCalo = 0

    elif line.startswith("CALO"):
        hitcalo = True
        print( "Hit calo")
        caloRow = line.split(',')
        print(caloRow[2])
        yCalo = caloRow[2].split(' ')[2]
        print("xCalo " + str(xCalo))

        xCalo = 1075
        # split line into x hit on face, time, energy

    else:
        row = line.split(',')
        xhit.append(row[0])
        yhit.append(row[1].strip('\n'))


