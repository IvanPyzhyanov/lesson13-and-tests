import sys
import unittest
from pathlib import Path
import os
import main

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import TemplateMixin


class SettingsTestCase(SkyproTestCase, TemplateMixin):
    def setUp(self):
        self.app = main.app.test_client()

    def test_get_query_param_page(self):
        soup = self.check_code_and_get_soup("/tours", 200)
        self.assertTrue(
            soup.h1.text == "Найдено: 0",
            "%@Проверьте что если параметр не задан, то на странице после формы отображается "
            "текст 'Найдено: 0'"
        )
    def test_tour_not_found(self):
        soup = self.check_code_and_get_soup("/tours?s=qwe", 200)
        self.assertTrue(
            soup.h1.text == "Найдено: 0",
            "%@Проверьте что если туров не найдено, то на странице отображается заголовок h1 с текстом текст 'Найдено: 0'"
        )
    def test_tour_search_two_elem(self):
        main_tag = self.check_code_and_get_soup("/tours?s=ро", 200)
        h2 = main_tag.h1
        self.assertTrue(
            h2.text == "Найдено: 2",
            ("%@Проверьте что, надпись в заголовке h1 отображается верно, а также правильно "
             "считается количество найденных туров")
        )
        html_list_numbers = main_tag.ul
        self.assertIsNotNone(
            html_list_numbers,
            "%@Проверьте, что добавили тег 'Маркированный список'")
        li_elements = html_list_numbers.find_all('li')
        len_elements = len(li_elements)
        self.assertEqual(
            len_elements, 2,
            ("%@Проверьте что добавляются все элементы списка."
             f" Должно быть 2, тогда как у вас {len_elements}"))

    def test_tour_search_one_elem(self):
        main_tag = self.check_code_and_get_soup("/tours?s=ви", 200)
        h2 = main_tag.h1
        self.assertTrue(
            h2.text == "Найдено: 1",
            ("%@Проверьте что, надпись в заголовке h1 отображается верно, а также правильно "
             "считается количество найденных туров")
        )
        html_list_numbers = main_tag.ul
        self.assertIsNotNone(
            html_list_numbers,
            "%@Проверьте, что добавили тег 'Маркированный список'")
        li_elements = html_list_numbers.find_all('li')
        len_elements = len(li_elements)
        self.assertEqual(
            len_elements, 1,
            ("%@Проверьте что добавляются все элементы списка."
             f" Должно быть 1, тогда как у вас {len_elements}"))


if __name__ == "__main__":
    unittest.main()