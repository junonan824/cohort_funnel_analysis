import unittest
import pandas as pd
from scripts.cohort_analysis import cohort_analysis
from scripts.funnel_analysis import funnel_analysis

class TestAnalysisMethods(unittest.TestCase):

    def setUp(self):
        self.data = {
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
            'Qty_blog_readers': [1500, 1200, 300, 2700, 1400],
            'Buy_within_24_hrs': [150, 360, 15, 270, 25],
            'Buy_within_1_week': [75, 120, 15, 54, 140],
            'Buy_within_2_weeks': [75, 120, 15, 54, 70],
            'Buy_within_3_weeks': [30, 60, 0, 54, 0],
            'Click_through_no_buy': [225, 300, 75, 1080, 350],
            'No_click': [945, 240, 180, 1188, 490]
        }
        self.df = pd.DataFrame(self.data)

    def test_cohort_analysis(self):
        cohort_analysis(self.df)

    def test_funnel_analysis(self):
        funnel_analysis(self.df)

if __name__ == '__main__':
    unittest.main()