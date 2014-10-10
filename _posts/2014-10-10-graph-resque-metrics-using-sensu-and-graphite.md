---
layout: post
title: "Graph resque metrics using sensu and graphite."
tags:
 -
---
We are using Resque for our background jobs and we use the Resque Web interface
to keep track of what is happening. But the only issue, is that we had no
real insight to how many jobs we were running on average during certain times
of the day. We didn't know how many jobs we were processing per minute. Now how 
many workers we had per host all day everyday, which varies depending on the time
of the day.


###Download Script

* [Resque Metrics](https://github.com/linuxdynasty/Linuxdynasty/blob/master/scripts/sensu/metrics/resque_queue_metrics.rb)

###Dependencies
* [Sensu](http://sensuapp.org/) (shipper)
* [Graphite](http://graphite.wikidot.com/)
* [Resque](https://github.com/resque/resque)
* [Redis](http://redis.io/)


{% highlight bash %}
/opt/sensu/embedded/bin/ruby /etc/sensu/plugins/resque_queue_metrics.rb  -h localhost -n 15 --scheme redis-db01.resque
redis-db01.resque.queue.update_unapplied.workers 1, 1412961997
redis-db01.resque.queue.update_unapplied.jobs 0 1412961997
redis-db01.resque.queue.aging.workers 1, 1412961997
redis-db01.resque.queue.aging.jobs 0 1412961997
redis-db01.resque.host.worker-host-01.processed 90537 1412961997
redis-db01.resque.host.worker-host-01.queues 38 1412961997
redis-db01.resque.host.worker-host-01.workers 47 1412961997
redis-db01.resque.host.worker-host-02.processed 20482 1412961997
redis-db01.resque.host.worker-host-02.queues 29 1412961997
redis-db01.resque.host.worker-host-02.workers 20 1412961997
redis-db01.resque.host.worker-host-05.processed 20560 1412961997
redis-db01.resque.host.worker-host-05.queues 1 1412961997
redis-db01.resque.host.worker-host-05.workers 9 1412961997
redis-db01.resque.host.worker-host-03.processed 10928 1412961997
redis-db01.resque.host.worker-host-03.queues 1 1412961997
redis-db01.resque.host.worker-host-03.workers 15 1412961997
redis-db01.resque.host.worker-host-04.processed 23554 1412961997
redis-db01.resque.host.worker-host-04.queues 1 1412961997
redis-db01.resque.host.worker-host-04.workers 9 1412961997
redis-db01.resque.failed.communication.Communication.ActiveRecord_RecordNotFound 3 1412961997
redis-db01.resque.failed.communication.Communication.Redis_TimeoutError 1 1412961997
redis-db01.resque.failed.create_batch.CreateBatch.BatchCreationValidator_Error 77 1412961997
redis-db01.resque.failed.create_batch.CreateBatch.RuntimeError 5 1412961997
redis-db01.resque.failed.notification.Notification.ActiveRecord_RecordInvalid 2 1412961997
redis-db01.resque.failed.notification.Notification.Resque_DirtyExit 4 1412961997
redis-db01.resque.failed.notification.Notification.Redis_TimeoutError 3 1412961997
redis-db01.resque.failed.message_notifications.MessageTaskJob.RuntimeError 2 1412961997
redis-db01.resque.failed.note_upload.NoteUploadJob.HttpClient_AuthorizationError 40 1412961997
redis-db01.resque.failed.invitation.InvitationJob.ActiveRecord_RecordInvalid 2 1412961997
redis-db01.resque.failed.post.PostJob.Redis_TimeoutError 6 1412961997
redis-db01.resque.failed.post.PostJob.Resque_DirtyExit 48 1412961997
redis-db01.resque.failed.encounter.EncounterJob.Exception_NoTransitionAllowed 1 1412961997
redis-db01.resque.failed.claim_assembly.ClaimAssembly.Redis_TimeoutError 2 1412961997
redis-db01.resque.failed.claim_assembly.ClaimAssembly.Resque_DirtyExit 3 1412961997
redis-db01.resque.failed.claim_assembly.ClaimAssembly.Exception 1 1412961997
redis-db01.resque.failed.balance.Balancer_BalancerJob.Resque_DirtyExit 28 1412961997
redis-db01.resque.failed.balance.Balancer_BalanceJob.Redis_TimeoutError 1 1412961997
redis-db01.resque.failed.balance.Balancer_BalanceJob.Resque_DirtyExit 2 1412961997
redis-db01.resque.queue.failed.jobs   231 1412961997
redis-db01.resque.queues  35  1412961997
redis-db01.resque.workers 100 1412961997
redis-db01.resque.working 2   1412961997
{% endhighlight %}

###Screenshots

Now you can create dashboards, with enough information, that the developers
will no longer need to ask you what is happening with resque.

![Grafana Failed Resque Jobs]({{ site.url }}/assets/failed_resque_jobs.png)
![Grafana Resque Jobs]({{ site.url }}/assets/resque_jobs_1.png)
![Grafana Resque Workers Used]({{ site.url }}/assets/resque_workers.png)
