#!/usr/bin/env python3
import moms_apriltag as apt
import numpy as np
import imageio
from matplotlib import pyplot as plt

if __name__ == '__main__':


    # span =4
    # family = "tag36h11"
    # shape = (1,1) 
    # scale = 10
    # filename = 'id'+str(span)+'.png'
    # #make tag board
    # tgt = apt.board(shape, family, scale,span)
    # imageio.imwrite(filename, tgt)

    
#%%

    for tagID in range(0,49):
        family = "tag36h11"
        #tagID= 1
        tag = apt.generate(family, [tagID])[0]
        print(tag)
        im = np.array(tag.array) # so array, contains the image data
        plt.axis('off')
        plt.imshow(im, cmap="gray")
        plt.savefig(str(tagID)+'.png')
    
        


