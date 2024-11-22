def create_nodes(femmesh):
    # nodes
    femmesh.addNode(0.0, 500.0, 0.0, 1)
    femmesh.addNode(0.0, 500.0000000000002, 1000.0, 2)
    femmesh.addNode(8000.0, 500.0, 0.0, 3)
    femmesh.addNode(8000.0, 500.0000000000002, 1000.0, 4)
    femmesh.addNode(0.0, 500.0000000000001, 500.0, 5)
    femmesh.addNode(2000.0, 500.0, 0.0, 6)
    femmesh.addNode(4000.0, 500.0, 0.0, 7)
    femmesh.addNode(6000.0, 500.0, 0.0, 8)
    femmesh.addNode(1000.0, 500.0, 0.0, 9)
    femmesh.addNode(7000.0, 500.0, 0.0, 10)
    femmesh.addNode(3000.0, 500.0, 0.0, 11)
    femmesh.addNode(5000.0, 500.0, 0.0, 12)
    femmesh.addNode(8000.0, 500.0000000000001, 500.0, 13)
    femmesh.addNode(2000.0, 500.0000000000002, 1000.0, 14)
    femmesh.addNode(4000.0, 500.0000000000002, 1000.0, 15)
    femmesh.addNode(6000.0, 500.0000000000002, 1000.0, 16)
    femmesh.addNode(1000.0, 500.0000000000002, 1000.0, 17)
    femmesh.addNode(7000.0, 500.0000000000002, 1000.0, 18)
    femmesh.addNode(3000.0, 500.0000000000002, 1000.0, 19)
    femmesh.addNode(5000.0, 500.0000000000002, 1000.0, 20)
    femmesh.addNode(2000.0, 500.0000000000001, 500.0, 21)
    femmesh.addNode(1000.0, 500.0000000000001, 500.0, 22)
    femmesh.addNode(6000.0, 500.0000000000001, 500.0, 23)
    femmesh.addNode(7000.0, 500.0000000000001, 500.0, 24)
    femmesh.addNode(4000.0, 500.0000000000001, 500.0, 25)
    femmesh.addNode(3000.0, 500.0000000000001, 500.0, 26)
    femmesh.addNode(5000.0, 500.0000000000001, 500.0, 27)
    return True


def create_elements(femmesh):
    # elements
    femmesh.addFace([14, 17, 22, 21], 21)
    femmesh.addFace([6, 21, 22, 9], 22)
    femmesh.addFace([1, 9, 22, 5], 23)
    femmesh.addFace([2, 5, 22, 17], 24)
    femmesh.addFace([4, 18, 24, 13], 25)
    femmesh.addFace([3, 13, 24, 10], 26)
    femmesh.addFace([8, 10, 24, 23], 27)
    femmesh.addFace([16, 23, 24, 18], 28)
    femmesh.addFace([7, 25, 26, 11], 29)
    femmesh.addFace([6, 11, 26, 21], 30)
    femmesh.addFace([14, 21, 26, 19], 31)
    femmesh.addFace([15, 19, 26, 25], 32)
    femmesh.addFace([16, 20, 27, 23], 33)
    femmesh.addFace([8, 23, 27, 12], 34)
    femmesh.addFace([7, 12, 27, 25], 35)
    femmesh.addFace([15, 25, 27, 20], 36)
    return True
