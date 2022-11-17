# from entities import *
import pandas as pd
from ast import literal_eval

member_columns = ["id", "name", "points", "team"]
member_table_path = "src\\tables\\members.csv"
member_default = ["no name", dict([x, 0] for x in range(5)), -1]

team_columns = ["id", "name", "points", "members"]
teams_table_path = "src\\tables\\teams.csv"
team_default = ["no name", dict([x, 0] for x in range(5, 10)), []]

events_columns = ["id", "team", "places"]
events_table_path = "src\\tables\\events.csv"
event_default = [False, dict([x, 0] for x in range(20))]


def create(path: str, columns: list, default: list, count: int):
    readed = False
    try:
        table = pd.read_csv(path).set_index("id")
        readed = True
    except:
        table = pd.DataFrame(
            data=[[x]+default for x in range(count)], columns=columns).set_index("id")
        table.to_csv(path)

    return table, readed


def update_member(members_table: pd.DataFrame, id: int, name: str = "", points={}, team: int = -1):
    if name != "":
        members_table.at[id, "name"] = name
    if points != {}:
        members_table.at[id, "points"] = points
    if team != -1:
        members_table.at[id, "team"] = int(team)
    members_table.to_csv(member_table_path)


def change_events(table: pd.DataFrame, ids: list, team: bool, places: int):
    for i, row in table.iterrows():
        if i in ids:
            table.at[i, "team"] = team
            table.at[i, "places"] = places

    table.to_csv(events_table_path)


def set_team(team_table: pd.DataFrame, members_table: pd.DataFrame, id: int, name: str = "", points={}, members=[]):
    if name != "":
        team_table.at[id, "name"] = name
    if points != {}:
        team_table.at[id, "points"] = points
        for i in members:
            members_table.at[i, "points"] = points
    if members != []:
        team_table.at[id, "members"] = members
        for i in members:
            members_table.at[i, "team"] = id
    team_table.to_csv(teams_table_path)
    members_table.to_csv(member_table_path)


def team_members(members_table):
    return members_table[members_table['team'] != -1]


def usual_members(members_table):
    return members_table[members_table['team'] == -1]


def team_events(events_table):
    return events_table[events_table['team'] == True]


def usual_events(events_table):
    return events_table[events_table['team'] == False]


def get_events(events):
    table = events
    table["places"] = table["places"].map(
        lambda x: list(literal_eval(x).values()))
    table["id"] = table.index
    temp_cols = table.columns.tolist()
    new_cols = temp_cols[-1:] + temp_cols[:-1]
    table = table[new_cols]
    table = table[["id", "places"]]
    return table.values.tolist()


def get_members(members, teams):
    table = members.replace({"team": teams["name"]}).replace(
        {"team": {-1: "No Team"}})
    table["pos"] = table["points"].map(
        lambda x: list(literal_eval(x).values()))
    table["points"] = table["points"].map(
        lambda x: sum(literal_eval(x).values()))
    table["id"] = table.index
    temp_cols = table.columns.tolist()
    new_cols = temp_cols[-1:] + temp_cols[:-1]
    table = table[new_cols]
    return table.values.tolist()


def get_teams(teams, members):
    # table = members.replace({"team": teams["name"]}).replace(
    #     {"team": {-1: "No Team"}})
    table = teams
    table["pos"] = table["points"].map(
        lambda x: list(literal_eval(x).values()))
    table["points"] = table["points"].map(
        lambda x: sum(literal_eval(x).values()))
    table["id"] = table.index
    table = table[["id", "name", "points", "pos"]]
    return table.values.tolist()

# if __name__ == "__main__":


def load_tables():

    members, readed = create(path=member_table_path,
                             columns=member_columns, default=member_default, count=40)
    print("members ", readed)

    teams, readed = create(path=teams_table_path,
                           columns=team_columns, default=team_default, count=4)
    if not readed:
        set_team(team_table=teams, members_table=members, id=0, name="Team A",
                 members=[x for x in range(0, 5)])
        set_team(team_table=teams, members_table=members, id=1, name="Team B",
                 members=[x for x in range(5, 10)])
        set_team(team_table=teams, members_table=members, id=2, name="Team C",
                 members=[x for x in range(10, 15)])
        set_team(team_table=teams, members_table=members, id=3, name="Team D",
                 members=[x for x in range(15, 20)])
    print("teams ", readed)

    events, readed = create(path=events_table_path, columns=events_columns,
                            default=event_default, count=10)
    if not readed:
        change_events(table=events, ids=list(range(5)), team=True,
                      places=dict([x, 0] for x in range(4)))
    print("events ", readed)
    # update_member(members, id=0, name="N")
    # print(get_members(members, teams))s
    print(get_events(team_events(events)))
    print(get_teams(teams, members))
    return members, teams, events


load_tables()
