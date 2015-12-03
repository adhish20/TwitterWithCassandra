# Twitter With Cassandra
### Team 21
### Team Members
- Adhish Singla : 201403004
- Saurabh Jain : 201301128
- Gaurav Singh : 201264059
- Shantanu : 201202022

<br/>
We aim at building an online social networking service (Twitter) that enables users to send and read short messages using a distributed DBMS – Apache Cassandra which is an open source distributed database management system designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure. Cassandra offers robust support for clusters spanning multiple datacenters, with asynchronous masterless replication allowing low latency operations for all clients.
<br/><br/>
###To setup TwitterWithCassandra:-
<br/>
1) Install Django – lattest version 1.8.3
<br/>
2) Install Cassandra – yum install cassandra (for RedHat ent.),
                       apt-get install cassandra (for debian)
<br/>
3) Install pip
<br/>
4) install cassandra-driver –> pip install cassandra-driver
<br/>
5) pip install django-cassandra-engine
<br/>
6) git clone TwitterWithCassandra repo from github
<br/>
7) cd TwitterWithCassandra
<br/>
8) pip install -U -r requirements.txt
<br/>
9) start cassandra in one terminal by typing cassandra
      (It should run. In case of any errors, google it ;)
<br/>
10) Make sure you are in twitter directory, type:
     python manage.py sync_cassandra
<br/>
11) then run the following command:
       python manage.py runserver
<br/><br/>

By default the server runs at port  8000. So open browser and goto 127.0.0.1:8000
Twitter should be running.
