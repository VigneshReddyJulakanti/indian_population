from flask import Flask,render_template,request

import pickle

app=Flask(__name__)
 
model=pickle.load(open("model/pop.pkl",'rb')) 

def convert_to_string_with_comma(ans):
        ans=int(ans[0])
        ans=str(ans)
        ans=ans[::-1]
        fans=""
        for i in range(0,len(ans),3):
            fans+=f"{ans[i:i+3]},"
        fans=fans[::-1]
        fans=fans[1:]
        return fans

@app.route('/')
def home():
    return render_template("home2.html")

@app.route('/submitted',methods=['POST'])
def submitted():
    if request.method=="POST":
        year=request.form["year"]
        year=int(year)
        ans=model.predict([[year]])

        ans=convert_to_string_with_comma(ans)
        

    
        return render_template("home2.html",ans=f"The population of India in {year} is {ans}",year=year)



if __name__ =="__main__":
    app.run(debug=True)
