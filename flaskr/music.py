from flask import (
    Blueprint, render_template,
)
from flaskr.db import get_db

bp = Blueprint('music', __name__)


@bp.route('/names/')
def names():
    db = get_db()
    count = db.execute(
        'SELECT COUNT ( DISTINCT artist ) AS "Amount" FROM tracks;'
    ).fetchone()
    return render_template('names.html', count=count)


@bp.route('/tracks/')
def tracks():
    db = get_db()
    count = db.execute(
        'SELECT COUNT ( id ) AS "Amount" FROM tracks;'
    ).fetchone()
    return render_template('tracks.html', count=count)


@bp.route('/tracks/<genre_title>/')
def genres(genre_title):
    genre_title = genre_title.lower()
    db = get_db()
    count = db.execute(
        'SELECT COUNT (tracks.id) AS "Amount" FROM tracks INNER JOIN genres  ON '
        'tracks.genre_id = genres.id WHERE genres.title = ?;', (genre_title,)
    ).fetchone()
    return render_template('genres.html',
                           count=count,
                           genre=genre_title)


@bp.route('/tracks-sec/')
def tracks_sec():
    db = get_db()
    tracks_list = db.execute(
        'SELECT title, seconds FROM tracks;'
    ).fetchall()
    return render_template('tracks_sec.html', tracks_list=tracks_list)


@bp.route('/tracks-sec/statistics/')
def statistics():
    db = get_db()
    len_tracks = db.execute(
        'SELECT SUM(tracks.seconds) AS "total", AVG(tracks.seconds) AS "avg" FROM tracks;'
    ).fetchone()
    return render_template('statistics.html', len_tracks=len_tracks)
