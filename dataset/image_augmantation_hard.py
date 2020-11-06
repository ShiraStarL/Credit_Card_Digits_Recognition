import numpy as np
import imgaug as ia
import imageio
import imgaug.augmenters as iaa


dirs = range(5, 8)
path = "data/"

for d in dirs:
    img_path = path+str(d)+"/"+str(d)+".jpg"

    image = imageio.imread(img_path)

    images = [image] * 50

    sometimes = lambda aug: iaa.Sometimes(0.5, aug)

    seq = iaa.Sequential(
        [
            iaa.RandAugment(m=10),
            iaa.RandAugment(m=(2, 9)),
            iaa.RandAugment(n=(1, 3)),

            iaa.SomeOf((5, 10),
                [
                    iaa.RelativeRegularGridVoronoi(0.1, 0.25),
                    iaa.Superpixels(p_replace=(0.1, 1.0), n_segments=(16, 128)),
                    iaa.Add((-40, 40), per_channel=0.5),
                    iaa.Multiply((0.5, 1.5), per_channel=0.5),
                     iaa.Multiply((0.5, 1)),
                     iaa.JpegCompression(compression=(70, 99)),
                     iaa.BlendAlphaHorizontalLinearGradient(iaa.AddToHue((-100, 100))),
                     iaa.BlendAlphaCheckerboard(nb_rows=2, nb_cols=(1, 4),
                                 foreground=iaa.AddToHue((-100, 100))),
                     iaa.GaussianBlur(sigma=(0.0, 1.0)),
                     iaa.AddToHueAndSaturation((-50, 50), per_channel=True),
                     iaa.GammaContrast((0.5, 2.0), per_channel=True),
                     iaa.Affine(rotate=(-15, 15)),
                     iaa.Affine(translate_percent={"x": -0.20}, mode=ia.ALL, cval=(0, 255)),
                     iaa.Affine(translate_percent={"y": -0.20}, mode=ia.ALL, cval=(0, 255)),
                     iaa.Affine(translate_percent={"x": +0.20}, mode=ia.ALL, cval=(0, 255)),
                     iaa.Affine(translate_percent={"y": +0.20}, mode=ia.ALL, cval=(0, 255)),
                     iaa.BlendAlpha(
                        (0.0, 1.0),
                        iaa.Affine(rotate=(-20, 20)),
                        per_channel=0.5),
                    iaa.BlendAlpha([0.25, 0.75], iaa.MedianBlur(13)),
                    iaa.BlendAlphaElementwise(
                        (0.0, 1.0),
                        foreground=iaa.Add(100),
                        background=iaa.Multiply(0.2)),
                    iaa.BlendAlphaSimplexNoise(iaa.EdgeDetect(1.0)),
                    iaa.BlendAlphaSimplexNoise(
                        iaa.EdgeDetect(1.0),
                        upscale_method="nearest"),
                    iaa.BlendAlphaSimplexNoise(
                        iaa.EdgeDetect(1.0),
                        upscale_method="linear"),
                    iaa.BlendAlphaSomeColors(iaa.TotalDropout(1.0)),
                    iaa.BlendAlphaSomeColors(
                        iaa.AveragePooling(7), alpha=[0.0, 1.0], smoothness=0.0),
                    iaa.FastSnowyLandscape(
                        lightness_threshold=140,
                        lightness_multiplier=2.5),
                    iaa.Clouds(),
                    iaa.Fog(),
                    iaa.Rain(speed=(0.1, 0.3)),
                ],
                random_order=True
            )
        ],
        random_order=True
    )

    images_aug = seq(images=images)

    i = 0
    for img in images_aug:
        imageio.imwrite(path+str(d)+"/"+str(d)+"_"+ str(i) + '.jpg', img)
        i += 1

