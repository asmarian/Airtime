__author__ = 'nareg'

import unittest, time, re, sys, psycopg2, datetime
from settings import *

# function for finding a match in a list of words
def find_word(text, search):
    result = re.findall('\\b' + search + '\\b', text, flags=re.IGNORECASE)
    if len(result) > 0:
        return True
    else:
        return False


# translate word returns word fro now, meant for later translations
def tr_word(text):
    return text


# delete a specific user 'usertype' from database
def deleteUser(use_rtype):
    conn = psycopg2.connect(database=DB, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("DELETE FROM cc_subjs WHERE login='%s';" % use_rtype)
    conn.commit()
    conn.close()


def delete_all_users_from_db():
    conn = psycopg2.connect(database=DB, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("DELETE FROM cc_subjs WHERE login IN ('%s', '%s', '%s', '%s');" % (
    GUEST_LOGIN, DJ_LOGIN, PR_LOGIN, TADMIN_LOGIN))
    conn.commit()
    conn.close()


# this funciton receives a trackname and returns the track id from the database
def get_track_id(track_name):
    conn = psycopg2.connect(database=DB, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("SELECT * FROM cc_files WHERE track_title='%s';" % track_name)
    id = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return id


def utilize_id(trackid):
    utrackid = "au_" + str(trackid)
    return utrackid


def delete_track_from_db(trackid):
    conn = psycopg2.connect(database=DB, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("DELETE FROM cc_files WHERE id='%s';" % trackid)
    conn.commit()
    conn.close()


def delete_all_tracks_from_db():
    conn = psycopg2.connect(database=DB, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("DELETE FROM cc_files;")
    conn.commit()
    conn.close()


def get_show_id(show_name, show_date):
    conn = psycopg2.connect(database=DB, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    # cur.execute("SELECT id FROM cc_show WHERE name='%s';" % show_name)
    cur.execute(
        "select * from (select * from cc_show where name = '%s') a join (select * from cc_show_days where first_show = '%s') b on b.show_id = a.id; " % (
        show_name, show_date))
    show_id = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return show_id


def instance_show(show_id):
    # instance_id = "data-show-id-" + str(show_id)
    #print instance_id
    return show_id


def my_date_time():
    localtime = time.localtime()
    d = datetime.datetime.now()
    minutes = d.minute + 2
    start_time = str(d.hour) + ":" + str(minutes)
    start_date = time.strftime("%Y-%m-%d", localtime)
    # timer = time.strftime("%H:%M", localtime)
    return start_date, start_time


def month_name_year():
    full_month = time.strftime("%B")
    day_of_month = time.strftime("%Y")
    dates = full_month + " " + day_of_month
    return dates






