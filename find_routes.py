import pandas as pd
import numpy as np


def find_route_ids(name):

    trips = pd.read_csv('data/trips.txt')
    stops = pd.read_csv('data/stops.txt')
    routes = pd.read_csv('data/routes.txt')
    stop_times = pd.read_csv('data/stop_times.txt')
    step3 = pd.DataFrame()
    step4 = pd.DataFrame()
    ele = stops.loc[stops['stop_name']==name]
    ele = ele.iloc[0]
    step_2 = stop_times.loc[stop_times['stop_id']==int(ele['stop_id'])]

    for i in step_2['trip_id']:
        b = trips.loc[trips['trip_id']==i]
        a = np.asarray(b)
        step3 = step3.append(b)
    to_comp = np.unique(np.asarray(step3['route_id']))
    for rid in to_comp:
        c = routes.loc[routes['route_id'] ==rid]
        step4 = step4.append(c)
    source_route_id = np.asarray(step4['route_id'])

    return source_route_id, np.asarray(step4['route_long_name'])

def check_zero_hop(source, dest):
    ch = set(find_route_ids(source)[0]).intersection(set(find_route_ids(dest)[0]))
    rts = set(find_route_ids(source)[1]).intersection(set(find_route_ids(dest)[1]))
    if bool(ch):
        return rts
    else:
        return 0

def find_one_hop(name):

    trips = pd.read_csv('data/trips.txt')
    stops = pd.read_csv('data/stops.txt')
    routes = pd.read_csv('data/routes.txt')
    stop_times = pd.read_csv('data/stop_times.txt')
    bus_from_one = find_route_ids(name)[1]
    print(bus_from_one)
    step_1_1=pd.DataFrame()
    for i in bus_from_one:
        step_1_1 = step_1_1.append(routes.loc[routes['route_long_name'] == i])

    step_1_2 = pd.DataFrame()

    for i in np.asarray(step_1_1['route_id']):
        step_1_2 = step_1_2.append(trips.loc[trips['trip_id']==i])

    step_1_3= pd.DataFrame()
    for i in np.asarray(step_1_2['trip_id']):
        step_1_3 = step_1_3.append(stop_times.loc[stop_times['trip_id']==i])

    step_1_4 = pd.DataFrame()
    for i in np.asarray(step_1_3['stop_id']):
        step_1_4 = step_1_4.append(stops.loc[stops['stop_id']==i])

    return np.unique(np.asarray(step_1_4['stop_name']))

def check_one_hop(source, dest):
    out = set(find_one_hop(source)[0]).intersection(set(find_one_hop(dest)[0]))
    return bool(out), out

def check_hops(source, dest):
    trips = pd.read_csv('data/trips.txt')
    stops = pd.read_csv('data/stops.txt')
    routes = pd.read_csv('data/routes.txt')
    stop_times = pd.read_csv('data/stop_times.txt')
    ch1 = check_zero_hop(source, dest)
    ch2 = check_one_hop(source, dest)
    if ch1:
        return 0, ch1
    elif ch2[0]:
        return 1, ch2[1]
    else:
        return -1
