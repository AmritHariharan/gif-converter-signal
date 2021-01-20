import logging

import azure.functions as func

from PIL import Image
from io import BytesIO


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('HTTP trigger function processing a request')

    img_gif = Image.open(BytesIO(req.get_body()))
    img_byte_arr = BytesIO()
    img_gif.save(img_byte_arr, format='webp', save_all=True, duration=img_gif.info['duration'], optimize=True, quality=100)

    logging.info('HTTP trigger function processed gif to webp')

    return func.HttpResponse(
        body=img_byte_arr.getvalue(),
        mimetype='image/webp',
        status_code=200
    )
