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
os.chdir(Path(os.path.abspath(__file__)).parent)


class CategoryTestCase(SkyproTestCase, TemplateMixin):

    def setUp(self):
        self.app = main.app.test_client()

    def test_form_is_rendering_and_shows_correct(self):
        soup = self.check_code_and_get_soup("/tours", 200)
        self.assertTrue(
            soup.form,
            "%@Проверьте, что при get-запросе на адрес /tours отрисовывается форма"
        )

        li_elements = soup.ul.find_all('li')
        self.assertTrue(
            len(li_elements) == 5,
            "%@Проверьте что при отсутствии условия выводится полный список туров"
        )
        self.assertTrue(
            li_elements[0].text == 'Винный тур',
            ("%@Проверьте что список отображаемых элементов списка "
             "содержит только названия и отсутствуют лишние пробелы")
        )

    def test_if_tours_not_found_render_all(self):
        soup = self.check_code_and_get_soup("/tours?category=sqwf", 200)
        li_elements = soup.ul.find_all('li')
        self.assertTrue(
            len(li_elements)==5,
            ("%@Проверьте, что если туры, удовлетворяющие условиям поиска не найдены, "
             "то возвращается их полный список")
        )


    def test_search_bus_works_correct(self):
        soup = self.check_code_and_get_soup("/tours?category=bu", 200)
        li_elements = soup.ul.find_all('li')
        self.assertTrue(
            len(li_elements) == 2,
            "%@Проверьте что поиск по категориям работает корректно"
        )

    def test_search_quest_works_correct(self):
        soup = self.check_code_and_get_soup("/tours?category=qu", 200)
        li_elements = soup.ul.find_all('li')
        self.assertTrue(
            len(li_elements) == 1,
            "%@Проверьте что поиск по категориям работает корректно"
        )
        soup = self.check_code_and_get_soup("/tours?category=Qu", 200)
        li_elements = soup.ul.find_all('li')
        self.assertTrue(
            len(li_elements) == 1,
            "%@Проверьте при поиске по категориям не учитывается регистр"
        )

if __name__ == "__main__":
    unittest.main()