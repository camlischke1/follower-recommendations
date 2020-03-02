# follower-recommendations
By counting the number of two-paths in a graph, this program gives social media follower recommendations for each user.


 This program will read the ﬁles A16.txt and A1024.txt, which are input matrices representing follower graphs.
 The input ﬁles are formatted using one line per row and spaces between columns (each entry is either 0 or 1). Compute
 recommendations (based on number of two-paths) for each vertex using both matrix multiplication and a new adjacency-list based algorithm.
 This program uses 1-indexing (the ﬁrst row of the matrix corresponds to user 1, not user 0).

The recommendations are written to text files 'rec16.txt' and 'rec1024.txt'. For line n, it is recommended that user n followers the index of the integer written on that line. If these files already exist in the current directory, they will be overwritten. However, if they do not exist, this program will create files of these names and write recommendation based onthe input matrices. 

The output given is in the form of a weighted directed graph, using adjacency lists. The graph connects nodes that had two-paths from the 
inputted graph matrix. It returns two lists per node. outputEl is the list of the id's of the connected nodes and outputVal is the list
of frequencies, or the weights, and the indices of the lists correspond directly to the other. Both lists for each node will be printed.

It is super easy to change the input files, too.

EXECUTE INSTRUCTIONS:

	python program1b.py
