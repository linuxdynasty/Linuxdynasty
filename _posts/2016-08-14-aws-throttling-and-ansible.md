---
title: AWS throttling and Ansible
tags:
 - Ansible
 - AWS
 - Automation
 - Python
comments: true
share: true
header:
  image: awsretry3.png
  teaser: awsretry3.png
excerpt: If the community is going to seriously consider using Ansible for all of it's cloud provisioning needs, then a backoff decorator needs to be implemented.
---
{% include toc %}

# Throttling and eventual consistency errors with Ansible handling the AWS provisioning.
While using some of the AWS modules for Ansible, you may have been bitten by 1 of these 2 errors:

* **RequestLimitExceeded** This happens when the region you are in is being saturated by API requests.
* **^\w+.NotFound** (Eventual Consistency Errors). The Amazon API follows an eventual consistency model. This means that the result of an API command you run that affects your Amazon resources might not be immediately visible to all subsequent commands you run.

If we were to walk through a set of tasks in a role to deploy a VPC, we would see a common set of steps.

1. vpc
2. igw
3. subnets
4. etc..

Each of the modules above can make 1+ calls to AWS and depending on the amount of calls that is being made. AWS will start to throttle the requests it receives and your playbook will fail. 

## The current state on the majority of the AWS modules in Ansible.
Since a good portion of the modules for aws do not implement a backoff decorator, we are forced to do the following.

* Add a pause between modules. (We really should not have to do this.)
* Add the retry plugin to the module. (This is not a good idea either.)

Here are a few of the AWS modules that have implemented a basic retry functionality.

* [cloudformation](https://github.com/ansible/ansible-modules-core/blob/95c67dc72a4ac1d11908980f3c345ce7d1d5136b/cloud/amazon/cloudformation.py#L226)
* [route53](https://github.com/ansible/ansible-modules-core/blob/91e9223a763bf5aa6515f02e377b38c7b5be2072/cloud/amazon/route53.py#L372)
* [ec2_elb_lb](https://github.com/ansible/ansible-modules-core/blob/81c663ff71c85f0ab9cf57e8347df1d88079f121/cloud/amazon/ec2_elb_lb.py#L403) (This one actually uses a decorator that will retry only on *RequestLimitExceeded*)

# This is where the AWSRetry.backoff decorator comes in and saves the day.
AWSRetry.backoff decorator will retry on the following errors.

* RequestLimitExceeded
* Unavailable
* ServiceUnavailable
* InternalFailure
* InternalError
* ^\w+.NotFound (Eventual Consistency Errors)

{: .notice--info}
If an exception that is not in that list is not matched, it will then just raise the exception as it normally would.

## How AWSRetry.backoff works.
The AWSRetry.backoff decorator will retry to call the failing function using an [exponential backoff algorithm](https://en.wikipedia.org/wiki/Exponential_backoff). Each time the decorated function/method throws an exception, the decorator will wait for *x* amount of time and retry calling the function until the maximum number of tries is reached. If the decorated function fails on the last try, the exception will occur unhandled.

AWSRetry is derived from the CloudRetry class. This class is meant to be used as a base class to other cloud providers, that want to build similiar functionality into Ansible Cloud modules.

### CloudRetry Class (Code)
<script src="http://gist-it.appspot.com/http://github.com/linuxdynasty/ld-ansible-filter-plugins/blob/master/aws.py?slice=15:88"></script>

### AWSRetry Class (Code)
<script src="http://gist-it.appspot.com/http://github.com/linuxdynasty/ld-ansible-filter-plugins/blob/master/aws.py?slice=89:124"></script>

### Example of how to use the AWSRetry.backoff decorator
{% highlight python %}
#Default tries is 10 and default delay is 2
@AWSRetry.backoff(tries=2, delay=1.2)
def aws_client(region, service='ec2', profile=None):
    try:
        session = boto3.Session(region_name=region, profile_name=profile)
        return session.client(service)
    except botocore.exceptions.ClientError as e:
        raise e
{% endhighlight %}

# Where to get AWSRetry.
You can the the AWSRetry decorator on GitHub in the Ansible Core repo (Still in a PR) or in my personal repo.

## For Ansible Modules
* [Currently the AWSRetry.backoff decorator is in a PR](https://github.com/ansible/ansible/pull/17039).

## Ansible Modules that are in a PR state and that depend on AWSRetry.
* [acm_certificate_facts](https://github.com/ansible/ansible-modules-extras/pull/2718)
* [ec2_vpc_nat_gateway](https://github.com/ansible/ansible-modules-extras/pull/2721)

{: .notice--info}
If you do not want to wait, you can just copy module_utils/cloud.py and module_utils/ec2.py into your ansible installation directory.

## For Ansible Filters
* [If you want to use this decorator with your AWS Filters](https://github.com/linuxdynasty/ld-ansible-plugins/tree/master/filter_plugins)

# Wrap up
If the community is going to seriously consider using Ansible for all of it's cloud provisioning needs, then a backoff decorator needs to be implemented.
