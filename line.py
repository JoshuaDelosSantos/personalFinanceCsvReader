"""
A transactional 'line' class that initialises a line object.
By: Joshua Delos Santos
"""

from datetime import datetime

CATEGORY_TO_TEXTS = {
    'Grocery': ['WOOLWORTHS', 'COLES', '2234', '4527', '2462', '4494'],
    'Travel': ['AIRBNB', 'HOTEL', 'GRAB', 'FOREIGN FEE', 'FRGN'],
    'Dining': ['RESTAURANT', 'CAFE', 'FOOD', 'EATERY', 'MCDONALDS', 'SUSHI', 'VIETNAMESE'],
    'Shopping': ['KMART', 'SHOP', 'CLOTHING', 'RETAIL', 'MARKET', 'BIG W', 'REBEL', 'WILLOWS', '1034', '0287', 'SPORT'],
    'Utilities': ['BILL', 'OPTUS', 'TELSTRA', 'PREPAID'],
    'Acc Deposits': ['SALARY', 'PAYROLL', 'PAYMENT', 'DEPOSIT'],
    'Entertainment': ['NETFLIX', 'SPOTIFY', 'STREAMING', 'MOVIE', 'CRUNCHYROLL'],
    'Health and Fitness': ['GYM', 'FITNESS', 'WORKOUT', 'JIMRHONDASFIT', 'CHEMIST'],
    'Transfer': ['TRANSFER', 'TFR', 'PAYMENT TO'],
    'Other': ['WITHDRAWAL', 'DEPOSIT-OSKO PAYMENT', 'WITHDRAWAL-OSKO PAYMENT', 'AITKENVALE', 'DOUGLAS', 'TOWNSVILLE',
              'BRISBANE', 'THURINGOWA', 'HANDYBANK']
}


class Line:

    def __init__(self, date_string: str, description: str, debited, credited):
        """Initialise line object."""
        self.date = datetime.strptime(date_string, '%d/%m/%Y')
        self.description = description
        self.debited = debited
        self.credited = credited

    def __str__(self):
        return f"{self.date.date()},{self.description},{self.debited},{self.credited}"

    def determine_category(self):
        """Categorize transaction based on description."""
        parts = self.description.upper().split(' ')

        for category, texts in CATEGORY_TO_TEXTS.items():
            if any(keyword in parts for keyword in texts):
                return category

        return 'Uncategorized'
