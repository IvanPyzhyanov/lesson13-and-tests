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
        with open('settings.json', 'r', encoding='utf-8') as f:
            try:
                cls.student_data = json.load(f)
            except:
                cls.student_data = []

    @classmethod
    def tearDownClass(cls):
        with open('settings.json', 'w', encoding='utf-8') as f:
            json.dump(cls.student_data, f, ensure_ascii=False, indent=4)

    def setUp(self):
        self.app = main.app.test_client()

    def test_form_is_rendering_and_shows_correct(self):
        soup = self.check_code_and_get_soup("/settings", 200)
        self.assertTrue(
            soup.form,
            "%@Проверьте, что при get-запросе на странице отрисовывается форма"
        )

    def test_form_attrs_is_ok(self):
        data=dict(
            project_name='test_name', 
            project_tagline='test2',
        )
        with open('settings.json', 'r', encoding='utf-8') as f:
            try:
                current_data = json.load(f)
            except:
                current_data = []
        start_len = len(current_data)
        response = self.app.post('/settings', data=data)
        self.assertNotIn(
            response.status_code, [500, 404, 400],
            r'%@Проверьте, что POST-запрос на адрес /settings обрабатывается без ошибок'
        )

        soup = BeautifulSoup(response.get_data(True), "html.parser")
        input_tags = soup.form.find_all('input')
        self.assertTrue(
            len(input_tags) == 3,
            "%@Проверьте, форма для ввода текста отрисовывается корректно"
        )

        for index, value in zip(range(2), data.values()):
            self.assertTrue(
                input_tags[index].attrs.get('value') == value,
                f"%@Проверьте, что в {index+1}-ом поле после отправки данных страница содержит обновленные сведения"
            )
        with open('settings.json', 'r', encoding='utf-8') as f:
            try:
                current_data = json.load(f)
            except:
                current_data = []

        self.assertEqual(
            current_data, data,
            "%@Проверьте что после POST-запроса на адрес и заполения формы, данные записываются в файл"
        )


if __name__ == "__main__":
    unittest.main()