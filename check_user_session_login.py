from flask import g, session, abort, render_template


@app.before_request
def before_request():
    if "user_id" in session:
        g.user = User.query.get(session["user_id"])


@app.route("/restricted")
def admin():
    if g.user is None:
        abort(403)
    return render_template("admin.html")
