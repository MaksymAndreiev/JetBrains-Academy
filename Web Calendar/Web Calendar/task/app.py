import datetime
import http

from flask import Flask, abort, request
from flask_restful import Api, Resource, reqparse, inputs, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///name.db'

parser = reqparse.RequestParser()
parser.add_argument(
    'event',
    type=str,
    help='The event name is required!',
    required=True
)
parser.add_argument(
    'date',
    type=inputs.date,
    help='The event date with the correct format is required! The correct format is YYYY-MM-DD!',
    required=True
)

resource_fields = {
    'id': fields.Integer,
    'event': fields.String,
    'date': fields.DateTime(dt_format='iso8601')
}


class Event(db.Model):
    __tablename__ = 'name.db'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date, nullable=False)


db.create_all()


class EventByID(Resource):
    @marshal_with(resource_fields)
    def get(self, event_id):
        event = Event.query.filter(Event.id == event_id).first()
        if event is None:
            abort(404, "The event doesn't exist!")
        return event

    def delete(self, event_id):
        event = Event.query.filter(Event.id == event_id).first()
        if event is None:
            abort(404, "The event doesn't exist!")
        Event.query.filter_by(id=event_id).delete()
        db.session.commit()
        return {"message": "The event has been deleted!"}


class TodayEventResource(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return Event.query.filter(Event.date == datetime.date.today()).all()


class EventResource(Resource):
    # @marshal_with(resource_fields)
    def get(self):
        start_time = request.args.get('start_time')
        end_time = request.args.get('end_time')
        if start_time and end_time:
            list_ = []
            events = Event.query.filter(Event.date >= start_time). \
                filter(Event.date <= end_time).all()
            if len(events) < 1:
                abort(404, {"message": "The event doesn't exist!"})
            for e in events:
                el = {"id": e.id, "event": e.name, "date": str(e.date)}
                list_.append(el)
            return list_
        list_ = []
        for e in Event.query.all():
            el = {"id": e.id, "event": e.name, "date": str(e.date)}
            list_.append(el)
        return list_

    def post(self):
        args = parser.parse_args()
        name = args['event']
        date = args['date']
        event = Event(name=name, date=date)
        db.session.add(event)
        db.session.commit()

        result = {
            "message": "The event has been added!",
            "event": name,
            "date": str(date.date())
        }
        return result


api.add_resource(TodayEventResource, '/event/today')
api.add_resource(EventResource, '/event')
api.add_resource(EventByID, '/event/<int:event_id>')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
