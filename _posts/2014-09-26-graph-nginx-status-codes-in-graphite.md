---
layout: post
title: "Graph nginx status codes in Graphite."
tags:
 -[sensu, graphite, metrics, nginx]
---

I'm currently at the tail end of collecting metrics for the current company I work for.
We are using a combination of..
* [Sensu](http://sensuapp.org/) (shipper)]
* [Graphite](http://graphite.wikidot.com/)/[StatsD](https://github.com/etsy/statsd/) (metrics handler)
* [Grafana](http://grafana.org/) (Beautiful Dashboards).

I built a python script, that leverages the awesome tool [logtail](http://linux.die.net/man/8/logtail)
in order to collect http status codes, without consuming too much cpu/ram.

I have tested this script against nginx logs and against 2 different formats (txt and json).

###Basic Logging
~~~ txt
"GET /test/foo HTTP/1.0" 200 76288 "-" "Ruby"
~~~

###Json Logging
I printed the json on multiple lines, but in the log, the json is all in 1 line.
{% highlight json %}
{
    "@timestamp": "2014-09-26T08:45:35-04:00",
    "@fields": {
        "remote_addr": "127.0.0.1",
        "remote_user": "-",
        "body_bytes_sent": "4823",
        "request_time": "0.127",
        "status": "200",
        "request": "POST /rubyamf_gateway/ HTTP/1.0",
        "request_method": "POST",
        "http_referrer": "https://foo.bar.net/test/test",
        "http_user_agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36"
    }
}
{% endhighlight %}

The only dependency of this script is logtail which you can install easily on any *nix system.
* apt-get install logtail
* yum install logtail

If you do not have logtail installed you will get the following error
{% highlight bash %}
{9:45}~/Linuxdynasty/scripts/sensu/metrics:master ✓ python nginx-status-code-metrics.py -h
Please install logtail
{% endhighlight %}

The following options are available
{% highlight bash %}
{9:45}~/Linuxdynasty/scripts/sensu/metrics:master ✓ ➭ python nginx-status-code-metrics.py -h
Options:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory=DIRECTORY
                        The directory where the access logs exist
  -f FILE, --file=FILE  name of the access log
  -t FILE_FORMAT, --file_format=FILE_FORMAT
                        json or txt
  -s SCHEME, --scheme=SCHEME
                        the metric naming scheme
{% endhighlight %}
