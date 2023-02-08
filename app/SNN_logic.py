'''Contains static class for SNNs

Welcome to to SNN mini database. Check your SNN or check if it is in the database.'''

import datetime
import pandas as pd

# Create class SNN
class SNN:

    def __init__(self, snns: list):
        # Create dataframe from SNNs
        self.snn_df = pd.DataFrame(snns, columns=['snn'])
        self.snn_df = self.snn_df[self.snn_df['snn'].apply(lambda x: self.valid(x))]
        self.snn_df['gender'] = self.snn_df['snn'].apply(lambda x: 'woman' if int(x[8])%2 == 0 else 'man')

    def valid(self, snn: str):

        if not isinstance(snn, str):
            return False
        if len(snn) != 11:
            return False
        try: 
            datetime.datetime.strptime(snn[0:6], '%d%m%y')
        except:
            return False
        
        control_1 = [3, 7, 6, 1, 8, 9, 4, 5, 2, 1]
        control_2 = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
        snn = [int(x) for x in snn]

        total = 0
        for x, y in zip (snn[:10], control_1):
            total += x*y
        if total % 11 != 0:
            return False
        
        total = 0
        for x, y in zip (snn[:11], control_2):
            total += x*y
        if total % 11 != 0:
            return False

        return True

    def is_among_given_snns(self, snn):
        return True if snn in self.snn_df['snn'].values else False

    def gender(self, snn: str):
        return 'Woman' if int(snn[8]) % 2 == 0 else 'Man'
    
    def age(self, snn: str) -> int:

        if self.valid(snn):

            # Get current year
            current_year = datetime.datetime.now().year

            # Get year of birth from SNN
            year_of_birth = snn[4:6]
            control_number = int(snn[6:9])

            '''
            Rules:

            000–499 omfatter personer født i perioden 1900–1999.
            500–749 omfatter personer født i perioden 1854–1899.
            500–999 omfatter personer født i perioden 2000–2039.
            900–999 omfatter personer født i perioden 1940–1999.
            '''
            
            if control_number < 500:
                year_of_birth = '19' + year_of_birth
            elif 500 <= control_number <= 999 and int(snn[4:6]) < 40:
                year_of_birth = '20' + year_of_birth
            elif 500 <= control_number <= 749 and 54 <= int(snn[4:6]) <= 99:
                year_of_birth = '18' + year_of_birth
            elif 900 <= control_number <= 999 and 40 <= int(snn[4:6]) <= 99:
                year_of_birth = '19' + year_of_birth
            else:
                year_of_birth = '19' + year_of_birth
            
            # Get age
            age = current_year - int(year_of_birth)

            # Determine if snn has haf birthday yet
            current_day = datetime.datetime.today()
            try:
                snn_day = datetime.datetime.strptime(snn[:6], '%d%m%y').replace(year=current_year)
            except ValueError:
                snn_day = datetime.datetime.strptime(snn[:6], '%d%m%y').replace(year=current_year, day=28)

            if current_day < snn_day and age != 0:
                age = age - 1

            return age
        else:
            raise ValueError("SNN is not valid. SNN is " + snn + ".")
    
    def count_by_gender(self) -> dict:
        
        return self.snn_df['gender'].value_counts().to_dict()

    def count_by_gender_by_age(self):
        '''Returns {man: {11: 0, 12: 1, 13: 3, ...}, woman: {11: 0, 12: 1, 13: 3, ...}}'''

        # Create empty dictionary
        men_women = {'man': dict(), 'woman': dict()}

        for snn in self.snn_df['snn']:
            age = self.age(snn)

            if age == 'None':
                continue
            
            if self.gender(snn) == 'Man':
                if age not in men_women['man'].keys():
                    men_women['man'][age] = 1
                else:
                    men_women['man'][age] += 1
            else:
                if age not in men_women['woman'].keys():
                    men_women['woman'][age] = 1
                else:
                    men_women['woman'][age] += 1
            
        # Sort dictionary by age key
        men_women['man'] = dict(sorted(men_women['man'].items()))
        men_women['woman'] = dict(sorted(men_women['woman'].items()))

        return men_women

