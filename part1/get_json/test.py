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
from ttools.skyprotests.tests_mixins import ResponseTestsMixin
os.chdir(Path(os.path.abspath(__file__)).parent)


class SettingsTestCase(SkyproTestCase, ResponseTestsMixin):

    def setUp(self):
        self.app = main.app.test_client()
        self.tours = [
            { "title": "Винный тур", "price_rur": 2000, "category": "bus" },
            { "title": "Тифлис - город модерна", "price_rur": 4900, "category": "walk" },
            { "title": "Квест-экскурсия по Тбилиси", "price_rur": 5800, "category": "quest" },
            { "title": "Лучшие панорамы вечернего города", "price_rur": 1800, "category": "walk"},
            { "title": "Болгар — Северная Мекка", "price_rur": 1800, "category": "bus" }
        ]


    def test_view_books_get_is_available_and_works_correct(self):
        url = '/tours'
        test_options = {
            "url": url,
            "method": 'GET',
            "code": [200],
            "student_response": self.app.get(
                url, json=""),
            "expected": list,
            "answer": self.tours
        }
        response = self.check_status_code_jsonify_and_expected(**test_options)
        self.assertTrue(
            response.is_json,
            "%@Проверьте соответсвуют ли возвращаемые данные формату json"
        )


if __name__ == "__main__":
    unittest.main()