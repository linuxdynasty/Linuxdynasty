---
layout: post
status: publish
published: true
title: HowTo check redis availability and get stats using Redis-py, Zenoss, and Python
author:
  display_name: dynasty
  login: dynasty
  email: asanabria@linuxdynasty.org
  url: ''
author_login: dynasty
author_email: asanabria@linuxdynasty.org
date: !binary |-
  MjAxMi0wMy0yMCAwMzozNzo1MiAtMDQwMA==
date_gmt: !binary |-
  MjAxMi0wMy0xOSAyMjozNzo1MiAtMDQwMA==
categories:
- Python
- Zenoss
- Redis
tags:
- Python
- Zenoss
- Redis
comments: []
---

My team was assigned to create a redis slave status check to be ran under Zenoss.
So while they are creating that check, I decided to google for redis checks
written in python that work under Nagios and or Zenoss and none of the checks
i found did exactly what I wanted.

So I decided to write my own check, that will grab every piece of data that the redis info() command was able to retrieve. Since this info is all in a python dictionary, I was able to get all the stats that were labeled as type int or as type float, which made my job that much easier.

So 1st I had to install 2 Redis instances on my local Ubuntu server at home. Now that i completed that, I had to make sure the slave was syncing off the master server. I used this link "<a title="Redis Replication Configuration" href="http://redis.io/topics/replication" target="_blank">http://redis.io/topics/replication</a>" to help me configure redis replication.
Now that all that stuff is out of the way, I wrote an easy_peasy python script to connect to redis and grab all of the performance stats. As well as verify if the instance is a master or a slave instance. If it is a slave instance, than it also verifies if it is syncing to the master or not.
The script is using <a href="https://github.com/andymccurdy/redis-py" target="_blank">Redis-py</a> that was installed using PIP.

Here is the script I wrote
{% highlight bash %}
godssoldier:python asanabria$ python ld_check_redis.py -d 127.0.0.1 -p 't35t_r3d15' -n 6379
OK Master Redis Server 127.0.0.1 is Running 2.4.4 | pubsub_channels=0 bgrewriteaof_in_progress=0
connected_slaves=1 uptime_in_days=0 lru_clock=1099413 last_save_time=1332199497 redis_git_sha1=0
loading=0 connected_clients=1 keyspace_misses=4 used_memory=939792 vm_enabled=0
used_cpu_user_children=0.000000 used_memory_peak=939776 total_commands_processed=10
latest_fork_usec=211 used_memory_rss=1286144 total_connections_received=8 pubsub_patterns=0
aof_enabled=0 used_cpu_sys=0.130000 used_cpu_sys_children=0.000000 blocked_clients=0
used_cpu_user=0.120000 client_biggest_input_buf=0 db0_keys=2 db0_expires=0 arch_bits=64
mem_fragmentation_ratio=1.370000 expired_keys=0 evicted_keys=0 bgsave_in_progress=0
client_longest_output_list=0 process_id=22007 uptime_in_seconds=401 changes_since_last_save=2
redis_git_dirty=0 keyspace_hits=1

godssoldier:python asanabria$ python ld_check_redis.py -d 127.0.0.1 -p 't35t_r3d15' -n 6390
OK Master 127.0.0.1 is up and Slave 127.0.0.1 is in sync | pubsub_channels=0 bgrewriteaof_in_progress=0
connected_slaves=0 uptime_in_days=0 lru_clock=1099413 last_save_time=1332199497 redis_git_sha1=0
loading=0 connected_clients=2 keyspace_misses=4 used_memory=939872 master_last_io_seconds_ago=8
vm_enabled=0 used_cpu_user_children=0.000000 used_memory_peak=931248 total_commands_processed=44
latest_fork_usec=0 used_memory_rss=1277952 total_connections_received=2 pubsub_patterns=0 aof_enabled=0
used_cpu_sys=0.130000 used_cpu_sys_children=0.000000 blocked_clients=0 used_cpu_user=0.070000
master_port=6379 client_biggest_input_buf=0 db0_keys=2 db0_expires=0 arch_bits=64
mem_fragmentation_ratio=1.360000 expired_keys=0 evicted_keys=0 bgsave_in_progress=0 client_longest_output_list=0
master_sync_in_progress=0 process_id=22010 uptime_in_seconds=398 changes_since_last_save=2 redis_git_dirty=0
keyspace_hits=0

CRITICAL Master 127.0.0.1 is down and Slave 127.0.0.1 is out of sync |
pubsub_channels=0 bgrewriteaof_in_progress=0 connected_slaves=0 master_link_down_since_seconds=1332199283
uptime_in_days=0 lru_clock=1099352 last_save_time=1332198992 redis_git_sha1=0 loading=0 connected_clients=1
keyspace_misses=0 used_memory=931040 master_last_io_seconds_ago=-1 vm_enabled=0 used_cpu_user_children=0.000000
used_memory_peak=931040 total_commands_processed=5 latest_fork_usec=0 used_memory_rss=1261568
total_connections_received=6 pubsub_patterns=0 aof_enabled=0 used_cpu_sys=0.080000
used_cpu_sys_children=0.000000 blocked_clients=0 used_cpu_user=0.030000 master_port=6379
client_biggest_input_buf=0 arch_bits=64 mem_fragmentation_ratio=1.360000 expired_keys=0 evicted_keys=0
 bgsave_in_progress=0 client_longest_output_list=0 master_sync_in_progress=0 process_id=21887
uptime_in_seconds=290 changes_since_last_save=0 redis_git_dirty=0 keyspace_hits=0
{% endhighlight %}
