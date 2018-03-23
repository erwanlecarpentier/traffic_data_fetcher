# Traffic Data Fetcher

Python script to fetch data from the Google Maps Distance Matrix API.
The API is provided <a href="https://developers.google.com/maps/documentation/distance-matrix/">here</a> and requires a Google API key that can be found <a href="https://developers.google.com/maps/documentation/embed/get-api-key">here</a>.

# Use

There are two ways of using the script, each corresponding to a mode set in the parameters file 'parameters.py'.

1. By creating a complete duration matrix. (mode = 0)<br>
In this case, you should provide the structure of the graph with the 'graph_structure.csv' provided as an example. The output will be the resulting duration matrix, saved at the location set in the parameters.

2. By filling a duration matrix. (mode = 1)<br>
In this case, you should provide the path to the uncomplete duration matrix in the parameters file. The output will be the completed duration matrix, saved at the location set in the parameters.

In each cases, other parameters such as the considered period of time and the time step width are set into the parameters file.

# Duration matrix

The resulting duration matrix has the following structure:

<table style="width:100%">
  <tr>
    <th>Starting location</th>
    <th>Goal location</th> 
    <th>t<sub>0</sub></th>
    <th>...</th>
    <th>t<sub>M</sub></th>
  </tr>
  <tr>
    <td>start<sub>0</sub></td>
    <td>goal<sub>0</sub></td>
    <td>duration<sub>0,0</sub></td>
    <td>...</td>
    <td>duration<sub>0,M</sub></td>
  </tr>
  <tr>
    <td>...</td>
    <td>...</td>
    <td>...</td>
    <td>...</td>
    <td>...</td>
  </tr>
  <tr>
    <td>start<sub>N</sub></td>
    <td>goal<sub>N</sub></td>
    <td>duration<sub>N,0</sub></td>
    <td>...</td>
    <td>duration<sub>N,M</sub></td>
  </tr>
</table>

Whith the following notations:
- (start<sub>0</sub>, ..., start<sub>N</sub>) are the starting locations of the edges;
- (goal<sub>0</sub>, ..., goal<sub>N</sub>) are the goal locations of the edges;
- (t<sub>0</sub>, ..., t<sub>M</sub>) are the time steps of departure time (s);
- (duration<sub>i,j</sub>) are the computed durations.

