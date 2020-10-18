from flask import Flask,render_template,request

import running_youtube
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search_topic")
def search_topic():
    return render_template("search_topic.html")

@app.route("/ans",methods = ['POST', 'GET'])
def ans():
   if request.method == 'POST':
      result = request.form
      url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/4f926a80-ab91-46c0-88e4-341f6e1ce08b/classify/iterations/Iteration2/url?"
      payload = 'Url=https%3A//i1.wp.com/www.kalimbatutorials.com/wp-content/uploads/2020/05/Imahe-By-Magnus-Haven-Kalimba-Tabs-1-e1590120483133.jpg%3Fresize%3D1080%252C607%26ssl%3D1'
      headers = {'Prediction-Key': 'de012887ce6147f18b0b2e27c3228860','ontent-Type': 'application/json','Content-Type': 'application/x-www-form-urlencoded'}

      response = requests.request("POST", url, headers=headers, data = payload)

      answer=response.json()['predictions'][2]['tagName']

      return render_template("ans.html",value=answer)
if __name__ == "__main__":
    app.run(debug=True)
