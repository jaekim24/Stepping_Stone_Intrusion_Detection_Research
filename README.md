## STEPPING STONE INTRUSION DETECTION RESEARCH
I was in charge of cleaning the data which are the packets captured by TCP dump.

Created a chaff perturbation simulation algorithm in python to manipulate the TCP traffic to test if an intrusion
detection algorithm is resistant to the changes.

Using Azure Databricks, created a cluster and uploaded the packets as a text file that has been collected by using
TCPDump to run some statistical analysis such as getting the standard deviations of the run trip time, removing
outliers with the z-score, and filtering the packets to determine how effective the intrusion detection algorithm is
