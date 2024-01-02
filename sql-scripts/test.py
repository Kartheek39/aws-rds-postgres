#!/usr/bin/env python3

import argparse
import psycopg2

from db_config import config

conn = None  # global variable

def create_pagila_db():
    """
    Creates Pagila database by running DDL and DML scripts
    """

    try:
        global conn
        with conn:
            with conn.cursor() as curs:
                curs.execute(open("../sql-scripts/schema/schema.sql", "r").read())
                #curs.execute(open("../sql-scripts/data.sql", "r").read())
                conn.commit()
                print('Pagila SQL scripts executed')
  

