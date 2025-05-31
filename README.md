## macs30123-party-model
### Final Project for MACS 30123. Parallelized parameter sweeps of an agent-based model aimed at modeling dance parties.

Sometime during the summer of 2023, one of my closest college friends decided to host a house
party. She rented a large house with four other roommates, and this house had a wide living
room, backyard, and car garage—which rarely contained cars while she lived there; the space
was usually reserved for the beer pong/rage cage table. I arrived about an hour late so as not be
unfashionably on time, and when I walked in, many partygoers were already dancing to blaring
music. Without much hesitation, I joined in on the dancing.

A few months later, a different friend hosted a holiday party. It was a much smaller affair
than the summertime event, but I knew only the host of the party and my poor roommate whom I
dragged along with me. I spent the night listening to people in their early thirties recount
whatever travel trips they had taken or various upscale bars they frequented—all of which was
purchased with their grown-up, salaried paychecks. The host made attempts to get people to
dance, with no success. By the time I left, dissatisfied and bored, I decided that not all dance
parties were created equal. This curiosity brings me to the research question at hand: how do
different social networks party differently, and how do you throw a good party?

I address this problem by designing an agent-based model (ABM), as ABMs are well suited for examining 
counterfactuals to social phenomenon. ABMs are not just well suited to generative phenomenon, they can 
reveal non-linear relationships, which is why they are better suited in some cases than regression models. 
In any case, I create my ABM, which is a combination of a simple virus SEIR model and information cascade model, 
inspired by Page and Miller's standing ovation problem (SOP). In order to examine the outcomes of this model, 
I need to perform batch runs and parameter sweeps. This is inefficient to do in parallel on a standard laptop CPU, 
which necessitates high-performance computing solutions. Batch runs are well suited to parallelization, 
because the series of tasks are highly similar, utilize most of the same files and scripts, and require little-to-no 
cross-task communication.

I attempted to parallelize using MPI on Midway3 to perform batch runs; however, I ran into an issue. 
The version of python needed for mesa, the package I use to design my model, is incompatible with the version 
of MPI that we have used in class and on Midway3. I have fought tooth and nail to get this to work, believe me. 
But, it simply won't. Fortunately, mesa has a different built-in solution. I managed to get mesa onto the air-locked RCC by git cloning the latest stable repository in my login node. From 
there, I built wheels for the package. These are not included in this repo, and they would not be stable; for reference, 
though, the version I use is mesa=3.2.1. My model is built on this latest version of mesa, which is why it requires python=>3.11. 
Regardless, mesa has an argument for parallelizing batch runs, which I use to parallelize the process on compute nodes. 

From here, I have a large csv file that I analyze using Dask ML, given the size of the dataset. From here, I generate visualizations 
to examine the relationships between parameters and what I call "party metrics." I use two different types of party metrics: 
one is the total volume of dancing, and the other is the total duration of dancing. I use visualizations rather than running regressions 
because I do not assume a linear relationship. Because I don't need to make regression models, Dask is well suited for this task. 
It has a pandas-like structure that allows for interaction with other widely used python visualization packages, such as seaborn and matplotlib. 
Its delayed compute feature allows for optimized computing by using a scheduler to arrange and order computation for optimal organization.

The visualizations provide several interesting results. As expected, higher rates of drinking where alcohol_prop > 0.5 tend to have shorter
dancing durations; it also appears that around this same threshold that dancing volume plateaus.
Interestingly, when examining the spread of dancing volume, lower rates of drinking can produce
outliers of high dancing volume; because sober agents can dance for longer than drunk agents,
there may be certain rare occasions that a low rate of drinking can produce a high volume, long
duration party. This ceiling of dancing volume is reflected as drinking rates increase, which
deterministically lowers maximum dancing volume, but also simultaneously increases average
dancing volume.

However, when considering how results vary by _k,_ a parameter controlling density of the network, we have even more difference. We can see how k values greatly impact the dancing
duration and dancing volume of party, but converge as drinking rates increase. Lower _k_ values
tend to peak early in both volume and duration around lower rates of drinking, whereas higher _k_
values tend to slowly increase and plateau in dancing volume with increased drinking rates.

When drinking rates are low in this model, the two other dancing activation thresholds,
proportion of dancing neighbors and extroversion, become more influential in dancing
activation. With lower _k_ comes a less dense network, meaning that each edge holds more weight
in calculating the proportion of dancing neighbors and a smaller number of DQs can activate the
same number of neighbors relative to a high _k_ network. We see this effect in play in the visualizations,
where smaller _k_ values peaks both earlier and higher than larger _k_ values in both dancing volume
and dancing duration.

However, varying _p_ values seem to have little to no effect on dance party metrics.
The trajectories of different _p_ value models are tightly clustered
together. The _p_ value of a Watts-Strogatz network controls the global topography with regards to
shortest paths and clustering; high _p_ values correspond with less clustering and shorter average
shortest paths, and vice versa. However, clustering and average shortest paths may have less
influence in the spread of dancing for two reasons. The first reason is that at the scale size of my
party model, the average shortest path is more influenced by density rather than clustering, in
which case _k_ is the more salient variable. The second reason is that the spawn point of dancing is
both random and independent in my model, which means that the information cascade of
dancing can begin from multiple nodes in the model and does not necessarily rely on optimal
clustering or average shortest path to converge.

## REPO

```
├── analysis.ipynb # IMPORTANT!! Contains all the visualizations!!
├── batch_run_midway.sbatch # SBATCH file used to process job. Please forgive all the comments
├── batch_test.csv # CSV file used for Dask analysis
├── batch_test.json # IGNORE: saved out to the wrong file type
├── batch_test_midway.json # IGNORE: failed attempt to parallelize with MPI
├── batch_test.py # Python script with batch run instructions
├── json_folder # IGNORE: failed attempt to parallelize with MPI
├── mesa_batch.err # Errors from batch run SBATCH job
├── mesa_batch.out # Outputs from batch run SBATCH job
├── partyagent.py # Python file detailing agent logic
├── partymodel.py # Python file detailing model logic
└── README.md # this file
```
