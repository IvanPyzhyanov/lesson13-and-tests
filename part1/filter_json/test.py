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


class FilterTestCase(SkyproTestCase, ResponseTestsMixin):

    def setUp(self):
        self.app = main.app.test_client()
        self.tours = [
            { "title": "Винный тур", "price_tur": 2000, "category": "bus" },
            { "title": "Тифлис - город модерна", "price_tur": 4900, "category": "walk" },
            { "title": "Квест-экскурсия по Тбилиси", "price_tur": 5800, "category": "quest" },
            { "title": "Лучшие панорамы вечернего города", "price_tur": 1800, "category": "walk"},
            { "title": "Болгар — Северная Мекка", "price_tur": 1800, "category": "bus" }
        ]


    def test_tours_is_available_and_works_correct(self):
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

    def test_tours_with_starts_filter_is_available_and_works_correct(self):
        url = '/tours?starts=4800'
        test_options = {
            "url": url,
            "method": 'GET',
            "code": [200],
            "student_response": self.app.get(
                url, json=""),
            "expected": list,
            "answer": [{ "title": "Тифлис - город модерна", "price_tur": 4900, "category": "walk" },
                       { "title": "Квест-экскурсия по Тбилиси", "price_tur": 5800, "category": "quest" }
            ]
        }
        response = self.check_status_code_jsonify_and_expected(**test_options)
        self.assertTrue(
            response.is_json,
            "%@Проверьте соответсвуют ли возвращаемые данные формату json"
        )

    def test_tours_with_ends_filter_is_available_and_works_correct(self):
        url = '/tours?ends=1800'
        test_options = {
            "url": url,
            "method": 'GET',
            "code": [200],
            "student_response": self.app.get(
                url, json=""),
            "expected": list,
            "answer": [{ "title": "Лучшие панорамы вечернего города", "price_tur": 1800, "category": "walk"},
                       { "title": "Болгар — Северная Мекка", "price_tur": 1800, "category": "bus" }
            ]
        }
        response = self.check_status_code_jsonify_and_expected(**test_options)
        self.assertTrue(
            response.is_json,
            "%@Проверьте соответсвуют ли возвращаемые данные формату json"
        )

    def test_tours_with_both_filter_is_available_and_works_correct(self):
        url = '/tours?starts=1800&ends=2000'
        test_options = {
            "url": url,
            "method": 'GET',
            "code": [200],
            "student_response": self.app.get(
                url, json=""),
            "expected": list,
            "answer": [{ "title": "Винный тур", "price_tur": 2000, "category": "bus" },
                       { "title": "Лучшие панорамы вечернего города", "price_tur": 1800, "category": "walk"},
                       { "title": "Болгар — Северная Мекка", "price_tur": 1800, "category": "bus" }
            ]
        }
        response = self.check_status_code_jsonify_and_expected(**test_options)
        self.assertTrue(
            response.is_json,
            "%@Проверьте соответсвуют ли возвращаемые данные формату json"
        )

if __name__ == "__main__":
    unittest.main()