import matplotlib.pyplot as plt
import numpy as np
import matplotlib

#Moorabie TB-TJM-080 (standard deviance given)
#Krymka RS-CMP-063 (No standard deviance given)

font = {'family' : 'timesnewroman',    ####
        'color'  : 'darkred',          # Defines what color/texture/font the title/label text will be.
        'weight' : 'normal',           #
        'size'   : 16,                 ####
        }

datafile = file('catalogues/Spectra_Catalogue.txt') #Where the file name/IDs are stored
identification = raw_input("What ID number would you like to search in the Spectra_Catalogue?\n")
wavelength = raw_input("Would you like the wavelength units to be micrometers (m) or nanometers (n)?\n")

id1 = identification[3:6] ## Splits up the id to get folder names
id2 = identification[0:2] ##

for line in datafile:
    if identification in line:
        contents = line.split()
        fileName = contents[0] #Get just the filename
        print("The File name is: "+fileName+".txt")
        fileName=fileName+".txt"
        break

samples = file ('catalogues/Sample_Catalogue.txt')
for line in samples:
    if identification in line: #Find the name of the sample associated with the ID provided.
        contentsofLine = line.split()
        sampleName = contentsofLine[1]


path = "data/"+id1+"/"+id2+"/"+fileName #standard path
print(path+"\n\n")
currFile = path
x=[]
y=[]
error=[] #for standard deviance
inputFileHandle = open(currFile)
fileLines = inputFileHandle.readlines()
errorbar_bool = True
for line in fileLines:
    nums = line.split()
    x.append(nums[0])
    y.append(nums[1])
    try:
        error.append(nums[2])
    except IndexError:
        errorbar_bool=False
        pass
x=x[2:]
y=y[2:]
x = np.array(x, np.float)
y = np.array(y, np.float)
error = error[2:]
error = np.array (error, np.float)
nanometers =[]
x=np.array(x)
y=np.array(y)
errornumpy = np.array(error)

nameOfWave = "(microns)"
if (wavelength == "n" or wavelength == "N"):
    i = 0
    nameOfWave = "(nanometers)"
    for each in x:
        x[i] = x[i]*1000
        i+=1



if errorbar_bool == True:
    plt.errorbar(x, y, yerr=error, fmt='-o')
    print("Error bars shown because standard deviance given.")
else:
    plt.plot(x, y, 'bo')
    print("No standard deviance given.")

plt.title('Reflectance Spectrum for '+identification+' ('+sampleName+')', fontdict=font)
#plt.text(2,0.050,identification, fontdict=font)
plt.xlabel('Wavelength '+nameOfWave, fontdict=font)
plt.ylabel('Reflectance', fontdict=font)
plt.show()
