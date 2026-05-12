from PIL import Image
from qrtocurve.qrreader.qrimage import QRImage

def read_qr(image: Image) -> QRImage:
    '''
    Read an image and convert it to a QRImage.

    :param image: An image loaded in memory. See README for specifications.
    :type image: Image
    :return: The QR image.
    :rtype: QRImage
    '''
    if not isinstance(image, Image):
        raise TypeError(f"image must be type PIL.Image, not type {type(image)}.")
    # TODO: Find the first black pixel
