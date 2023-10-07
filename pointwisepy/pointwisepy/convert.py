def extractNastranData(nasFile,outputFile):
    """Open NAS file and output number of PSHELLs, nodes and elements (boundary faces). Used with NastranToFro. Redundant with /home/eg916039/codes/NastranToFro"""
    with open(nasFile, "r") as f:
        for line in f:
            if line.startswith('PSHELL'):
                pshell_line = line
            elif line.startswith('GRID'):
                grid_line = line
            elif line.startswith('CTRIA3'):
                ctria3_line = line
            else:
                None

        pshell_line = pshell_line.split('PSHELL,')[1]
        pshell_line = pshell_line.split(',')[0]
        PSHELL = int(pshell_line)
        
        grid_line = grid_line.split('GRID')[1]
        grid_line = grid_line.split(',')[1]
        GRID = int(grid_line)
        
        ctria3_line = ctria3_line.split('CTRIA3,')[1]
        ctria3_line = ctria3_line.split(',')[0]
        CTRIA3 = int(ctria3_line)

    f = open(outputFile, "w")
    f.write("PSHELLS: {}\nNodes: {}\nElements/Boundary Faces: {}".format(PSHELL,GRID,CTRIA3))
    f.close()