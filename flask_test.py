# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 12:42:36 2022
@author: Hagar
"""

from flask import Flask
app=Flask(__name__)

""" this Function render the home page"""
@app.route("/", methods=["GET","POST"])
def home():
    if request.method =="POST":
            name=request.form.get("name")
            size= float(request.form.get("size"))
            crema=request.form.get("crema")
            quantity= int(request.form.get("quantity"))
            #check the cake size
            if size == "8":
                sizeValue=8
            elif size == "10":
                sizeValue=10
            else:
                sizeValue= 16
                        
            #Calculate Total 
            price= (sizeValue * quantity)
            total=price+(price*0.06)
            #return render("Yourorder.html").format(name=name,size=size,quantity=quantity,total=total,crema=crema)
            print("<html><body>Your order is here</body></html>")
        
    else:    
        
            #return render("home.html")
            print("<html><body>Home page is here</body></html>")
                           
                           
if __name__ =="__main__" :
    
        app.run(host='0.0.0.0', port=8080)
