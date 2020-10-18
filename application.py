from flask import Flask,render_template,request

import running_youtube
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search_topic")
def search_topic():
    return render_template("search_topic.html")

@app.route("/result",methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      data={"Url":"https://i1.wp.com/www.kalimbatutorials.com/wp-content/uploads/2020/05/Imahe-By-Magnus-Haven-Kalimba-Tabs-1-e1590120483133.jpg?resize=1080%2C607&ssl=1"}
      headers = {'Prediction-Key':'de012887ce6147f18b0b2e27c3228860','Content-Type': 'application/json'}  
      r = requests.post(url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/4f926a80-ab91-46c0-88e4-341f6e1ce08b/classify/iterations/Iteration2/url?", data = data,headers=headers)
      
      return render_template("result.html",result = r,url=img_url)
if __name__ == "__main__":
    app.run(debug=True)
