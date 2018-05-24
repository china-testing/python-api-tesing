class MockDBHelper:

    def connect(self, database="crimemap"):
        pass

    def add_crime(self, category, date, latitude, longitude, description):
        data = [category, date, latitude, longitude, description]
        for i in data:
            print (i, type(i))

    def get_all_crimes(self):
        return [{'latitude': -33.301304,
                 'longitude': 26.523355,
                 'date': "2000-01-01",
                 'category': "mugging",
                 'description': "mock description"}]

    def add_input(self, data):
        pass

    def clear_all(self):
        pass
