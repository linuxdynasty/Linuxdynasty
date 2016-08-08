---
title: How to use Ansible AWS filters to make your playbooks and roles dynamic.
tags: [Ansible, Ansible Filters, AWS, Automation]
comments: true
share: true
---

Before I get into how I leverage Filter plugins, 1st let me post a resource about what Filters are in Ansible and how you can leverage them. [Common Filter in Ansible](http://docs.ansible.com/ansible/playbooks_filters.html)

After reading this post about Filters, you may want to start building your own. The resource below will point you to the Ansibile documentation for developing plugins. [Developing Plugins in Ansible](http://docs.ansible.com/ansible/developing_plugins.html)

# Hard coding ARNs and IDs. Life without filters. :(

If I were not to go the route of using filters and I wanted to deploy a new VPC and all of it's resources (subnets, routes, igws, nat gateways, peers), I would have to take the following steps with Ansible.

### Steps to Deploy a VPC (hard coding).

1. Run vpc_deploy.yml playbook. (Wait for playbook to finish running.)
2. Hard code IDs and ARNs in either your host_vars, group_vars, or vars folder in the role you used to deploy the VPC.
3. Commit the changes and push to github or what ever VCS you use.

<figure class="third">
    <a href="{{ site.url }}/assets/wtf_hardcoding.png"><img src="{{ site.url }}/assets/wtf_hardcoding.png" alt=""></a>
    <figcaption>WTF am I reading?</figcaption>
</figure>

Now you still have to deploy the AWS resources your services depend on (RDS, Security Groups, ELB, ASG, Kinesis, SQS, etc...).

### Steps to Deploy AWS Services (hard coding).

1. Run aws_services.yml playbook (Wait for playbook to finish running.)
2. Hard code IDs and ARNs in either your host_vars, group_vars, or vars folder in the role you used to deploy the AWS services.
3. Commit the changes and push to github or what ever VCS you use.

<figure class="second">
    <a href="{{ site.url }}/assets/wtf_hardcoding2.png"><img src="{{ site.url }}/assets/wtf_hardcoding2.png" alt=""></a>
    <figcaption>More hard coding </figcaption>
</figure>
Now if I had to do that for every VPC we manage, I would lose my mind. Also what if I want to deploy a new VPC to test out a new feature. This is not only time consuming but a real pain in the ass. Would you not rather come up with a name scheme for your AWS infrastructure and based on that name scheme, you will no longer have to worry about hard coding IDs or ARNs any more?

# Filters and the end of hard coding ARN's and IDs.
I see Ansible Filters as easy to write Python functions. Anything you can write in a function can be used as a filter. If you have been writing scripts in Python for a while, you will find that writing Ansible plugins is such a breeze.

Due to the awesomeness of filters, I know longer have to hard code any ARN or ID in any of my playbooks. Instead I have a filter that grabs the ARN for me based on the name of the resource. Now you may ask, so what is the big deal with hard coding? Well, I personally do not want to use another tool to deploy a new VPC.

{: .notice--info}
In order for these AWS filters to work, you will need to use the Name tag for all of your services.

### Example of using filters in a role "**roles/services/vars/webapp.yml**"
{% highlight yml %}
{% raw %}
---
mysql_server: "{{ aws_region | get_rds_endpoint(rds_instance_name) }}"
memcached_server: "{{ aws_region | get_elasticache_endpoint(memcached_instance_name) }}"
redshift_server: "{{ aws_region | get_redshift_endpoint(redshift_name) }}"
{% endraw %}
{% endhighlight %}

### The benefits of using the filters above.

* You do not need to know the rds instance address, sqs url, or AWS Certificate ARN in advance.
* You do not need to hard code it for each vpc or environment or app. Name space everything appropriately, and you will always get the right ARN, ID, Address, URL, etc..
* AWS Filters should be used in the task or role and not in group_vars/, host_vars, or vars.  (**If the resource does not exist, when you call the filter. The filter will raise an exception**)

# A look into the get_rds_endpoint filter.

{: .notice--info}
# I am not using the correct plugin type. I should be using lookup plugins instead of the filters plugin. My decision to use the filter plugin instead of the lookup plugin, is purely a choice based on taste. I do not want to have a Python file for each lookup that I require. I rather write a module for each type of filtering that I need to do. For instance, my aws calls are in the filter_plugins/aws.py.

<script src="http://gist-it.appspot.com/http://github.com/linuxdynasty/ld-ansible-filters/blob/master/filter_plugins/aws.py?slice=371:401"></script>

The *get_rds_endpoint* function is 15 lines of code and 13 lines of documentation. Such a small script and yet it has saved me from hard coding.

# Wrap up
* Do not hard code ARNs or IDs.
* Spend less time commiting to your VCS.
* Use AWS filters in your roles or in tasks.
* Do not use AWS filters in group_vars, host_vars, or vars.
