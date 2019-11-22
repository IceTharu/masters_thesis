import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa
import cv2
import matplotlib.pyplot as plt

import matplotlib.image as mpimg




#ia.seed(1)

# Example batch of images.
# The array has shape (32, 64, 64, 3) and dtype uint8.
images = mpimg.imread('/home/thorsteinngj/Documents/Skoli/Thesis/Code/Mask_RCNN/samples/graves/new_dataset/val/95873168.jpg')
#images = cv2.imread('/home/thorsteinngj/Documents/Skoli/Thesis/Code/Mask_RCNN/samples/graves/new_dataset/val/95873168.jpg')
#images = np.array(
#    [ia.quokka(size=(64, 64)) for _ in range(32)],
#    dtype=np.uint8
#)

seq = iaa.Sometimes(.667, iaa.Sequential([
    #iaa.Fliplr(1), # horizontal flips
    #iaa.Crop(percent=(0, 0.1)), # random crops
    # Small gaussian blur with random sigma between 0 and 0.25.
    # But we only blur about 50% of all images.
    iaa.Sometimes(0.5,
        #iaa.GaussianBlur(sigma=(0, 0.25))
    ),
    # Strengthen or weaken the contrast in each image.
    #iaa.ContrastNormalization((0.75, 1.5)),
    # Add gaussian noise.
    # For 50% of all images, we sample the noise once per pixel.
    # For the other 50% of all images, we sample the noise per pixel AND
    # channel. This can change the color (not only brightness) of the
    # pixels.
    #iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255)),
    # Make some images brighter and some darker.
    # In 20% of all cases, we sample the multiplier once per channel,
    # which can end up changing the color of the images.
    #iaa.Multiply((0.8, 1.2)),
    # Apply affine transformations to each image.
    # Scale/zoom them, translate/move them, rotate them and shear them.
    iaa.Affine(
        #scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},
        #translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},
        #rotate=(-180, 180),
        #shear=(-8, 8)
    )
], random_order=True)) # apply augmenters in random order



images_aug = seq(images=images)

#plt.imshow(images)
#plt.imshow(images_aug)



fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax1.imshow(images)
ax2 = fig.add_subplot(2,1,2)
ax2.imshow(images_aug)
#%%

seq = iaa.Sequential([
    iaa.Fliplr(0.5), # horizontal flips
    iaa.Crop(percent=(0, 0.1)), # random crops
    # Small gaussian blur with random sigma between 0 and 0.5.
    # But we only blur about 50% of all images.
    iaa.Sometimes(0.5,
        iaa.GaussianBlur(sigma=(0, 0.5))
    ),
    # Strengthen or weaken the contrast in each image.
    iaa.ContrastNormalization((0.75, 1.5)),
    # Add gaussian noise.
    # For 50% of all images, we sample the noise once per pixel.
    # For the other 50% of all images, we sample the noise per pixel AND
    # channel. This can change the color (not only brightness) of the
    # pixels.
    iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),
    # Make some images brighter and some darker.
    # In 20% of all cases, we sample the multiplier once per channel,
    # which can end up changing the color of the images.
    iaa.Multiply((0.8, 1.2), per_channel=0.2),
    # Apply affine transformations to each image.
    # Scale/zoom them, translate/move them, rotate them and shear them.
    iaa.Affine(
        scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},
        translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},
        rotate=(-25, 25),
        shear=(-8, 8)
    )
], random_order=True) # apply augmenters in random order
    