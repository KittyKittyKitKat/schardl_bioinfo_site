# Copyright (c) 2023 Nyx Harris-Palmer, Tharanie Subramaniam

from pathlib import Path
import json

def build_manifest():
    static_path = Path('bioinfo_site') / 'static'
    images_path = static_path  / 'images' / 'slideshow'

    image_names = []

    for image_file in images_path.glob('*'):
        image_names.append(image_file.name)

    with open(static_path / 'slideshow_manifest.json', 'w') as fp:
        json.dump(image_names, fp)

build_manifest()