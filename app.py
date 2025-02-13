from flask import Flask, render_template, request, redirect
app = Flask(__name__)

todos = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        todos.append({
            'title': title,
            'description': description,
            'completed': False
        })
    return render_template('index.html', todos=todos)

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect('/')

@app.route('/complete/<int:index>')
def complete(index):
    if 0 <= index < len(todos):
        todos[index]['completed'] = not todos[index]['completed']
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)