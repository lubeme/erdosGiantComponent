#!/usr/bin/python
# -*- coding: UTF-8 -*-
import networkx as nx
import random
from scipy.stats import bernoulli

__author__ = 'Luis Úbeda (http://www.github.com/lubeme)'


def bar_ub_zuf(n, p, th,seed= None):

    #init
    G = nx.Graph()
    G.name = "bar_ub_zuf"
    G.add_nodes_from(range(1, n + 1))
    posibleEdges = {}
    keyAux = 0
    giantComponent=False
    probabilities = bernoulli.rvs(p, size = n*(n-1)/2)
    for node1 in xrange(0, n):
        for node2 in xrange(node1 + 1, n):
            #Si el enlace existe o no, puede hacerse offline antes del experimento.
            posibleEdges[keyAux]=(probabilities[keyAux], node1, node2)
            keyAux += 1
    print posibleEdges
    print posibleEdges.pop(random.choice(posibleEdges.keys()))
    for iter in xrange(0, len(posibleEdges)):
        posEdge = posibleEdges.pop(random.choice(posibleEdges.keys()))
        #Existe el enlace
        if posEdge[0]==1:
            G.add_edge(posEdge[1],posEdge[2])
            #Comprobacion de componente gigante
            if len(nx.connected_components(G)[0])>th:
               giantComponent=True
               break
    #Devuelve si existe una componente gigante y la iteración en que se alcanza
    numEdgesForGiantComponent=iter+1
    return giantComponent,numEdgesForGiantComponent
