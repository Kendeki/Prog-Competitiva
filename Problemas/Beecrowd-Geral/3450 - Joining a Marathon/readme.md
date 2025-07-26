
# Joining a Marathon

There are R runners about to participate in a marathon. Johnny, who is organizing the marathon, knows that if a runner starts to run at time T with constant speed S, then at time t (for t ≥ T) the runner will be at position (t - T) * S on the track. Before time T, the runner is considered to not be on the track.  

Of course, such an event has to have great photos taken. P photos will be taken in total. Each photo will be taken at a specific time and will contain a carefully chosen segment of the track. If there are no runners in that segment at that time, the photo is considered to be trash.  

Johnny, knowing all this, was saddened by the number of trash photos that would come from his event, so he decided to take the matter into his own feet and participate in the marathon along with the other runners.  

Johnny is considering how he may run, so he will ask you Q queries of the following format: if Johnny starts to run at a given time with a certain constant speed, how many trash photos will still be taken in his event?  

###### Input
The first line contains an integer R (1 ≤ R ≤ 1000) indicating the number of runners. Each of the next R lines describes a runner with two integers T (0 ≤ T ≤ 109) and S (1 ≤ S ≤ 109), representing respectively the starting time and the speed of the runner.  

The next line contains an integer P (1 ≤ P ≤ 106) denoting the number of photos. Each of the next P lines describes a photo with three integers U (0 ≤ U ≤ 109), A and B (0 ≤ A ≤ B ≤ 109), specifying that the photo will be taken at time U and will cover the segment [A, B] of the track.  

The next line contains an integer Q (1 ≤ Q ≤ 1000) indicating the number of queries. Each of the next Q lines describes a query with two integers T′ (0 ≤ T′ ≤ 109) and S′ (1 ≤ S′ ≤ 109), representing respectively a possible starting time and speed for Johnny.  

###### Output
Output Q lines, each line with an integer indicating the number of trash photos for the corresponding query of the input.  

