from spyre import server

import pandas as pd


class Lab2(server.App):

    title = "lab2"

    inputs = [{"type":'dropdown',"label":'Region', "options":[{"label":"Cherkasy","value": "1"},{"label":"Chernihiv","value": "2"},{"label":"Chernivtsi","value": "3"},
                                                              {"label":"Crimea","value": "4"},{"label":"Dnipro","value": "5"},{"label":"Donets`k","value": "6"},
                                                              {"label":"Ivano-Frankivsk","value": "7"},{"label":"Kharkiv","value": "8"},{"label":"Kherson","value": "9"},
                                                              {"label":"Khmelnitskiy","value": "10"},{"label":"Kiev","value": "11"},{"label":"Kiev City","value": "12"},
                                                              {"label":"Kirovograd","value": "13"},{"label":"Luhansk","value": "14"},{"label":"Lviv","value": "15"},
                                                              {"label":"Mykolaiv","value": "16"},{"label":"Odessa","value": "17"},{"label":"Poltava","value": "18"},
                                                              {"label":"Rivne","value": "19"},{"label":"Sevastopol","value": "20"},{"label":"Sumy","value": "21"},
                                                              {"label":"Ternopil","value": "22"},{"label":"Transcarpathia","value": "23"},{"label":"Vinnitsya","value": "24"},
                                                              {"label":"Volyn","value": "25"},{"label":"Zaporizhzhya","value": "26"},{"label":"Zhytomyr","value": "27"}],
               "key":'ticker',"action_id":"update_data"},

              {"type":'dropdown',"label":'Year',"options":[{"label":"1981", "value":"1981"},{"label":"1982", "value":"1982"},{"label":"1983", "value":"1983"},{"label":"1984", "value":"1984"},
                                                           {"label": "1985", "value": "1985"},{"label":"1986", "value":"1986"},{"label":"1987", "value":"1987"},{"label":"1988", "value":"1988"},
                                                           {"label": "1989", "value": "1989"},{"label":"1990", "value":"1990"},{"label":"1991", "value":"1991"},{"label":"1992", "value":"1992"},
                                                           {"label": "1993", "value": "1993"},{"label":"1994", "value":"1994"},{"label":"1995", "value":"1995"},{"label":"1996", "value":"1996"},
                                                           {"label": "1997", "value": "1997"},{"label":"1998", "value":"1998"},{"label":"1999", "value":"1999"},{"label":"2000", "value":"2000"},
                                                           {"label": "2001", "value": "2001"},{"label":"2002", "value":"2002"},{"label":"2003", "value":"2003"},{"label":"2004", "value":"2004"},
                                                           {"label": "2005", "value": "2005"},{"label":"2006", "value":"2006"},{"label":"2007", "value":"2007"},{"label":"2008", "value":"2008"},
                                                           {"label": "2009", "value": "2009"},{"label":"2010", "value":"2010"},{"label":"2011", "value":"2011"},{"label":"2012", "value":"2012"},
                                                           {"label": "2013", "value": "2013"},{"label":"2014", "value":"2014"},{"label":"2015", "value":"2015"},{"label":"2016", "value":"2016"},
                                                           {"label": "2017", "value": "2017"}],
               "key":'year',"action_id":"update_data"},
              {"type":'dropdown',"label":'With',"options": [{"label": "1", "value": "1"}, {"label": "2", "value": "2"},
                                                            {"label": "3", "value": "3"}, {"label": "4", "value": "5"},
                                                            {"label": "5", "value": "5"}, {"label": "6", "value": "6"},
                                                            {"label": "7", "value": "7"}, {"label": "8", "value": "8"},
                                                            {"label": "9", "value": "9"}, {"label": "10", "value": "10"},
                                                            {"label": "11", "value": "11"}, {"label": "12", "value": "12"},
                                                            {"label": "13", "value": "12"}, {"label": "14", "value": "14"},
                                                            {"label": "15", "value": "15"}, {"label": "16", "value": "16"},
                                                            {"label": "17", "value": "17"}, {"label": "18", "value": "18"},
                                                            {"label": "19", "value": "19"}, {"label": "20", "value": "20"},
                                                            {"label": "21", "value": "21"}, {"label": "22", "value": "22"},
                                                            {"label": "23", "value": "23"}, {"label": "24", "value": "24"},
                                                            {"label": "25", "value": "25"}, {"label": "26", "value": "26"},
                                                            {"label": "27", "value": "27"}, {"label": "28", "value": "28"},
                                                            {"label": "29", "value": "29"}, {"label": "30", "value": "30"},
                                                            {"label": "31", "value": "31"}, {"label": "32", "value": "32"},
                                                            {"label": "33", "value": "33"}, {"label": "34", "value": "34"},
                                                            {"label": "35", "value": "35"}, {"label": "36", "value": "36"},
                                                            {"label": "37", "value": "37"}, {"label": "38", "value": "38"},
                                                            {"label": "39", "value": "39"}, {"label": "40", "value": "40"},
                                                            {"label": "41", "value": "41"}, {"label": "42", "value": "42"},
                                                            {"label": "43", "value": "43"}, {"label": "44", "value": "44"},
                                                            {"label": "45", "value": "45"}, {"label": "46", "value": "46"},
                                                            {"label": "47", "value": "47"}, {"label": "48", "value": "48"},
                                                            {"label": "49", "value": "49"}, {"label": "50", "value": "50"},
                                                            {"label": "51", "value": "51"}, {"label": "52", "value": "52"}],
               "key":'week1',"action_id":"update_data"},
              {"type": 'dropdown', "label": 'Before',
               "options": [{"label": "1", "value": "1"}, {"label": "2", "value": "2"},
                           {"label": "3", "value": "3"}, {"label": "4", "value": "5"},
                           {"label": "5", "value": "5"}, {"label": "6", "value": "6"},
                           {"label": "7", "value": "7"}, {"label": "8", "value": "8"},
                           {"label": "9", "value": "9"}, {"label": "10", "value": "10"},
                           {"label": "11", "value": "11"}, {"label": "12", "value": "12"},
                           {"label": "13", "value": "12"}, {"label": "14", "value": "14"},
                           {"label": "15", "value": "15"}, {"label": "16", "value": "16"},
                           {"label": "17", "value": "17"}, {"label": "18", "value": "18"},
                           {"label": "19", "value": "19"}, {"label": "20", "value": "20"},
                           {"label": "21", "value": "21"}, {"label": "22", "value": "22"},
                           {"label": "23", "value": "23"}, {"label": "24", "value": "24"},
                           {"label": "25", "value": "25"}, {"label": "26", "value": "26"},
                           {"label": "27", "value": "27"}, {"label": "28", "value": "28"},
                           {"label": "29", "value": "29"}, {"label": "30", "value": "30"},
                           {"label": "31", "value": "31"}, {"label": "32", "value": "32"},
                           {"label": "33", "value": "33"}, {"label": "34", "value": "34"},
                           {"label": "35", "value": "35"}, {"label": "36", "value": "36"},
                           {"label": "37", "value": "37"}, {"label": "38", "value": "38"},
                           {"label": "39", "value": "39"}, {"label": "40", "value": "40"},
                           {"label": "41", "value": "41"}, {"label": "42", "value": "42"},
                           {"label": "43", "value": "43"}, {"label": "44", "value": "44"},
                           {"label": "45", "value": "45"}, {"label": "46", "value": "46"},
                           {"label": "47", "value": "47"}, {"label": "48", "value": "48"},
                           {"label": "49", "value": "49"}, {"label": "50", "value": "50"},
                           {"label": "51", "value": "51"}, {"label": "52", "value": "52"}],
               "key": 'week2', "action_id": "update_data"},
              ]
    controls = [{ "type" : "hidden","id" : "update_data"}]

    tabs = [ "Table", "Plot"]

    outputs = [ { "type" : "plot",
                                "id" : "plot",
                                "control_id" : "update_data",
                                "tab" : "Plot" },
                { "type" : "table",
                                "id" : "table_id",
                                "control_id" : "update_data",
                                "tab" : "Table",
                                "on_page_load" : True }]
    def getData(self, params):
            ticker = params['ticker']

            year = int(params['year'])
            week1 = int(params['week1'])
            week2 = int(params['week2'])

            df = pd.read_csv('vhi_id_{} 2017 04 02.csv'.format(ticker), index_col=False, header=1, skipfooter=1, engine='python',
                             names=['year', 'week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI'], delimiter='\,\s+|\s+|\,')

            df = df[(df['year'] == year) & (df['week'] >= week1) & (df['week'] <= week2)]

            return df


    def getPlot(self, params):
        df = self.getData(params).set_index('week').drop(['year'], axis=1)

        plt_obj = df.plot()
        plt_obj.set_ylabel("value")
        plt_obj.set_title('Diagram')
        fig = plt_obj.get_figure()
        return fig


app =Lab2()
app.launch(port=9093)