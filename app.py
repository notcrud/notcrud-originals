from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_view():
	return render_template('test.html')


@app.route('/postman')
def postman_view():
	post_title = 'Postman'
	post_headline = 'Fixing the API development workflow.'
	post_thread_url = 'http://notcrud.com/topic/212/postman-fixing-the-api-workflow'

	return render_template('post.html', post_title=post_title, post_headline=post_headline, post_thread_url=post_thread_url)



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=9000, debug=True)
