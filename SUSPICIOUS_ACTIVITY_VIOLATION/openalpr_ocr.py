import requests

def ocr(IMAGE_PATH):
        try:
                with open(IMAGE_PATH, 'rb') as fp:
                        response = requests.post(
                                'https://api.platerecognizer.com/v1/plate-reader/',
                                files=dict(upload=fp),
                                headers={'Authorization': 'Token b6f16704be75364f58a0d368c7541cf11e825ee9'})
                results = response.json()
                return (results['results'][0]['plate'])
        except:
                print("No number plate found")
