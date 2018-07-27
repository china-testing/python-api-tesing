import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from flask import Flask
import numpy as np
import io

app = Flask(__name__)

@app.route('/plot')
def build_plot():

    # Generate the plot
    x = np.linspace(0, 10)
    line, = plt.plot(x, np.sin(x))

    f = io.BytesIO()
    plt.savefig(f, format='png')

    # Serve up the data
    header = {'Content-type': 'image/png'}
    f.seek(0)
    data = f.read()

    return data, 200, header

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000, debug=True)

