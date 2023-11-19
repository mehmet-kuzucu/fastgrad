import numpy as np

class Number:
    def __init__(self, value, child=(), grad=0):
        self.value = value
        self.prev = set(child)
        self.grad = grad
        self._backward = lambda: None


    def backward(self):

        #create a graph
        graph = []
        visited = set()
        def build_graph(node):
            if node in visited:
                return
            visited.add(node)
            for prev in node.prev:
                build_graph(prev)
            graph.append(node)
        build_graph(self)

        self.grad = 1
        for v in reversed(graph):
            v._backward()


    def __add__(self, other):
        if isinstance(other, Number):
            r = Number(self.value + other.value, child=(self, other))
        elif isinstance(other, int) or isinstance(other, float):
            other = Number(other)
            r = Number(self.value + other.value, child=(self, other))
        else:
            raise TypeError("Not supported type")
        
        def _backward():
            self.grad += 1 * r.grad
            other.grad += 1 * r.grad
        r._backward = _backward

        return r

    
    def __mul__(self, other):
        if isinstance(other, Number):
            r = Number(self.value * other.value, child=(self, other))
        elif isinstance(other, int) or isinstance(other, float):
            other = Number(other)
            r = Number(self.value * other.value, child=(self, other))
        else:
            raise TypeError("Not supported type")
        
        def _backward():
            self.grad += other.value * r.grad
            other.grad += self.value * r.grad
        r._backward = _backward

        return r

    def __radd__(self, other):
        return self.__add__(other)
    def __rmul__(self, other):
        return self.__mul__(other)
    
    # visulize the graph using matplotlib use the values as the node
    def visulize(self):
        
        import matplotlib.pyplot as plt
        import networkx as nx

        graph = nx.DiGraph()
        visited = set()
        def build_graph(node):
            if node in visited:
                return
            visited.add(node)
            for prev in node.prev:
                build_graph(prev)
                graph.add_edge(prev.value, node.value)
        build_graph(self)

        nx.draw(graph, with_labels=True)
        plt.show()
    
    


if __name__ == "__main__":
    a = Number(5)
    b = Number(10)
    c = a * b
    d = a + 2
    f = c * d


    print(f"a value : {a.value}")
    print(f"b value : {b.value}")
    print(f"c value : {c.value}")
    print(f"d value : {d.value}")
    print(f"f value : {f.value}")

    print("===============")
   
    f.backward()
    print(f"a grad : {a.grad}")
    print(f"b grad : {b.grad}")
    print(f"c grad : {c.grad}")
    print(f"d grad : {d.grad}")
    print(f"f grad : {f.grad}")

    print("===============")

    f.visulize()




    
