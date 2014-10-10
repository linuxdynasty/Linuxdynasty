---
layout: post
title: "Graph passenger metrics using sensu and graphite."
tags:
 -
---

Before I started working here, they were only collecting the common metrics
for passenger (queue, processes, and max processes). After being here a little
over a month, I realized that we were always logging into the nodes
and running watch passenger-status, and watching how much memory
certain passenger workers were consuming and how much time each of these
processes were taking.

I kept telling my team, there had to be a better way of gathering this information.
After a quick glance at passenge-status --help, I hit the gold mine.
{% highlight bash %}
Usage: passenger-status [options] [Phusion Passenger's PID]

Tool for inspecting Phusion Passenger's internal status.

Options:
        --show=pool|requests|backtraces|xml|union_station
                                     Whether to show the pool's contents,
                                     the currently running requests,
                                     the backtraces of all threads or an XML
                                     description of the pool.
    -v, --verbose                    Show verbose information.
{% endhighlight %}


###Download Script

* [Passenger Metrics](https://github.com/linuxdynasty/Linuxdynasty/blob/master/scripts/sensu/metrics/passenger_metrics.rb)

###Dependencies
* [Sensu](http://sensuapp.org/) (shipper)
* [Graphite](http://graphite.wikidot.com/)
* [NokoGiri](http://www.nokogiri.org/)

###Testing passenger-status --show xml

If you installed libxml2-utils, the xml will look very nice..
Lets take a quick glance, on what the show xml command will display....

{% highlight bash %}
passenger-status --show xml
<?xml version="1.0" encoding="iso8859-1"?>
<info version="2">
   <process_count>1</process_count>
   <max>20</max>
   <capacity_used>1</capacity_used>
   <get_wait_list_size>0</get_wait_list_size>
   <get_wait_list/>
   <supergroups>
      <supergroup>
         <name>/home/deploy/test_app/current</name>
         <state>READY</state>
         <get_wait_list_size>0</get_wait_list_size>
         <capacity_used>1</capacity_used>
{% endhighlight %}

Another example of the xml data, but showing you the process data instead...
{% highlight bash %}
passenger-status --show xml
          <processes>
               <process>
                  <pid>8540</pid>
                  <sticky_session_id>1653709171</sticky_session_id>
                  <gupid>167557a-WVPmDSUsnlj</gupid>
                  <connect_password>l;sdkflskdjfslkfjsaj;flkdjs</connect_password>
                  <concurrency>1</concurrency>
                  <sessions>0</sessions>
                  <busyness>0</busyness>
                  <processed>102</processed>
                  <spawner_creation_time>1412922319025804</spawner_creation_time>
                  <spawn_start_time>1412958391718240</spawn_start_time>
                  <spawn_end_time>1412958391746191</spawn_end_time>
                  <last_used>1412958455204460</last_used>
                  <uptime>1m 5s</uptime>
                  <life_status>ALIVE</life_status>
                  <enabled>ENABLED</enabled>
                  <has_metrics>true</has_metrics>
                  <cpu>4</cpu>
                  <rss>171028</rss>
                  <pss>136789</pss>
                  <private_dirty>103424</private_dirty>
                  <swap>0</swap>
                  <real_memory>103424</real_memory>
                  <vmsize>642504</vmsize>
{% endhighlight %}

###Running the script

As you can see, you can get a wealth of data. Data that will allow you and your
team to easily track down what is happening in you rails/sinatra cluster.

This script was written to work with Sensu and it's graphite handler.
{% highlight bash %}
/opt/sensu/embedded/bin/ruby /etc/sensu/plugins/passenger_metrics.rb --scheme rails-01.passenger
rails-01.passenger.max_pool_size  50  1412958773
rails-01.passenger.processes  23  1412958773
rails-01.passenger.top_level_queue    0   1412958773
rails-01.passenger._var_www_html_test_api_current.queue    0   1412958773
rails-01.passenger._var_www_html_test_api_current.processes    23  1412958773
rails-01.passenger._var_www_html_test_api_current.processes_being_spawned  0   1412958773
rails-01.passenger._var_www_html_test_api_current.process_1.processed  3567    1412958773
rails-01.passenger._var_www_html_test_api_current.process_1.pid    7703    1412958773
rails-01.passenger._var_www_html_test_api_current.process_1.uptime 921 1412958773
rails-01.passenger._var_www_html_test_api_current.process_1.memory 909664  1412958773
rails-01.passenger._var_www_html_test_api_current.process_1.cpu_percent    27  1412958773
rails-01.passenger._var_www_html_test_api_current.process_2.processed  2194    1412958773
rails-01.passenger._var_www_html_test_api_current.process_2.pid    11878   1412958773
rails-01.passenger._var_www_html_test_api_current.process_2.uptime 659 1412958773
rails-01.passenger._var_www_html_test_api_current.process_2.memory 644108  1412958773
rails-01.passenger._var_www_html_test_api_current.process_2.cpu_percent    23  1412958773
rails-01.passenger._var_www_html_test_api_current.process_3.processed  1484    1412958773
rails-01.passenger._var_www_html_test_api_current.process_3.pid    16146   1412958773
rails-01.passenger._var_www_html_test_api_current.process_3.uptime 402 1412958773
rails-01.passenger._var_www_html_test_api_current.process_3.memory 691392  1412958773
rails-01.passenger._var_www_html_test_api_current.process_3.cpu_percent    32  1412958773
rails-01.passenger._var_www_html_test_api_current.process_4.processed  1343    1412958773
rails-01.passenger._var_www_html_test_api_current.process_4.pid    16738   1412958773
rails-01.passenger._var_www_html_test_api_current.process_4.uptime 353 1412958773
rails-01.passenger._var_www_html_test_api_current.process_4.memory 521676  1412958773
rails-01.passenger._var_www_html_test_api_current.process_4.cpu_percent    32  1412958773
{% endhighlight %}

###Screenshots

Now you can create dashboards, with enough information, that the developers
will no longer need to ask you what is happening with passenger.

![Grafana Passenger Workers]({{ site.url }}/assets/passenger_workers.png)
![Grafana Passenger Queues]({{ site.url }}/assets/passenger_queues.png)
![Grafana Passenger Memory Used]({{ site.url }}/assets/passenger_memory_used.png)
![Grafana Passenger Time Spent]({{ site.url }}/assets/passenger_time_spent.png)
![Grafana Nginx and Passenger dashboard Part 1]({{ site.url }}/assets/nginx_passenger.png)
