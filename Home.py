from flask import Flask, render_template, redirect, url_for, session, jsonify
from flask_dance.contrib.google import make_google_blueprint, google


app = Flask(__name__)
app.config['OAUTHLIB_INSECURE_TRANSPORT'] = True
app.secret_key = "yoursecretkey"
# AIzaSyByifQgxNH1EhlVDORm3Tsil38CSZqlo7w
# create the google oauth blueprint
google_bp = make_google_blueprint(client_id="148837241813-2prertuaf355jrm1ebvib94lblvk5vh7.apps.googleusercontent.com",
                                  client_secret="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",
                                  scope=["https://www.googleapis.com/auth/userinfo.email","https://www.googleapis.com/auth/userinfo.profile"])

# register the blueprint
app.register_blueprint(google_bp, url_prefix="/login")

# home page
@app.route("/")
def home():
    return render_template("template.html")

# login page
@app.route("/login")
def login():
    return render_template("login.html")

# callback route
@app.route("/login/google/authorized")
def google_authorized():
    resp = google.authorized_response()
    if resp is None:
        return "Access denied: reason=%s error=%s" % (
            request.args["error_reason"],
            request.args["error_description"]
        )
    session["google_token"] = (resp["access_token"], "")
    return "You have been logged in!"

# Profile page
@app.route("/profile")
def profile():
    if "google_token" in session:
        me = google.get("/plus/v1/people/me").json()
        return jsonify({"data": me})
    else:
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
