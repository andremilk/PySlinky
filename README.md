About PySlinky
========

PySlinky is a simple web application to test and learn about autoscaling and scalability in general.    
It was named after a very popular [toy](http://en.wikipedia.org/wiki/Slinky) which was basically a helical spring. It uses [Flask](http://flask.pocoo.org) and it's meant to test and learn how scalability on different approaches will work.
The idea here is to stress the app enough to trigger autoscaling watches either by using the database or simply the server load. 
A reverse proxy will be used to access this application.

Requirements
======

*  [psutil](https://github.com/giampaolo/psutil)
* [Flask](http://flask.pocoo.org)

Services and Contents
=======

*  mysql database with data to be defined
    * the main goal here is to test the database scalability, it will run in another server
*  a simple service to stress the server and return simple codes for better understanding of application health
    * the application should stress memory, cpu and others (TBD) resources on the server 

Testing it
=======

One of the tools you might use to test/stress the app is [httperf](http://www.hpl.hp.com/research/linux/httperf).

Acknowledgement
=========

I would like to thank my friend bozo (vitor) helping me pick the name of this project :3.
