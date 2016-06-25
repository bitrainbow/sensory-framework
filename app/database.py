#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys


def get_database():
    """Get a databse object."""
    con = None
    try:
        con = sqlite3.connect('main.db')
        cursor = con.cursor()
        return cursor
    except sqlite3.Error as e:
        print("Error {}".format(e))
        sys.exit(1)
    finally:
        if con:
            con.close()
