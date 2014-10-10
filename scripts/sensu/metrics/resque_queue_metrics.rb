#!/usr/bin/env ruby
#
# Metrics collector for resque.
#This script work in conjuction with sensu and graphite
#
#Author: Allen Sanabria <https://github.com/linuxdynasty>
# Released under the same terms as Sensu (the MIT license); see LICENSE
# for details.

require 'rubygems' if RUBY_VERSION < '1.9.0'
require 'sensu-plugin/metric/cli'
require 'socket'
require 'resque'
require 'resque/failure/redis'


class ResqueMetrics < Sensu::Plugin::Metric::CLI::Graphite
  @@timestamp = Time.now.to_i

  option :hostname,
    :short => "-h HOSTNAME",
    :long => "--host HOSTNAME",
    :description => "Redis hostname",
    :required => true

  option :port,
    :short => "-P PORT",
    :long => "--port PORT",
    :description => "Redis port",
    :default => "6379"

  option :namespace,
    :description => "Resque namespace",
    :short => "-n NAMESPACE",
    :long => "--namespace NAMESPACE",
    :default => "resque"

  option :scheme,
    :description => "Metric naming scheme, text to prepend to metric",
    :short => "-s SCHEME",
    :long => "--scheme SCHEME",
    :default => "#{Socket.gethostname}.resque"

  def workers(workers)
    queue_data = {}
    host_data = {}
    hosts = []
    data = []
    workers.each do |worker|
      hdata = worker.id.split(":")
      hosts.push(hdata[0])
      unless host_data.has_key?(hdata[0])
        host_data[hdata[0]] = {:pids => [{:pid => worker.pid, :queues => worker.queues, :processed => worker.processed}]}
      else
        host_data[hdata[0]][:pids].push({:pid => worker.pid, :queues => worker.queues, :processed => worker.processed})
      end
      worker.queues.each do |queue|
        unless queue_data.has_key?(queue)
          queue_data[queue] = {:workers => [hdata[0]]}
        else
          queue_data[queue][:workers].push(hdata[0])
        end
      end
    end
    queue_data.keys.each do |queue|
      queue_data[queue][:workers] = queue_data[queue][:workers].to_set.to_a
      data << "#{config[:scheme]}.queue.#{queue}.workers #{queue_data[queue][:workers].length}, #{@@timestamp}"
      data << "#{config[:scheme]}.queue.#{queue}.jobs #{Resque.size(queue)} #{@@timestamp}"
    end
    host_data.keys.each do |host|
      unless host_data[host].has_key?(:queues)
        host_data[host][:queues] = []
      end
      unless host_data[host].has_key?(:processed)
        host_data[host][:processed] = 0
      end
      host_data[host][:pids].each do |pid_data|
        host_data[host][:queues] = host_data[host][:queues].to_set.union(pid_data[:queues]).to_a
        host_data[host][:processed] = host_data[host][:processed] + pid_data[:processed].to_i
      end
    end
    host_data.keys.each do |host|
      data << "#{config[:scheme]}.host.#{host}.processed #{host_data[host][:processed]} #{@@timestamp}"
      data << "#{config[:scheme]}.host.#{host}.queues #{host_data[host][:queues].length} #{@@timestamp}"
      data << "#{config[:scheme]}.host.#{host}.workers #{host_data[host][:pids].length} #{@@timestamp}"
    end
    return data
  end

  def get_failures(backend)
    failure_ids = []
    failures = {}
    backend.each do |failure_id|
      failure_ids << failure_id
    end
    failure_ids.each do |id|
      failure = backend.all(index=id)
      if failures.has_key? failure["queue"]
        if failures[failure["queue"]].has_key? failure["payload"]["class"]
          if failures[failure["queue"]][failure["payload"]["class"]].has_key? failure["exception"]
            current_count = failures[failure["queue"]][failure["payload"]["class"]][failure["exception"]]
            failures[failure["queue"]][failure["payload"]["class"]][failure["exception"]] = current_count + 1
          else
            failures[failure["queue"]][failure["payload"]["class"]][failure["exception"]] = 1
          end
        else 
          failures[failure["queue"]][failure["payload"]["class"]] = {}
          failures[failure["queue"]][failure["payload"]["class"]][failure["exception"]] = 1
        end
      else
         failures[failure["queue"]] = {}
         failures[failure["queue"]][failure["payload"]["class"]] = {}
         failures[failure["queue"]][failure["payload"]["class"]][failure["exception"]] = 1
      end
    end
    return failures
  end

  def print_failures(failures)
    data = []
    if !failures.empty?
      failures.each do |queue_key, queue_val|
        failures[queue_key].each do |error_class_key, error_class_val|
          failures[queue_key][error_class_key].each do |exception_class_key, exception_class_val|
            error_class = error_class_key.gsub("::", "_")
            exception_class = exception_class_key.gsub("::", "_")
            data << "#{config[:scheme]}.failed.#{queue_key}.#{error_class}.#{exception_class} #{exception_class_val} #{@@timestamp}"
          end
        end
      end
    end
    return data
  end

  def run
    Resque.redis = Redis.new(:host => config[:hostname], :db => config[:namespace], :port => config[:port])
    worker_data = workers(Resque.workers)
    failures = get_failures(Resque::Failure.backend)
    failure_data = print_failures(failures)
    output_data = worker_data + failure_data
    output_data.each do |data|
      output data
    end
    count = Resque::Failure::Redis.count
    output "#{config[:scheme]}.queue.failed.jobs", count, @@timestamp
    output "#{config[:scheme]}.queues", Resque.queues.length, @@timestamp
    output "#{config[:scheme]}.workers", Resque.workers.length, @@timestamp
    output "#{config[:scheme]}.working", Resque.working.length, @@timestamp
    ok
  end
end
