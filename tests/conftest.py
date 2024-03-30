import os
import zipfile
import pytest
from qa_guru_python_10_7.utils import RESOURCES_DIR, ARCHIVE_DIR, FILES_LIST, TMP_DIR

@pytest.fixture
def create_archive():
    if not os.path.exists(RESOURCES_DIR):
        os.mkdir(RESOURCES_DIR)
    with zipfile.ZipFile(ARCHIVE_DIR, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in FILES_LIST:
            add_file = os.path.join(TMP_DIR, file)
            zf.write(add_file, os.path.basename(add_file))
    with zipfile.ZipFile(ARCHIVE_DIR, 'r') as zip_ref:
        zip_ref.extractall(TMP_DIR)
    yield TMP_DIR
    os.remove(ARCHIVE_DIR)