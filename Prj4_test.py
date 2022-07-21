import unittest
import pandas as pd
import matplotlib.pyplot as plt
from Project_4 import *




class Functions_Tester(unittest.TestCase):

    def setUp(self):
        try:
            self.__df = pd.read_csv('test_df1.csv')
            self.__df2 = pd.read_csv('test_df2.csv') 
            self.__emp = pd.read_csv('US_Unemployment_Oct2012.csv', index_col = 0)
        except BaseException as e:
            print(e)
            print('Testing failed.')

    def test_make_subset_data_no_vars(self):
        print('\n\nTest subset_data no inputs')
        try:
                result = make_subset(self.__df)
                cur_id = id(self.__df)
                result_id = id(result)
                expected = make_subset(self.__df)
                print('Result\n',result, '\n')
                print('Expected\n',expected, '\n')
                print('Checking for equal content of data frames')
                self.assertTrue(result.equals(expected))
                print('Checking to make sure df is a copy')
                self.assertFalse(result_id == cur_id)
        except BaseException as e:
                print(e)
                print('Testing failed.')
                
    def test_make_subset_multi_region(self):
        print('\n\nTest make_subset region only')
        print('regions are Eastern_Europe_and_Central_Asia,South_Asia')
        try:
                result = make_subset(self.__df, region = ['Eastern_Europe_and_Central_Asia','South_Asia'])
                result.index = list(range(len(result.index)))
                expected = pd.read_csv('result1.txt')
                print('Result\n',result, '\n')
                print('Expected\n',expected, '\n')
                print('Checking for equal content of data frames')
                self.assertTrue(result.equals(expected))
        except BaseException as e:
                print(e)
                print('Testing failed.')
                
                
    def test_make_subset_multi_year(self):
        print('\n\nTest make_subset year only')
        print('years are 2014 and 2016')
        try:
                result = make_subset(self.__df2, year = ['2014','2016'])
                result.index = list(range(len(result.index)))
                expected = pd.read_csv('result2.txt')
                print('Result\n',result, '\n')
                print('Expected\n',expected, '\n')
                print('Checking for equal content of data frames')
                self.assertTrue(result.equals(expected))
        except BaseException as e:
                print(e)
                print('Testing failed.')
    
    def test_make_subset_region_year(self):
        print('\n\nTest make_subset region and year')
        print('region is Middle_East_and_North_Africa years are 1989, 1993, 2010')
        try:
                result = make_subset(self.__df2, region = ['Middle_East_and_North_Africa'], year = ['1989','1993','2010'])
                result.index = list(range(len(result.index)))
                expected = pd.read_csv('result4.txt')
                print('Result\n',result, '\n')
                print('Expected\n',expected, '\n')
                print('Checking for equal content of data frames')
                self.assertTrue(result.equals(expected))
        except BaseException as e:
                print(e)
                print('Testing failed.')
                
    def test_make_subset_one_vaccine_only(self):
        print('\n\nTest make_subset one vaccine only')
        print('vaccine is RCV1')
        try:
                result = make_subset(self.__df, vaccine = ['RCV1'])
                result.index = list(range(len(result.index)))
                expected = pd.read_csv('result3.txt')
                print('Result\n',result, '\n')
                print('Expected\n',expected, '\n')
                print('Checking for equal content of data frames')
                self.assertTrue(result.equals(expected))
        except BaseException as e:
                print(e)
                print('Testing failed.')
                
    def test_make_subset_region_vaccine_year(self):
        print('\n\nTest make_subset region, vaccine, year')
        print('regions are Global, Western Europe, years are 2010, 2016, 2008, vaccine is HEPBB')
        try:
                result = make_subset(self.__df2, region = ['Global','Western_Europe']\
                                     , vaccine = ['HEPBB'], year = ['2010', '2016', '2018'])
                result.index = list(range(len(result.index)))
                expected = pd.read_csv('result5.txt')
                print('Result\n',result, '\n')
                print('Expected\n',expected, '\n')
                print('Checking for equal content of data frames')
                self.assertTrue(result.equals(expected))
        except BaseException as e:
                print(e)
                print('Testing failed.')

                
#testing make_plot function

    def test_make_plot_data_base(self):
        print('\n\nTest make_plot_data_base')
        try:
            ser = pd.Series(self.__emp.Unemployment, self.__emp.index)
            result = make_plot(ser)
            #fig = result.get_figure()
            plt.savefig('make_plot_bar.png')
            plt.clf()
            plt.cla()
            plt.close()
        except BaseException as e:
            print(e)
            print('Testing failed.')
            
    def test_make_plot_line(self):
        print('\n\nTest make_plot line plot')
        try:
            ser = pd.Series(self.__emp.Unemployment, self.__emp.index)
            result = make_plot(ser, bar = False)
            #fig = result.get_figure()
            plt.savefig('make_plot_line.png')
            plt.clf()
            plt.cla()
            plt.close()
        except BaseException as e:
            print(e)
            print('Testing failed.')
            
    def test_make_plot_title_line(self):
        print('\n\nTest make_plot mention title as line plot')
        try:
            ser = pd.Series(self.__emp.Unemployment, self.__emp.index)
            result = make_plot(ser, title='Unemp_Data', bar = False)
            #fig = result.get_figure()
            plt.savefig('make_plot_title.png')
            plt.clf()
            plt.cla()
            plt.close()
        except BaseException as e:
            print(e)
            print('Testing failed.')
          

if __name__ == '__main__':
  unittest.main()