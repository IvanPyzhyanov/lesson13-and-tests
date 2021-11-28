import sys
import unittest
from pathlib import Path
import os
import main
from bs4 import BeautifulSoup

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import TemplateMixin
os.chdir(Path(os.path.abspath(__file__)).parent)


class FileTestCase(SkyproTestCase, TemplateMixin):
    @classmethod
    def setUpClass(self):
        self.app = main.app.test_client()
        self.filename = 'testfile.txt'
        with open(self.filename, 'w') as f:
           f.write('test test test')
    
    @classmethod
    def tearDownClass(self):
        os.remove(self.filename)
        filepath = Path(os.path.abspath(__file__)).parent.joinpath("uploads", self.filename)
        if filepath.exists():
            os.remove(filepath)

    def test_form_is_rendering_and_shows_correct(self):
        soup = self.check_code_and_get_soup("/", 200)
        self.assertTrue(
            soup.form,
            "%@Проверьте, что при get-запросе на адрес / отрисовывается форма"
        )

    def test_try_upload_file(self):
        file = open(self.filename, 'rb')
        response = self.app.post('/upload', data={"thefile": file}, content_type='multipart/form-data')
        self.assertTrue(
            response.status_code==200,
            ('%@Проверьте, что при post-запросе на адрес /upload с загрузкой файла '
             'не происходит ошибок'
        ))
        
        soup = BeautifulSoup(response.get_data(True), "html.parser")
        self.assertTrue(
            soup.text == "Файл загружен",
            "%@Проверьте, что после загрузки файла возвращается сообщение 'Файл загружен'"
        )

        self.path = Path(os.path.abspath(__file__)).parent.joinpath("uploads", self.filename)
        self.assertTrue(
            self.path.exists(),
            "%@Проверьте, что при загрузке файла он сохраняется в директории 'uploads' в корне папки с заданием"
        )


if __name__ == "__main__":
    unittest.main()