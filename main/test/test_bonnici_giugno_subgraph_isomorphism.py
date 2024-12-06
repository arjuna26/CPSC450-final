import pytest
import networkx as nx
import os
import sys

# Add the parent directory to sys.path, import the algorithm to be tested
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bonnici_giugno import bonnici_giugno_subgraph_isomorphism
    