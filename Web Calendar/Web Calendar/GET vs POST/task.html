<h2>Description</h2>

<p>Let's add the ability to handle <code class="language-python">POST</code> requests from the user side and parse their arguments.</p>

<h2>Theory</h2>

<p>To parse the arguments from the <code class="language-python">POST</code> request, use the <code class="language-python">RequestParser</code> object. First, you need to create an object using the <code class="language-python">RequestParser()</code> method of the <code class="language-python">reqparse</code> object:</p>

<pre><code class="language-python">from flask_restful import reqparse

parser = reqparse.RequestParser()
</code></pre>

<p>Now, you need to specify arguments. The <code class="language-python">add_argument()</code> method can help you with that. It takes argument names, their type, and displays an error message if something goes wrong. You can also make an argument mandatory using the <code class="language-python">required=True</code> attribute:</p>

<pre><code class="language-python">from flask_restful import inputs

...

parser.add_argument(
    'date',
    type=inputs.date,
    help="Can't find the date or it has the wrong format!",
    required=True
)
parser.add_argument(
    'name',
    type=str,
    help="The name argument is required!",
    required=True
)</code></pre>

<p>The parser above requires <code class="language-python">date</code> and <code class="language-python">name</code> arguments in the request. If one of the arguments is missing, it will respond with an error message from the <code class="language-python">help</code> attribute in the following format:</p>

<pre><code class="language-json">{
    "message": {
        "name": "The name argument is required!"
    }
}</code></pre>

<p>if you're interested in more parsing features, please, refer to the official Flask-RESTful <a target="_blank" href="https://flask-restful.readthedocs.io/en/latest/quickstart.html#argument-parsing" rel="noopener noreferrer nofollow">Quickstart Guide</a>.</p>

<p>Now, call the <code class="language-python">parse_args()</code> method inside the process request:</p>

<pre><code class="language-python">class HelloWorldResource(Resource):
    def post(self):
        args = parser.parse_args()
        return args['name']</code></pre>

<p><button
        class="btn-sm btn-outline-secondary"
        onclick="getElementById('hint-1980').style.display='inline'">
        Hint
      </button>
      <div id="hint-1980" style="display:none;">If you want to handle POST requests in the resource, create a <code class="language-python">post()</code> method.</div></p>

<p><div class="alert alert-primary">Notice, that <code class="language-python">datetime</code> object is not JSON serializable, it can be serialized by converting it into the string representation: <code class="language-python">str(date.date())</code></div></p>

<h2>Objectives</h2>

<p>Create a new resource that will handle POST requests for the <em>/event </em>endpoint. It must require the following arguments in the request body:</p>

<ul>
	<li>An <code class="language-python">event</code> argument of the <code class="language-python">str</code> type. If this argument is missing, please, respond with the following error message: <code class="language-python">The event name is required!</code></li>
	<li>A <code class="language-python">date</code> argument of the <code class="language-python">inputs.date</code> type. If this argument is missing or it has the wrong format, please, respond with the following error message: <code class="language-python">The event date with the correct format is required! The correct format is YYYY-MM-DD!</code></li>
</ul>

<p>If a user sends the correct response, display the following message: <code class="language-python">The event has been added!</code>, and show the user data:</p>

<pre><code class="language-json">{
    "message": "The event has been added!",
    "event": "Client event name",
    "date": "Client date"
}</code></pre>

<h2>Examples</h2>

<p><strong>Example 1</strong>: <em>Wrong </em><code class="language-python">POST</code> <em>request for the /event endpoint</em></p>

<p>Request body:</p>

<pre><code class="language-json">{
    "date": "2021-02-10"
}</code></pre>

<p>Response body:</p>

<pre><code class="language-json">{
    "message": {
        "event": "The event name is required!"
    }
}</code></pre>

<p><strong>Example 2</strong>: <em>Wrong </em><code class="language-python">POST</code><em> request for the /event endpoint</em></p>

<p>Request body:</p>

<pre><code class="language-json">{
    "event": "Video conference",
}</code></pre>

<p>Response body:</p>

<pre><code class="language-json">{
    "message": {
        "date": "The event date with the correct format is required! The correct format is YYYY-MM-DD!"
    }
}</code></pre>

<p><strong>Example 3</strong>: <em>A</em> c<em>orrect</em> <code class="language-python">POST</code> <em>request for the /event endpoint</em></p>

<p>Request body:</p>

<pre><code class="language-json">{
    "event": "Video conference",
    "date": "2020-11-15"
}</code></pre>

<p>Response body:</p>

<pre><code class="language-json">
{
    "message": "The event has been added!",
    "event": "Video conference",
    "date": "2020-11-15"
}</code></pre>