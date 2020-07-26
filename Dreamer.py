import numpy as np 

from anytree import Node, RenderTree, findall

class Dream:
    def __init__(self, dreamtree=None):
        self.dreamtree = dreamtree

    
    # def add_dream_node(self):
    #     self.dreamtree

    def set_dreamtree(self, dreamtree):
        self.dreamtree = dreamtree

    def see_dream(self):
        print(self.dreamtree.root.children)
        print(RenderTree(self.dreamtree))

    def get_dream_node_by_name(self, node_name):
        nodes =  findall( self.dreamtree.root, filter_= lambda node: node.name == node_name )
        return nodes[0]
 #   def extract_spatial_dream(self):



class DreamExtractor:
    def __init__(self, dream_file):

        self.dream_file = dream_file
        self.unconverted_dream = None
        self.dream = None

    def read_dream(self):
        with open(self.dream_file, "r", ) as new_dream:
            self.unconverted_dream = [ dream_node.strip() for dream_node in new_dream ] # read each file line

    def generate_dream(self):
        if self.unconverted_dream is None:
            return False
        else:
            self.dream = Dream( dreamtree=Node("root") )
            for dream_node in self.unconverted_dream:
                if not (dream_node[0] is '#'): #discard comments
                    string_float_list = dream_node.split(" ")               #separate each float.
                    float_list = [ float(value) for value in string_float_list ]    #convert each string to float.

                    try:
                        trace_num = int(float_list[0])       # the trace number (1, 2, 3, ....)
                        dream_node_type = float_list[1] # axon, soma, basal dendrite.
                        x = float_list[2]
                        y = float_list[3]
                        z = float_list[4]
                        dream_node_radius = float_list[5]
                        dream_node_parent = int(float_list[6]) # parent node (parent trace number)
                        
                        print(float_list)

                        if trace_num is 1: #first node.
                            new_dream_node = Node(name=1, parent=self.dream.dreamtree.root,
                                             dream_coords={'x': x, 'y': y, 'z': z}, dream_radius=dream_node_radius, dream_node_type=dream_node_type)
                        else:
                            dream_node_parent = self.dream.get_dream_node_by_name( dream_node_parent )
                            print(dream_node_parent)
                            print("---")
                            new_dream_node = Node(name=trace_num, parent=dream_node_parent,
                                             dream_coords={'x': x, 'y': y, 'z': z}, dream_radius=dream_node_radius, dream_node_type=dream_node_type)

                    except IndexError:
                        print("not enough floats within this dream node")

            return self.dream