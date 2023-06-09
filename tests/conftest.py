import gzip
import os
import shutil

import pytest
import requests


@pytest.fixture(scope="session")
def A_dataset(tmp_path_factory):
    temp_dir = tmp_path_factory.mktemp("data")

    # url 이용해서 다운로드
    urls = [
        "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz",
        "http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz",
        "http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz",
        "http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz",
    ]
    filenames = [
        "train-images-idx3-ubyte.gz",
        "train-labels-idx1-ubyte.gz",
        "t10k-images-idx3-ubyte.gz",
        "t10k-labels-idx1-ubyte.gz",
    ]

    for url, filename in zip(urls, filenames):
        file_path = temp_dir / filename

        response = requests.get(url)
        with open(file_path, "wb") as f:
            f.write(response.content)

        # 다운로드 받은 데이터셋 압축풀기
        with gzip.open(file_path, "rb") as f_in:
            with open(temp_dir / filename[:-3], "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)

        # 다운로드한 압축 파일 삭제
        os.remove(file_path)

    return temp_dir
