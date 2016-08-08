---
title: How To monitor RTSP streaming videos using openRTSP and Zenoss
categories:
- Python
- Zenoss
tags:
- Zenoss
- openRTSP
comments: []
---
<p>Since I do currently work for a streaming company, that would imply that we should have some type of monitoring for our RTSP streams ;-). You will 1st need to get the openRTSP command.</p>
<ul>
<li>You will need to download the openRTSP command from http://www.live555.com/openRTSP/</li>
<li>Or if you are running Zenoss on top of Debian you can just run a apt-get install livemedia-utils</li>
</ul>
<p>Once you do that, all you have to do next is to download my script and have a valid server to point at and a path to test... Example below.. {filelink=24}</p>
<pre>./check_rtsp.py -d remote_server -p /iphone/2012 
OK /iphone/2012, test completed successfull against remote_server |status=0</pre>
<p>or with stats...</p>
<pre>./check_rtsp.py -d remote_server -p /iphone/2012 -s
OK /iphone/2012, test completed successfull against remote_server |status=0 num_packets_received=16 num_packets_lost=0 elapsed_measurement_time=3.000073 kBytes_received_total=16.309000 
measurement_sampling_interval_ms=1000 kbits_per_second_min=29.245485 kbits_per_second_ave=43.489608 
kbits_per_second_max=51.737449 packet_loss_percentage_min=0.000000 packet_loss_percentage_ave=0.000000 
packet_loss_percentage_max=0.000000 inter_packet_gap_ms_min=0.018000 inter_packet_gap_ms_ave=161.139313 
inter_packet_gap_ms_max=901.439000 subsession=video/H264 num_packets_received=61 num_packets_lost=0 
elapsed_measurement_time=3.000073 kBytes_received_total=27.630000 measurement_sampling_interval_ms=1000 
kbits_per_second_min=0.000000 kbits_per_second_ave=73.678207 kbits_per_second_max=122.923442 
packet_loss_percentage_min=0.000000 packet_loss_percentage_ave=0.000000 packet_loss_percentage_max=0.000000 
inter_packet_gap_ms_min=0.009000 inter_packet_gap_ms_ave=24.794672 inter_packet_gap_ms_max=528.923000</pre>
<p>So you can trend the different stats that openRTSP provides in Zenoss..</p>
