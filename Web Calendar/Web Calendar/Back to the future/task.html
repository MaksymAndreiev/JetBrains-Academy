<h2>Description</h2>

<p>It is so easy to forget about important things! Work meetings, doctor appointments, gym sessions, family gatherings, parties with friends, so much to remember! Planning is another important feature of our calendar. We need to add the ability to get a list of events for a certain time interval, find the event info by an ID, and delete events from the database.</p>

<h2>Theory</h2>

<p>You can get variables from the request URL:</p>

<pre><code class="language-python">class EventByID(Resource):

    @marshal_with(resource_fields)
    def get(self, event_id):
        return event_id


api.add_resource(EventByID, '/event/&lt;int:event_id&gt;')</code></pre>

<p>In the example above, we get an integer value from the request URL and return the variable as a response.</p>

<p>In some cases, you need to abort the requests and return an error message if something is wrong. You can use the <code class="language-python">abort()</code> method that accepts an HTTP status code and sends a response with the given status code and a message. Note that you need to call the <code class="language-python">abort()</code> method inside the request handler method:</p>

<pre><code class="language-python">from flask import abort

...

def get(self, event_id):
    event = Event.query.filter(Event.id == event_id).first()
    if event is None:
        abort(404, "The event doesn't exist!")
    return event</code></pre>

<p>In the example above, the method will return the <code class="language-python">404</code> status code with the message <code class="language-python">The event doesn't exist!</code> If the event does exist, it will return the event in JSON format with the <code class="language-python">200</code> status code.</p>

<h2>Objectives</h2>

<p>In this stage, add a resource with the <em>/event/&lt;int:id&gt; </em>URL. It should handle the following requests:</p>

<ul>
	<li>A <code class="language-python">GET</code> request should return the event with the ID in JSON format. If an event doesn't exist, return <code class="language-python">404</code> with the following message: <code class="language-python">The event doesn't exist!</code>.</li>
	<li>A <code class="language-python">DELETE</code> request should delete the event with the given ID and respond with the following response body: 
	<pre><code class="language-python">{
    "message": "The event has been deleted!"
}</code></pre>
	If the event with the ID doesn't exist, return <code class="language-python">404</code> with the message <code class="language-python">The event doesn't exist!</code></li>
	<li>A <code class="language-python">GET</code> request for the <em>/event </em>endpoint with <code class="language-python">start_time</code> and <code class="language-python">end_time</code> parameters should return a list of events for the given time range. If the arguments are missing, return the list of all events.</li>
	<li>The URLs from the previous stage should work in the same way.</li>
</ul>

<h2>Examples</h2>

<p><strong>Example 1</strong>: <code class="language-python">GET</code><em> request for the /event?start_time=2020-10-10&amp;end_time=2020-10-20 endpoint</em></p>

<p>Response Body:</p>

<pre><code class="language-json">[
   {
      "id":1,
      "event":"Video conference",
      "date":"2020-10-15"
   },
   {
      "id":2,
      "event":"Today's first event",
      "date":"2020-10-20"
   }
]</code></pre>

<p><strong> Example 2</strong>: <code class="language-python">GET</code><em> request for the /event/1 endpoint</em></p>

<p>Response Body:</p>

<pre><code class="language-json">{
    "id":1,
    "event":"Video conference",
    "date":"2020-10-15"
}</code></pre>

<p><strong>Example 3</strong>: <code class="language-python">GET</code><em> request for the /event/10 endpoint</em></p>

<p>Response Body:</p>

<pre><code class="language-json">{
    "message": "The event doesn't exist!"
}</code></pre>

<p><strong>Example 4</strong>: <code class="language-python">DELETE</code><em> request for the /event/1 endpoint</em></p>

<p>Response Body:</p>

<pre><code class="language-json">{
    "message": "The event has been deleted!"
}</code></pre>

<p><strong> Example 5</strong>: <code class="language-python">DELETE</code><em> request for the /event/10 endpoint</em></p>

<p>Response Body:</p>

<pre><code class="language-json">{
    "message": "The event doesn't exist!"
}</code></pre>