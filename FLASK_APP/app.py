from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)


class worksPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    explanation = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post'+str(self.id)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/works', methods=['GET', 'POST'])
def posts():

    # if request.method == 'POST':
    #     post_title = request.form['title']
    #     post_content = request.form['content']
    #     post_author = request.form['author']
    #     new_post = BlogPost(title=post_title, content=post_content, author=post_author)
    #     db.session.add(new_post)
    #     db.session.commit()
    #     return redirect('/works')
    # else:
        all_posts = worksPost.query.order_by(worksPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')




@app.route('/home/<int:id>')
def hello(id):
    return "Hello, "+str(id)


@app.route('/onlyget', methods=['GET','POST'])    
def get_req():
    return 'You can only get this webpage'


if __name__ =="__main__":
    app.run(debug=True)    