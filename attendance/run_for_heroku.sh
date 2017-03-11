#!/bin/bash

cd attendance
gunicorn attendance.wsgi --log-file -
