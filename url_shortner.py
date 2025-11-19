

import contextlib      #basic library hai 
from urllib.parse import urlencode
from urllib.request import urlopen


def get_tiny_url(url):                                                                                           #calling the lib
    request_url = 'http://tinyurl.com/api-create.php?'+urlencode({'url': url})

    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')
    


if __name__=='__main__':
    print(get_tiny_url("https://github.com/codexdevang"))   #here you can add ur website url and will get your output

