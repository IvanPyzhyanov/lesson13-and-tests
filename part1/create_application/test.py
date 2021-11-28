import sys
import unittest
from pathlib import Path
import os
import main
from bs4 import BeautifulSoup
import json

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import TemplateMixin
os.chdir(Path(os.path.abspath(__file__)).parent)


class SettingsTestCase(SkyproTestCase, TemplateMixin):

    @classmethod
    def setUpClass(cls):
        with open('enrollments.json', 'r', encoding='utf-8') as f:
            try:
                cls.student_data = json.load(f)
            except:
                cls.student_data = []

    @classmethod
    def tearDownClass(cls):
        with open('enrollments.json', 'w', encoding='utf-8') as f:
            json.dump(cls.student_data, f, ensure_ascii=False, indent=4)

    def setUp(self):
        self.app = main.app.test_client()

    def test_form_is_rendering_and_shows_correct(self):
        soup = self.check_code_and_get_soup("/enroll", 200)
        self.assertTrue(
            soup.form,
            "%@Проверьте, что при get-запросе на странице отрисовывается форма"
        )

    def test_form_attrs_is_ok(self):
        data=dict(
            name='test_user', 
            phone='727-72-77',
            email='test@sky.pro'
        )
        with open('enrollments.json', 'r', encoding='utf-8') as f:
            try:
                current_data = json.load(f)
            except:
                current_data = []
        start_len = len(current_data)
        response = self.app.post('/enroll', data=data)
        self.assertNotIn(
            response.status_code, [500, 404, 400],
            r'%@Проверьте, что POST-запрос на адрес /enroll обрабатывается без ошибок'
        )

        soup = BeautifulSoup(response.get_data(True), "html.parser")
        self.assertTrue(
            soup.text == 'Данные записаны',
            "%@Проверьте, что после отправки формы на странице выводится надпись 'Данные записаны'"
        )
        
        with open('enrollments.json', 'r', encoding='utf-8') as f:
            try:
                current_data = json.load(f)
            except:
                current_data = []
        finish_len = len(current_data)
        self.assertEqual(
            start_len + 1, finish_len,
            "%@Проверьте что после POST-запроса на адрес и заполения формы, данные записываются в файл"
        )
        for label in ['name', 'email', 'phone']:
            obj = current_data[-1].get(label)
            self.assertTrue(
                obj, f'%@Проверьте что при записи в файл в словаре сохраняются данные с ключём {label}'
            )


if __name__ == "__main__":
    unittest.main()