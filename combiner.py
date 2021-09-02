from PIL import Image
import numpy as np
import random

accessoriesHat = ["RiceWorkerHat.png", "SantaHat.png","Crown.png" ,"Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"]
accessoriesEyes = ["3DGlasses.png", "Scar.png","Empty","Empty","Empty","Empty","Empty","Empty"]
accessoriesNeck = ["GoldChain.png","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"]
basePath = r"C:/Users/Robert/Desktop/NFT/Pieces/" # Location where image pieces are
generatedImagePath = r"C:/Users/Robert/Desktop/NFT/Generated/" # Location where you want images to be saved to

def alteredImageColor(im, originalColour, newColour):
    data = np.array(im)

    r1, g1, b1 = originalColour[0], originalColour[1], originalColour[2] # Original value
    r2, g2, b2 = newColour[0], newColour[1], newColour[2] # Value that we want to replace it with

    red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
    mask = (red == r1) & (green == g1) & (blue == b1)
    data[:,:,:3][mask] = [r2, g2, b2]
    
    newImage = Image.fromarray(data)
    
    return newImage

def getRandomColourArray():
    return [random.randint(0,255), random.randint(0,255), random.randint(0,255)]


def getBaseImage():
    baseImage = Image.open(basePath + "BackGround.png")
    baseImage = alteredImageColor(baseImage, [255, 255, 255], getRandomColourArray());
    return baseImage;
	
def getFaceImage():
    faceColours = Image.open(basePath + "FaceColours.png")
    faceColours = alteredImageColor(faceColours, [0, 162, 232], getRandomColourArray());
    faceColours = alteredImageColor(faceColours, [255, 255, 255], getRandomColourArray());
    faceColours = alteredImageColor(faceColours, [153, 217, 234], getRandomColourArray());
    return faceColours;
	
def getEyeImage():
    eyeColuor = Image.open(basePath + "EyeColour.png")
    eyeColuor = alteredImageColor(eyeColuor, [237, 28, 36], getRandomColourArray());
    return eyeColuor;
	
def getOutlineImage():
    outline = Image.open(basePath + "Outline.png")
    return outline;
	
def combineImages(baseImage, onTopImage):
    baseImage.paste(onTopImage, (0,0), mask = onTopImage)
    return baseImage;

def applyAccessory(baseImage, accessoryList):
    accessory = accessoryList[random.randint(0,len(accessoryList) -1)]
    if accessory != "Empty":
        accessoryImage = Image.open(basePath + accessory);
        baseImage.paste(accessoryImage, (0,0), mask = accessoryImage);
	
		
def saveHighResImage(baseImage, imageID):
    baseImage = baseImage.resize((500,500),Image.NEAREST)
    imageLocation = generatedImagePath + "/JellyBob" + str(imageID)+ ".png";
    baseImage.save(imageLocation);


def makeJellyBob(labelNumber):
    baseImage = getBaseImage();

    outlineImage = getOutlineImage();

    faceImage = getFaceImage();

    eyeImage = getEyeImage();

    combineImages(baseImage, outlineImage);
    combineImages(baseImage, faceImage);
    combineImages(baseImage, eyeImage);


    applyAccessory(baseImage, accessoriesHat);
    applyAccessory(baseImage, accessoriesEyes);
    applyAccessory(baseImage, accessoriesNeck);
            
    saveHighResImage(baseImage, labelNumber);

    
def makeMultipleJellyBob(count):
    for i in range(count):
        makeJellyBob(i);

makeMultipleJellyBob(50);
