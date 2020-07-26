#main file

import numpy as np
from Dreamer import Dream, DreamExtractor

dream_loader = DreamExtractor(dream_file='./dreams/badea/Badea2011Brn3aONandOFF-RCNG.swc')

dream_loader.read_dream()
generated_dream = dream_loader.generate_dream()

new_dream = Dream( generated_dream.dreamtree )
new_dream.see_dream()