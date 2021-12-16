import unittest
from HomePageTest import HomePageTest
from SearchHealthCentresTest import SearchHealthCentresTest
from SearchMedInfoTest import SearchMedInfoTest
from EnglishArticlesTest import EnglishArticleTest

# get all tests from classes
Search_HealthCentres_Tests = unittest.TestLoader().loadTestsFromTestCase(
    SearchHealthCentresTest
)
Search_MedInfo_Tests = unittest.TestLoader().loadTestsFromTestCase(SearchMedInfoTest)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
English_Articles_Tests = unittest.TestLoader().loadTestsFromTestCase(EnglishArticleTest)

# create a test suite combining other test classes
smoke_tests = unittest.TestSuite(
    [
        home_page_tests,
        Search_HealthCentres_Tests,
        Search_MedInfo_Tests,
        English_Articles_Tests,
    ]
)
# run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_tests)
