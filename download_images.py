import time
import requests
import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1676868720246-d608555dd3ba',
    'https://images.unsplash.com/photo-1676737830610-2cebe4843eca',
    'https://images.unsplash.com/photo-1676845578082-2e08e7c359b4',
    'https://images.unsplash.com/photo-1627209876750-9db65322c4ed',
    'https://images.unsplash.com/photo-1676595670250-626d402700e0',
    'https://images.unsplash.com/photo-1653219305693-28ad4baf623a',
    'https://images.unsplash.com/photo-1677040628614-53936ff66632',
    'https://images.unsplash.com/photo-1676920410907-8d5f8dd4b5ba',
    'https://images.unsplash.com/photo-1676846631735-e10bf09d49d8',
    'https://images.unsplash.com/photo-1676765374032-57d90e318b8f',
    'https://images.unsplash.com/photo-1676625196031-b8b0d11c9172',
    'https://images.unsplash.com/photo-1676798635656-b78321e08eb5',
    'https://images.unsplash.com/photo-1676798385570-8fabdbf995ec',
    'https://images.unsplash.com/photo-1676744625189-48f9f6ad077f',
]


def image_downloader(img_url: str) -> None:
    """Downloads the image from the given URL.

    :param img_url: URL of the image.
    :return: None
    """
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'Downloaded the image: {img_name}')


if __name__ == '__main__':
    start_time = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(image_downloader, img_urls)

    end_time = time.perf_counter()

    print(f'Using threading finished in {end_time-start_time} seconds.')