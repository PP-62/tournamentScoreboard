from flask import Flask, render_template, request
from .table_control import *

members, teams, events = load_tables()
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        for i in range(members.size):
            name = request.form.get(str(i))
            print(name)
            if (name):
                update_member(members_table=members, id=i, name=name)

    return render_template('index.html',
                           team_members=get_members(
                               team_members(members), teams),
                           individual_members=get_members(
                               usual_members(members), teams),
                           )


@app.route("/team_events", methods=['POST', 'GET'])
def team_events_page():
    if request.method == 'POST':
        for i in range(members.size):
            name = request.form.get(str(i))
            print(name)
            if (name):
                update_member(members_table=members, id=i, name=name)

    return render_template('team_events.html',
                           team_members=get_members(team_members(members,), teams), events=get_events(team_events(events), teams=get_teams(teams, members))
                           )
