import base64 

def image_to_base64(image_name):
    image = open(image_name, 'rb')
    image_read = image.read()
    image_64_encode = base64.encodestring(image_read)
    return ("data:image+xml;base64," + image_64_encode.decode("utf-8"))
    #далее вставляем в html <img src="data:image+xml;base64,[base64]">, что позволит выводить фаотографии png,jpg, если надо svg, то <img src="data:image/svg+xml;base64,[base64]">
