from skimage import io, feature, color, transform
import discord
from discord.ext import commands
import numpy as np
import random


def importImage(link):
    finalImage = None

    image = io.imread(link)
    if len(image) > 0:
        finalImage = image

    return finalImage


def saveImage(img):
    if img is not None: 
        img = np.uint8(img)
        io.imsave("sample.jpg", img)
        return discord.File("sample.jpg")
    else:
        return None


def imgGrayscale(img):
    return color.rgb2gray(img)


def grayscale(arr):
    finalImage = None

    if len(arr) >= 2:
        link = arr[1]
        img = imgGrayscale(importImage(link))
        finalImage = saveImage(img)

    return finalImage


def edges(arr):
    finalImage = None

    if len(arr) >= 2:
        link = arr[1]
        img = feature.canny(imgGrayscale(importImage(link)))
        finalImage = saveImage(img)

    return finalImage


def swirl(arr):
    finalImage = None

    if len(arr) >= 2:
        link = arr[1]
        img = transform.swirl(importImage(link), rotation=7, strength=3, radius=1200)
        finalImage = saveImage(img)

    return finalImage


def warp(arr):
    finalImage = None

    if len(arr) >= 2:
        link = arr[1]
        img = importImage(link)
        h, w = img.shape[0:2]

        rand = random.random()
        src = np.array([[0, 0], [0, h], [w, h], [w, 0]])
        dst = np.array([[w*(0.3*rand + 0.1), h*(0.2*rand + 0.1)], [w*(0.3*rand), h*(0.4*rand + 0.6)],
                        [w*(0.2*rand + 0.8), h*(0.2*rand + 0.8)], [w*(0.4*rand + 0.5), h*(0.5*rand)]])

        tform3 = transform.ProjectiveTransform()
        tform3.estimate(src, dst)
        warped = transform.warp(img, tform3, output_shape=(h, w))
        finalImage = saveImage(warped)

    return finalImage


def printBack(arr):
    reply = ""

    if len(arr) >= 3:
        reply = arr[1] + " \n" + arr[2]

    return reply

# def roulette(ctx, message, member : discord.Member):
#     if random.randrange(1,7) == 1:
#         ctx.kick(member.User)
#         return 'hah DED!'
#     else :
#         return 'ew u alive still??!?'