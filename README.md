# Traffic Data Fetcher

Python script to fetch data from the Google Maps Distance Matrix API.
The API is provided <a href="https://developers.google.com/maps/documentation/distance-matrix/">here</a> and requires a Google API key that can be found <a href="https://developers.google.com/maps/documentation/embed/get-api-key">here</a>.

# Use

There are two ways of using the script, each corresponding to a mode set in the parameters file.

1. By creating a complete duration matrix. (mode = 0)\n
In this case, you should provide the structure of the graph with the 'graph_structure.csv' provided as an example. The output will be the resulting duration matrix, saved at the location set in the parameters.

2. By filling a duration matrix. (mode = 1)\n
In this case, you should provide the path to the uncomplete duration matrix in the parameters file. The output will be the completed duration matrix, saved at the location set in the parameters.

In each cases, other parameters such as the considered period of time and the time step width are set into the parameters file called 'parameters.py'.

# Duration matrix

The resulting duration matrix has the following structure:

<table style="width:100%">
  <tr>
    <th>Starting location</th>
    <th>Goal location</th> 
    <th>t0</th>
    <th>...</th>
    <th>tM</th>
  </tr>
  <tr>
    <td>Start_0</td>
    <td>Goal_0</td>
    <td>duration00</td>
    <td>...</td>
    <td>duration0M</td>
  </tr>
  <tr>
    <td>Start_N</td>
    <td>Goal_N</td>
    <td>durationN0</td>
    <td>...</td>
    <td>durationNM</td>
  </tr>
</table>

Whith the following notations:
- ($start_0$, ..., Start_N) are the starting locations of the edges;
- (Goal_0, ..., Goal_N) are the goal locations of the edges;
- (t0, ..., tM) are the time steps of departure time (s);
- (durationij) are the computed durations.

