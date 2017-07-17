from flask import Flask, request, render_template
# set the project root directory as the static folder, you can set others.
app = Flask(__name__)

@app.route('/')
@app.route('/<index>')
def root(index="index.html"):
    return app.send_static_file(index)
    
@app.route('/css/<path:filename>')
def send_css(filename):
    return send_from_directory('css', filename)
    
    
@app.errorhandler(404)
def page_not_found(e):
    argg = request.args.get('val')
    return render_template('404.html',args=argg),404
