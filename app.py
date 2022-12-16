# pip freeze > requirements.txt
# source youtubemp3/bin/activate
from flask import Flask, render_template, request, flash, send_file, redirect, url_for, session, after_this_request
from YTscript import getMP3
import re
import os.path


app = Flask(__name__)
app.secret_key = "super secret key"

@app.after_request
def add_no_cache_headers(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

def downloadMP3(url):
    result = getMP3(url)
    return result

@app.route("/", methods=["POST","GET"])
def index():
    return render_template("index.html")

@app.route('/forward', methods=['GET'])
def background_process_test():
    link = str(request.args.get("text"))

    # pattern = r"^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+"
    # if not re.match(pattern, link):
    #     error_statement = "Please enter a valid YouTube Link"
    #     return render_template('index.html')

    result = downloadMP3(link)
    path = result

    @after_this_request
    def delete_file(response):
        os.remove(path[0])
        return response
    return send_file(
        path[0],
        mimetype='audio/mpeg',
        as_attachment=True,
    )

if __name__ == "__main__":
    app.run()
