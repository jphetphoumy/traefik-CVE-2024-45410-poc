from flask import Flask, request, render_template, abort, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'

ALLOWED_HOST = "127.0.0.1"
FLAG = "CTF{h0p-by-h0p-tr43f!k}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        submitted_flag = request.form.get('flag', '')
        if submitted_flag == FLAG:
            flash("Congratulations! You've successfully redeemed the coupon.", "success")
        else:
            flash("Invalid coupon code. Please try again.", "danger")

    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/admin')
def admin():
    x_forwarded_host = request.headers.get('X-Forwarded-Host', '')
    if x_forwarded_host != ALLOWED_HOST:
        abort(403, description="Forbidden: Invalid X-Forwarded-Host")
    
    return render_template('admin.html', flag=FLAG)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
