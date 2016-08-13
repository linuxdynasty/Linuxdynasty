---
title: How to use Ansible AWS filters to make your playbooks and roles dynamic.
image: "elasticache.png"
tags: [Ansible, Ansible filters, AWS, Automation]
comments: true
header:
  teaser: "elasticache.png"
share: true
---
{% include toc %}

# What am I going to talk about today.
* Why hard coding AWS ARNs and IDs is a bad idea.
* Writing a filter using RDS as an example.
* How to use an Ansible filter.
* Benefits of using an Ansible filter.

# Hard coding ARNs and IDs. Life without filters. :(

To deploy a new VPC and all of it's resources (Subnets, Routes, IGWs, NAT Gateways, Peers).

## Steps to Deploy a VPC (hard coding).

1. Run vpc_deploy.yml playbook. (Wait for playbook to finish running.)
2. Hard code IDs and ARNs in either your host_vars, group_vars, or vars folder in the role you used to deploy the VPC.
3. Commit the changes and push to GitHub or what ever VCS you use.

**Example of hard coding IDs in group_vars. "*group_vars/environments/test/network.yml*"**
<figure class="third">
    <a href="{{ site.url }}/assets/wtf_hardcoding.png"><img src="{{ site.url }}/assets/wtf_hardcoding.png" alt=""></a>
    <figcaption>WTF am I reading?</figcaption>
</figure>

Now you still have to deploy the AWS resources your services depend on (RDS, Security Groups, ELB, ASG, Kinesis, SQS, etc...).

## Steps to Deploy AWS Services (hard coding).

1. Run aws_services.yml playbook (Wait for playbook to finish running.)
2. Hard code IDs and ARNs in either your host_vars, group_vars, or vars folder in the role you used to deploy the AWS services.
3. Commit the changes and push to GitHub or what ever VCS you use.


**Example of not using filters in a role "*roles/services/vars/webapp.yml*"
<figure class="second">
    <a href="{{ site.url }}/assets/wtf_hardcoding2.png"><img src="{{ site.url }}/assets/wtf_hardcoding2.png" alt=""></a>
    <figcaption>More hard coding </figcaption>
</figure>
Now if I had to do that for every VPC we manage, I would lose my mind. Also what if I want to deploy a new VPC to test out a new feature. This is not only time consuming but a real pain in the ass. Would you not rather come up with a name scheme for your AWS infrastructure and based on that name scheme. Now you will no longer have to worry about hard coding IDs or ARNs any more.

# Filters and the end of hard coding ARN's and IDs.
I see Ansible filters as easy to write Python functions. Anything you can write in a function can be used as a filter. If you have been writing scripts in Python for a while, you will find that writing Ansible plugins is such a breeze.

Due to the awesomeness of filters, I no longer have to hard code any ARN or ID in any of my playbooks. Instead I have a filter that grabs the ARN for me based on the name of the resource.

{: .notice--info}
In order for these AWS filters to work, you will need to use the Name tag for all of your services.

## A look into the get_rds_endpoint filter.

{: .notice--info}
**My decision to use the filter plugin instead of the lookup plugin, is purely a choice based on taste. I do not want to have a Python file for each lookup that I require. I rather write a module for each type of filtering that I need to do. For instance, my aws calls are in the filter_plugins/aws.py.**

The get_rds_endpoint filter will query the AWS API using the RDS instance name and return back the endpoint address.
<script src="http://gist-it.appspot.com/http://github.com/linuxdynasty/ld-ansible-filters/blob/master/filter_plugins/aws.py?slice=439:469"></script>

The *get_rds_endpoint* function is 15 lines of code and 13 lines of documentation. Such a small script and yet it has saved me from hard coding.

## Example of using the get_rds_endpoint filter in a role. "**roles/services/vars/webapp.yml**"
{% highlight yml %}
{% raw %}
---
aws_region: us-west-2
mysql_server: "{{ aws_region | get_rds_endpoint(rds_instance_name) }}"
memcached_server: "{{ aws_region | get_elasticache_endpoint(memcached_instance_name) }}"
redshift_server: "{{ aws_region | get_redshift_endpoint(redshift_name) }}"
{% endraw %}
{% endhighlight %}

## The benefits of using the filters above.
* You do not need to know the RDS instance address, SQS URL, or RedShift Cluster Address in advance.
* You do not need to hard code it for each VPC or environment or app. Name space everything appropriately, and you will always get the right ARN, ID, Address, URL, etc..
* AWS filters should be used in the task or role and not in group_vars/, host_vars, or vars. If the resource does not exist when you call the filter. The filter will raise an exception

# Wrap up
* Do not hard code ARNs or IDs.
* Since you are no longer hard coding ARNs or IDs, you will now spend less time commiting to your VCS. 
* Use AWS filters in your roles or in tasks.
* Do not use AWS filters in group_vars, host_vars, or vars. If the resource does not exist when you call the filter, the filter will raise an exception.
* [You can see all of the AWS filters I have written](https://github.com/linuxdynasty/ld-ansible-filters/blob/master/filter_plugins/aws.py)
* [An example Playbook that uses filters](https://github.com/linuxdynasty/ansible-examples)

# AnsibleFest 2016 San Francisco Talk Deploying to AWS using Ansible and Magic
<iframe src="//fast.wistia.net/embed/iframe/uzhdun6g8z" allowtransparency="true" frameborder="0" scrolling="no" class="wistia_embed" name="wistia_embed" allowfullscreen="allowfullscreen" mozallowfullscreen="mozallowfullscreen" webkitallowfullscreen="webkitallowfullscreen" oallowfullscreen="oallowfullscreen" msallowfullscreen="msallowfullscreen" width="760" height="472"></iframe>

<blockquote class="embedly-card" data-card-key="228d0c49a1274937a108a7b9d3f4289d"><h4><a href="http://www.slideshare.net/asanabria6910/ansiblefest2016deployingtoaws">AnsibleFest2016-Deploying-To-AWS</a></h4><p>Deploying to AWS using Ansible and Magic</p></blockquote>
<script async src="//cdn.embedly.com/widgets/platform.js" charset="UTF-8"></script>

# Documentation on filters
* [Common Ansible Filters and how to use them](http://docs.ansible.com/ansible/playbooks_filters.html).
* [Developing plugins in Ansible](http://docs.ansible.com/ansible/developing_plugins.html)
