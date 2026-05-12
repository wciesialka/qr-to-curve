import argparse
import os
from pathlib import Path

def _readable_file_argparse_type(path: str):
    try:
        filepath = Path(path).resolve(strict=True)
    except:
        raise ValueError(f"File {path} does not exist.")
    else:
        if not filepath.is_file():
            raise ValueError(f"File {filepath} is not a file.")
        if not os.access(filepath, os.R_OK):
            raise ValueError(f"File {filepath} is not readable.")
        return path

def get_parser() -> argparse.ArgumentParser:
    '''
    Get the CLI's internal argument parser.

    :return: The argument parser.
    :rtype: argparse.ArgumentParser
    '''
    parser_opts = {
        "description": "Convert qr codes to curves.",
        "epilog": """Please ensure QR codes follow the following format:
                        - Black and white
                        - PNG file format
                        - 300 DPI
                        - Module Size of 4
                   If you do not follow these specifications, the script is not guaranteed to work."""
    }
    parser = argparse.ArgumentParser(**parser_opts)
    parser.add_argument("image_file", 
        type=_readable_file_argparse_type,
        help="The path of the QR code image.")
    return parser