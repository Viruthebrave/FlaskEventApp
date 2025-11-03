from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory list to store events
events = []

@app.route('/')
def home():
    return render_template('index.html', events=events)

@app.route('/add', methods=['POST'])
def add_event():
    event = request.form.get('event')
    if event:
        events.append(event)
    return redirect(url_for('home'))

@app.route('/delete/<int:index>')
def delete_event(index):
    if 0 <= index < len(events):
        events.pop(index)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
