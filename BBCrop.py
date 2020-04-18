import pdb, os, re
import pandas as pd
import PIL
# args are coords of bounding box and padding in pixels
def findBox(i_width, i_height, x1, y1, x2, y2, padding=100):
    x_m = int((x1 + x2)/2)
    x1_n = x_m - padding
    x2_n = x_m + padding
    if (x1_n < 0): # for left-most bounding boxes if midpoint is within 100 pixels of both sides of image
        x1_n = 0
        x2_n = padding*2
    elif (x2_n > i_width):
        x1_n = i_width-2*padding
        x2_n = i_width
    y_m = int((y1 + y2)/2)
    y1_n = y_m - padding
    y2_n = y_m + padding
    if (y1_n < 0): # biased for upper-most bounding boxes if midpoint is within 100 pixels of top and bottom
        y1_n = 0
        y2_n = padding*2
    elif (y2_n > i_height):
        y1_n = i_height-2*padding
        y2_n = i_height

    return [x1_n, y1_n, x2_n, y2_n]

def cropImages():
    if not os.path.isdir('BoxedImages'):
        os.mkdir('BoxedImages')
    BBData2 = pd.read_csv("BoxedFish.csv")
    coords = map(int, re.findall(r'\d+', BBData2.iloc[0].loc["Box"]))
    # for m in coords:  
for file in os.listdir('Images_Manu_labelled/MC6_5'):
    if (file[-3:] == 'csv'):
        BBData = pd.read_csv(os.path.join("Images_Manu_labelled/MC6_5", str(file)))
        print(BBData.iloc[0][0]) #Image ID
        print(BBData.iloc[0][-4:]) #xmin, ymin, xmax, ymax
        for row in BBData:
            crop_coords = findBox(row[1], row[2], row[4], row[5], row[6], row[7], pad=112) #padding is 100 pixels by default
            im = PIL.open(os.path.join("Images_Manu_labelled/MC6_5", file[:-4], row[1]))
            n_im = im.crop(crop_coords)
            n_im.save(os.path.join("CroppedImages", MC6_5))
        break

readFiles()