from flask import Flask, render_template
from modules import convert_to_dict

app = Flask(__name__)
application = app

# create a list of dicts from a CSV
bees_list = convert_to_dict("beesknees.csv")

pairs_list = []
for b in bees_list:
    pairs_list.append( ( b['Number'], b['Name']) )
#first is the worst
@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, the_title="Bees Index")

#second is the best!
@app.route('/bee/<num>')

def detail(num):
    try:
        be_dict = bees_list[int(num)-1]
    except:
        return f"<h1>Invalid value for a bee: {num}</h1>"
    #you do need this! but you could possibly remove ord
    return render_template('bee.html', knees=be_dict, the_title=be_dict['Name'])

if __name__ == '__main__':
    app.run(debug=True)
