<h2>Description</h2>

<p>What about events that you have added to your calendar? We need to find a way to store and access them at any time you need. Use the <strong>Flask-SQLAlchemy </strong>extension<strong> </strong>that can connect a database to your Flask application.</p>

<h2>Theory</h2>

<p>To start working with Flask-SQLAlchemy, create an <code class="language-python">SQLAlchemy</code> object, pass a <code class="language-python">Flask</code> object to it, and specify the database file path:</p>

<pre><code class="language-python">from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///name.db'</code></pre>

<p>In the example above, <code class="language-python">name.db</code> is the database filename.</p>

<p>After that, you need to create a model that represents a table in the database. For that, you need to create a class that inherits the data from the <code class="language-python">db.Model</code> class. You would also need some fields in that class, as they represent the columns of the table:</p>

<pre><code class="language-python">class Car(db.Model):
    __tablename__ = 'table_name'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)</code></pre>

<p>The class model above can be converted into a table with the <code class="language-python">table_name</code> name with the following fields:</p>

<ul>
	<li><code class="language-python">id</code> of the <code class="language-python">INT</code> type. This column has the <code class="language-python">PRIMARY KEY</code> attribute; its value will be incremented and generated automatically.</li>
	<li><code class="language-python">name</code> of the <code class="language-python">VARCHAR</code> type. This column is <code class="language-python">NOT NULL</code>; the value length is 80 characters max.</li>
	<li><code class="language-python">date</code> of the <code class="language-python">DATE</code> type. This column is <code class="language-python">NOT NULL</code>.</li>
</ul>

<p>After that, you can save the table in the database. Call the <code class="language-python">create_all()</code> method of the SQLAlchemy object:</p>

<pre><code class="language-python">db.create_all()</code></pre>

<p>The method finds all classes that inherit from the <code class="language-python">db.Model</code> class and create their table representations in the database.</p>

<p>Now you can save, delete, and update your data in the database:</p>

<pre><code class="language-python">import datetime

...

car = Car(name='car_name', date=datetime.date.today())

# saves data into the table
db.session.add(car)
# commits changes
db.session.commit()

# returns all rows from the table as a list of Car objects.
Car.query.all()

# deletes the row from the table.
db.session.delete(car)

# returns all rows from the table where the date column has today's date as a list of Car objects.
Car.query.filter(Car.date == datetime.date.today()).all()</code></pre>

<p>Refer to the Flask-SQLAlchemy <a target="_blank" href="https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#quickstart" rel="noopener noreferrer nofollow">documentation</a> if you want to know more.</p>

<p>Also, please, convert your object into JSON format to send it as a response. You can use <code class="language-python">@marshal_with</code> annotation for that. Interested? Learn more about it from the <a target="_blank" href="https://flask-restful.readthedocs.io/en/latest/quickstart.html#data-formatting" rel="noopener noreferrer nofollow">Flask-RESTful documentation</a>.</p>

<h2>Objectives</h2>

<p>Create a model to save events to the database. The table should contain the following columns:</p>

<ul>
	<li><code class="language-python">id</code> of the <code class="language-python">INTEGER</code> type. It should be our <code class="language-python">PRIMARY KEY</code>.</li>
	<li><code class="language-python">event</code> of the <code class="language-python">VARCHAR</code> type. It should be <code class="language-python">NOT NULL</code>.</li>
	<li><code class="language-python">date</code> of the <code class="language-python">DATE</code> type. It should be <code class="language-python">NOT NULL</code>.</li>
</ul>

<p>You can use any name for your database.</p>

<p>Now your REST API should have the following features:</p>

<ul>
	<li><code class="language-python">POST</code> request for the <em>/event </em>endpoint should save the event to your database. It should require the same arguments as in the previous stage.</li>
	<li><code class="language-python">GET</code> request for the <em>/event </em>endpoint<em> </em>should return all the events from the database.</li>
	<li><code class="language-python">GET</code> request for the <em>/event/today </em>endpoint should return the list of today's events.</li>
</ul>

<h2>Examples</h2>

<p><strong>Example 1</strong>:<strong> </strong><code class="language-python">GET</code><em> request for the /event endpoint</em></p>

<p>Response body:</p>

<pre><code class="language-json">[
   {
      "id":1,
      "event":"Video conference",
      "date":"2021-03-01"
   },
   {
      "id":2,
      "event":"Today's first event",
      "date":"2021-02-28"
   }
]</code></pre>

<p><strong>Example 2</strong>:<strong> </strong><code class="language-python">GET</code><em> request for the /event/today endpoint.</em></p>

<p>Response body:</p>

<pre><code class="language-json">[
   {
      "id":2,
      "event":"Today's first event",
      "date":"2021-02-28"
   }
]</code></pre>