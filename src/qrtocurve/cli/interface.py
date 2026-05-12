import qrtocurve.cli.parser as argument_parser
from copy import deepcopy
from PIL import Image

class QRtoCurveCLI:

    def __init__(self, args=None):
        parser = argument_parser.parse_args()
        parsed_args = vars(parser.parse_args(args=args))
        # Create a copy to avoid accidental data poisoning
        self.__params = deepcopy(parsed_args)
    
    def __get_image(self) -> Image:
        '''
        Read the file provided by arguments and return the image.

        :return: The image given by arguments.
        :rtype: Image
        '''
        filepath = self.__params["filepath"]
        try:
            img = Image.open(filepath)
        except:
            raise ValueError("Provided file is not an image!")
        else:
            img = img.convert("1")
        return img

    def act(self):
        '''
        Process the parsed arguments, and run the qr-to-curve algorithm.
        '''
        img = self.__get_image()
        # TODO: The rest
        
    
