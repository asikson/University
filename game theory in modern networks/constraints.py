# n = 2
# getConstraintsForVN = [
#     {'type': 'ineq', 'fun': lambda x: x[0] - x[2]},
#     {'type': 'ineq', 'fun': lambda x: x[1] - x[3]},
# ]

# n = 4
# getConstraintsForVN = [
#     {'type': 'ineq', 'fun': lambda x: x[0] - x[4]},
#     {'type': 'ineq', 'fun': lambda x: x[1] - x[5]},
#     {'type': 'ineq', 'fun': lambda x: x[2] - x[6]},
#     {'type': 'ineq', 'fun': lambda x: x[3] - x[7]},
# ]

# n = 6
# getConstraintsForVN = [
#     {'type': 'ineq', 'fun': lambda x: x[0] - x[6]},
#     {'type': 'ineq', 'fun': lambda x: x[1] - x[7]},
#     {'type': 'ineq', 'fun': lambda x: x[2] - x[8]},
#     {'type': 'ineq', 'fun': lambda x: x[3] - x[9]},
#     {'type': 'ineq', 'fun': lambda x: x[4] - x[10]},
#     {'type': 'ineq', 'fun': lambda x: x[5] - x[11]},
# ]

# n = 8
# getConstraintsForVN = [
#     {'type': 'ineq', 'fun': lambda x: x[0] - x[8]},
#     {'type': 'ineq', 'fun': lambda x: x[1] - x[9]},
#     {'type': 'ineq', 'fun': lambda x: x[2] - x[10]},
#     {'type': 'ineq', 'fun': lambda x: x[3] - x[11]},
#     {'type': 'ineq', 'fun': lambda x: x[4] - x[12]},
#     {'type': 'ineq', 'fun': lambda x: x[5] - x[13]},
#     {'type': 'ineq', 'fun': lambda x: x[6] - x[14]},
#     {'type': 'ineq', 'fun': lambda x: x[7] - x[15]},
# ]

# n = 10
getConstraintsForVN = [
    {'type': 'ineq', 'fun': lambda x: x[0] - x[10]},
    {'type': 'ineq', 'fun': lambda x: x[1] - x[11]},
    {'type': 'ineq', 'fun': lambda x: x[2] - x[12]},
    {'type': 'ineq', 'fun': lambda x: x[3] - x[13]},
    {'type': 'ineq', 'fun': lambda x: x[4] - x[14]},
    {'type': 'ineq', 'fun': lambda x: x[5] - x[15]},
    {'type': 'ineq', 'fun': lambda x: x[6] - x[16]},
    {'type': 'ineq', 'fun': lambda x: x[7] - x[17]},
    {'type': 'ineq', 'fun': lambda x: x[8] - x[18]},
    {'type': 'ineq', 'fun': lambda x: x[9] - x[19]}
]

###########################################################################

# n = 2
# def getAdditionalConstraintForVN(minYk):
#     return [
#         {'type': 'ineq', 'fun': lambda x: x[0] + x[1] - minYk}
#     ]

# n = 4
# def getAdditionalConstraintForVN(minYk):
#     return [
#         {'type': 'ineq', 'fun': lambda x: x[0] + x[1] + x[2] + x[3] - minYk}
#     ]

# n = 6
# def getAdditionalConstraintForVN(minYk):
#     return [
#         {'type': 'ineq', 'fun': lambda x: x[0] + x[1] + x[2] + x[3] + x[4] + x[5] - minYk}
#     ]

# n = 8
# def getAdditionalConstraintForVN(minYk):
#     return [
#         {'type': 'ineq', 'fun': lambda x: x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7] - minYk}
#     ]

# n = 10
def getAdditionalConstraintForVN(minYk):
    return [
        {'type': 'ineq', 'fun': lambda x: x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7] + x[8] + x[9] - minYk}
    ]


###########################################################################

# n = 2, m = 2
# def getAdditionalConstraints(minYks):
#     return [
#         {'type': 'ineq', 'fun': lambda x: x[0] + x[1] - minYks[0]},
#         {'type': 'ineq', 'fun': lambda x: x[4] + x[5] - minYks[1]},
#     ]

# n = 4, m = 2
# def getAdditionalConstraints(minYks):
#     return [
#         {'type': 'ineq', 'fun': lambda x: x[0] + x[1] + x[2] + x[3] - minYks[0]},
#         {'type': 'ineq', 'fun': lambda x: x[8] + x[9] + x[10] + x[11] - minYks[1]},
#     ]

# n = 6, m = 2
# def getAdditionalConstraints(minYks):
#     return [
#         {'type': 'ineq', 'fun': lambda x: x[0] + x[1] + x[2] + x[3] + x[4] + x[5] - minYks[0]},
#         {'type': 'ineq', 'fun': lambda x: x[12] + x[13] + x[14] + x[15] + x[16] + x[17] - minYks[1]},
#     ]

# n = 8, m = 2
# def getAdditionalConstraints(minYks):
#     return [
#         {'type': 'ineq', 'fun': lambda x: x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7] - minYks[0]},
#         {'type': 'ineq', 'fun': lambda x: x[16] + x[17] + x[18] + x[19] + x[20] + x[21] + x[22] + x[23] - minYks[1]},
#     ]

# n = 10, m = 2
def getAdditionalConstraints(minYks):
    return [
        {'type': 'ineq', 'fun': lambda x: x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7] + x[8] + x[9] - minYks[0]},
        {'type': 'ineq', 'fun': lambda x: x[20] + x[21] + x[22] + x[23] + x[24] + x[25] + x[26] + x[27] + x[28] + x[29] - minYks[1]},
    ]

# n = 2, m = 7
# def getAdditionalConstraints(minYks):
#     return [
#         {'type': 'ineq', 'fun': lambda x: x[0] + x[1] - minYks[0]},
#         {'type': 'ineq', 'fun': lambda x: x[4] + x[5] - minYks[1]},
#         {'type': 'ineq', 'fun': lambda x: x[8] + x[9] - minYks[2]},
#         {'type': 'ineq', 'fun': lambda x: x[12] + x[13] - minYks[3]},
#         {'type': 'ineq', 'fun': lambda x: x[16] + x[17] - minYks[4]},
#         {'type': 'ineq', 'fun': lambda x: x[20] + x[21] - minYks[5]},
#         {'type': 'ineq', 'fun': lambda x: x[24] + x[25] - minYks[6]}
#     ]

# n = 2, m = 12
# def getAdditionalConstraints(minYks):
#     return [
#         {'type': 'ineq', 'fun': lambda x: x[0] + x[1] - minYks[0]},
#         {'type': 'ineq', 'fun': lambda x: x[4] + x[5] - minYks[1]},
#         {'type': 'ineq', 'fun': lambda x: x[8] + x[9] - minYks[2]},
#         {'type': 'ineq', 'fun': lambda x: x[12] + x[13] - minYks[3]},
#         {'type': 'ineq', 'fun': lambda x: x[16] + x[17] - minYks[4]},
#         {'type': 'ineq', 'fun': lambda x: x[20] + x[21] - minYks[5]},
#         {'type': 'ineq', 'fun': lambda x: x[24] + x[25] - minYks[6]},
#         {'type': 'ineq', 'fun': lambda x: x[28] + x[29] - minYks[7]},
#         {'type': 'ineq', 'fun': lambda x: x[32] + x[33] - minYks[8]},
#         {'type': 'ineq', 'fun': lambda x: x[36] + x[37] - minYks[9]},
#         {'type': 'ineq', 'fun': lambda x: x[40] + x[41] - minYks[10]},
#         {'type': 'ineq', 'fun': lambda x: x[44] + x[45] - minYks[11]}
#     ]

# n = 2, m = 17
# def getAdditionalConstraints(minYks):
#     return [
#         {'type': 'ineq', 'fun': lambda x: x[0] + x[1] - minYks[0]},
#         {'type': 'ineq', 'fun': lambda x: x[4] + x[5] - minYks[1]},
#         {'type': 'ineq', 'fun': lambda x: x[8] + x[9] - minYks[2]},
#         {'type': 'ineq', 'fun': lambda x: x[12] + x[13] - minYks[3]},
#         {'type': 'ineq', 'fun': lambda x: x[16] + x[17] - minYks[4]},
#         {'type': 'ineq', 'fun': lambda x: x[20] + x[21] - minYks[5]},
#         {'type': 'ineq', 'fun': lambda x: x[24] + x[25] - minYks[6]},
#         {'type': 'ineq', 'fun': lambda x: x[28] + x[29] - minYks[7]},
#         {'type': 'ineq', 'fun': lambda x: x[32] + x[33] - minYks[8]},
#         {'type': 'ineq', 'fun': lambda x: x[36] + x[37] - minYks[9]},
#         {'type': 'ineq', 'fun': lambda x: x[40] + x[41] - minYks[10]},
#         {'type': 'ineq', 'fun': lambda x: x[44] + x[45] - minYks[11]},
#         {'type': 'ineq', 'fun': lambda x: x[48] + x[49] - minYks[12]},
#         {'type': 'ineq', 'fun': lambda x: x[52] + x[53] - minYks[13]},
#         {'type': 'ineq', 'fun': lambda x: x[56] + x[57] - minYks[14]},
#         {'type': 'ineq', 'fun': lambda x: x[60] + x[61] - minYks[15]},
#         {'type': 'ineq', 'fun': lambda x: x[64] + x[65] - minYks[16]}
#     ]

# n = 2, m = 22
# def getAdditionalConstraints(minYks):
#     return [
#         {'type': 'ineq', 'fun': lambda x: x[0] + x[1] - minYks[0]},
#         {'type': 'ineq', 'fun': lambda x: x[4] + x[5] - minYks[1]},
#         {'type': 'ineq', 'fun': lambda x: x[8] + x[9] - minYks[2]},
#         {'type': 'ineq', 'fun': lambda x: x[12] + x[13] - minYks[3]},
#         {'type': 'ineq', 'fun': lambda x: x[16] + x[17] - minYks[4]},
#         {'type': 'ineq', 'fun': lambda x: x[20] + x[21] - minYks[5]},
#         {'type': 'ineq', 'fun': lambda x: x[24] + x[25] - minYks[6]},
#         {'type': 'ineq', 'fun': lambda x: x[28] + x[29] - minYks[7]},
#         {'type': 'ineq', 'fun': lambda x: x[32] + x[33] - minYks[8]},
#         {'type': 'ineq', 'fun': lambda x: x[36] + x[37] - minYks[9]},
#         {'type': 'ineq', 'fun': lambda x: x[40] + x[41] - minYks[10]},
#         {'type': 'ineq', 'fun': lambda x: x[44] + x[45] - minYks[11]},
#         {'type': 'ineq', 'fun': lambda x: x[48] + x[49] - minYks[12]},
#         {'type': 'ineq', 'fun': lambda x: x[52] + x[53] - minYks[13]},
#         {'type': 'ineq', 'fun': lambda x: x[56] + x[57] - minYks[14]},
#         {'type': 'ineq', 'fun': lambda x: x[60] + x[61] - minYks[15]},
#         {'type': 'ineq', 'fun': lambda x: x[64] + x[65] - minYks[16]},
#         {'type': 'ineq', 'fun': lambda x: x[68] + x[69] - minYks[17]},
#         {'type': 'ineq', 'fun': lambda x: x[72] + x[73] - minYks[18]},
#         {'type': 'ineq', 'fun': lambda x: x[76] + x[77] - minYks[19]},
#         {'type': 'ineq', 'fun': lambda x: x[80] + x[81] - minYks[20]},
#         {'type': 'ineq', 'fun': lambda x: x[84] + x[85] - minYks[21]}
#     ]

###########################################################################

# n = 2, m = 2
# getConstraints = [
#         {'type': 'ineq', 'fun': lambda x: x[0] - x[2]},
#         {'type': 'ineq', 'fun': lambda x: x[1] - x[3]},

#         {'type': 'ineq', 'fun': lambda x: x[4] - x[6]},
#         {'type': 'ineq', 'fun': lambda x: x[5] - x[7]}
# ]

# n = 4, m = 2
# getConstraints = [
#         {'type': 'ineq', 'fun': lambda x: x[0] - x[4]},
#         {'type': 'ineq', 'fun': lambda x: x[1] - x[5]},
#         {'type': 'ineq', 'fun': lambda x: x[2] - x[6]},
#         {'type': 'ineq', 'fun': lambda x: x[3] - x[7]},

#         {'type': 'ineq', 'fun': lambda x: x[8] - x[12]},
#         {'type': 'ineq', 'fun': lambda x: x[9] - x[13]},
#         {'type': 'ineq', 'fun': lambda x: x[10] - x[14]},
#         {'type': 'ineq', 'fun': lambda x: x[11] - x[15]},
# ]

# n = 6, m = 2
# getConstraints = [
#         {'type': 'ineq', 'fun': lambda x: x[0] - x[6]},
#         {'type': 'ineq', 'fun': lambda x: x[1] - x[7]},
#         {'type': 'ineq', 'fun': lambda x: x[2] - x[8]},
#         {'type': 'ineq', 'fun': lambda x: x[3] - x[9]},
#         {'type': 'ineq', 'fun': lambda x: x[4] - x[10]},
#         {'type': 'ineq', 'fun': lambda x: x[5] - x[11]},

#         {'type': 'ineq', 'fun': lambda x: x[12] - x[18]},
#         {'type': 'ineq', 'fun': lambda x: x[13] - x[19]},
#         {'type': 'ineq', 'fun': lambda x: x[14] - x[20]},
#         {'type': 'ineq', 'fun': lambda x: x[15] - x[21]},
#         {'type': 'ineq', 'fun': lambda x: x[16] - x[22]},
#         {'type': 'ineq', 'fun': lambda x: x[17] - x[23]},
# ]

# n = 8, m = 2
# getConstraints = [
#         {'type': 'ineq', 'fun': lambda x: x[0] - x[8]},
#         {'type': 'ineq', 'fun': lambda x: x[1] - x[9]},
#         {'type': 'ineq', 'fun': lambda x: x[2] - x[10]},
#         {'type': 'ineq', 'fun': lambda x: x[3] - x[11]},
#         {'type': 'ineq', 'fun': lambda x: x[4] - x[12]},
#         {'type': 'ineq', 'fun': lambda x: x[5] - x[13]},
#         {'type': 'ineq', 'fun': lambda x: x[6] - x[14]},
#         {'type': 'ineq', 'fun': lambda x: x[7] - x[15]},

#         {'type': 'ineq', 'fun': lambda x: x[16] - x[24]},
#         {'type': 'ineq', 'fun': lambda x: x[17] - x[25]},
#         {'type': 'ineq', 'fun': lambda x: x[18] - x[26]},
#         {'type': 'ineq', 'fun': lambda x: x[19] - x[27]},
#         {'type': 'ineq', 'fun': lambda x: x[20] - x[28]},
#         {'type': 'ineq', 'fun': lambda x: x[21] - x[29]},
#         {'type': 'ineq', 'fun': lambda x: x[22] - x[30]},
#         {'type': 'ineq', 'fun': lambda x: x[23] - x[31]},
# ]

# n = 10, m = 2
getConstraints = [
        {'type': 'ineq', 'fun': lambda x: x[0] - x[10]},
        {'type': 'ineq', 'fun': lambda x: x[1] - x[11]},
        {'type': 'ineq', 'fun': lambda x: x[2] - x[12]},
        {'type': 'ineq', 'fun': lambda x: x[3] - x[13]},
        {'type': 'ineq', 'fun': lambda x: x[4] - x[14]},
        {'type': 'ineq', 'fun': lambda x: x[5] - x[15]},
        {'type': 'ineq', 'fun': lambda x: x[6] - x[16]},
        {'type': 'ineq', 'fun': lambda x: x[7] - x[17]},
        {'type': 'ineq', 'fun': lambda x: x[8] - x[18]},
        {'type': 'ineq', 'fun': lambda x: x[9] - x[19]},

        {'type': 'ineq', 'fun': lambda x: x[20] - x[30]},
        {'type': 'ineq', 'fun': lambda x: x[21] - x[31]},
        {'type': 'ineq', 'fun': lambda x: x[22] - x[32]},
        {'type': 'ineq', 'fun': lambda x: x[23] - x[33]},
        {'type': 'ineq', 'fun': lambda x: x[24] - x[34]},
        {'type': 'ineq', 'fun': lambda x: x[25] - x[35]},
        {'type': 'ineq', 'fun': lambda x: x[26] - x[36]},
        {'type': 'ineq', 'fun': lambda x: x[27] - x[37]},
        {'type': 'ineq', 'fun': lambda x: x[28] - x[38]},
        {'type': 'ineq', 'fun': lambda x: x[29] - x[39]},
]


# n = 2, m = 7
# getConstraints = [
#         {'type': 'ineq', 'fun': lambda x: x[0] - x[2]},
#         {'type': 'ineq', 'fun': lambda x: x[1] - x[3]},

#         {'type': 'ineq', 'fun': lambda x: x[4] - x[6]},
#         {'type': 'ineq', 'fun': lambda x: x[5] - x[7]},

#         {'type': 'ineq', 'fun': lambda x: x[8] - x[10]},
#         {'type': 'ineq', 'fun': lambda x: x[9] - x[11]},

#         {'type': 'ineq', 'fun': lambda x: x[12] - x[14]},
#         {'type': 'ineq', 'fun': lambda x: x[13] - x[15]},

#         {'type': 'ineq', 'fun': lambda x: x[16] - x[18]},
#         {'type': 'ineq', 'fun': lambda x: x[17] - x[19]},

#         {'type': 'ineq', 'fun': lambda x: x[20] - x[22]},
#         {'type': 'ineq', 'fun': lambda x: x[21] - x[23]},

#         {'type': 'ineq', 'fun': lambda x: x[24] - x[26]},
#         {'type': 'ineq', 'fun': lambda x: x[25] - x[27]},
#     ]

# n = 2, m = 12
# getConstraints = [
    #     {'type': 'ineq', 'fun': lambda x: x[0] - x[2]},
    #     {'type': 'ineq', 'fun': lambda x: x[1] - x[3]},

    #     {'type': 'ineq', 'fun': lambda x: x[4] - x[6]},
    #     {'type': 'ineq', 'fun': lambda x: x[5] - x[7]},

    #     {'type': 'ineq', 'fun': lambda x: x[8] - x[10]},
    #     {'type': 'ineq', 'fun': lambda x: x[9] - x[11]},

    #     {'type': 'ineq', 'fun': lambda x: x[12] - x[14]},
    #     {'type': 'ineq', 'fun': lambda x: x[13] - x[15]},

    #     {'type': 'ineq', 'fun': lambda x: x[16] - x[18]},
    #     {'type': 'ineq', 'fun': lambda x: x[17] - x[19]},

    #     {'type': 'ineq', 'fun': lambda x: x[20] - x[22]},
    #     {'type': 'ineq', 'fun': lambda x: x[21] - x[23]},

    #     {'type': 'ineq', 'fun': lambda x: x[24] - x[26]},
    #     {'type': 'ineq', 'fun': lambda x: x[25] - x[27]},

    #     {'type': 'ineq', 'fun': lambda x: x[28] - x[30]},
    #     {'type': 'ineq', 'fun': lambda x: x[29] - x[31]},

    #     {'type': 'ineq', 'fun': lambda x: x[32] - x[34]},
    #     {'type': 'ineq', 'fun': lambda x: x[33] - x[35]},

    #     {'type': 'ineq', 'fun': lambda x: x[36] - x[38]},
    #     {'type': 'ineq', 'fun': lambda x: x[37] - x[39]},

    #     {'type': 'ineq', 'fun': lambda x: x[40] - x[42]},
    #     {'type': 'ineq', 'fun': lambda x: x[41] - x[43]},

    #     {'type': 'ineq', 'fun': lambda x: x[44] - x[46]},
    #     {'type': 'ineq', 'fun': lambda x: x[45] - x[47]},
    # ]

# n = 2, m = 17
# getConstraints = [
#         {'type': 'ineq', 'fun': lambda x: x[0] - x[2]},
#         {'type': 'ineq', 'fun': lambda x: x[1] - x[3]},

#         {'type': 'ineq', 'fun': lambda x: x[4] - x[6]},
#         {'type': 'ineq', 'fun': lambda x: x[5] - x[7]},

#         {'type': 'ineq', 'fun': lambda x: x[8] - x[10]},
#         {'type': 'ineq', 'fun': lambda x: x[9] - x[11]},

#         {'type': 'ineq', 'fun': lambda x: x[12] - x[14]},
#         {'type': 'ineq', 'fun': lambda x: x[13] - x[15]},

#         {'type': 'ineq', 'fun': lambda x: x[16] - x[18]},
#         {'type': 'ineq', 'fun': lambda x: x[17] - x[19]},

#         {'type': 'ineq', 'fun': lambda x: x[20] - x[22]},
#         {'type': 'ineq', 'fun': lambda x: x[21] - x[23]},

#         {'type': 'ineq', 'fun': lambda x: x[24] - x[26]},
#         {'type': 'ineq', 'fun': lambda x: x[25] - x[27]},

#         {'type': 'ineq', 'fun': lambda x: x[28] - x[30]},
#         {'type': 'ineq', 'fun': lambda x: x[29] - x[31]},

#         {'type': 'ineq', 'fun': lambda x: x[32] - x[34]},
#         {'type': 'ineq', 'fun': lambda x: x[33] - x[35]},

#         {'type': 'ineq', 'fun': lambda x: x[36] - x[38]},
#         {'type': 'ineq', 'fun': lambda x: x[37] - x[39]},

#         {'type': 'ineq', 'fun': lambda x: x[40] - x[42]},
#         {'type': 'ineq', 'fun': lambda x: x[41] - x[43]},

#         {'type': 'ineq', 'fun': lambda x: x[44] - x[46]},
#         {'type': 'ineq', 'fun': lambda x: x[45] - x[47]},

#         {'type': 'ineq', 'fun': lambda x: x[48] - x[50]},
#         {'type': 'ineq', 'fun': lambda x: x[49] - x[51]},

#         {'type': 'ineq', 'fun': lambda x: x[52] - x[54]},
#         {'type': 'ineq', 'fun': lambda x: x[53] - x[55]},

#         {'type': 'ineq', 'fun': lambda x: x[56] - x[58]},
#         {'type': 'ineq', 'fun': lambda x: x[57] - x[59]},

#         {'type': 'ineq', 'fun': lambda x: x[60] - x[62]},
#         {'type': 'ineq', 'fun': lambda x: x[61] - x[63]},

#         {'type': 'ineq', 'fun': lambda x: x[64] - x[66]},
#         {'type': 'ineq', 'fun': lambda x: x[65] - x[67]},
#     ]

# n = 2, m = 22
# getConstraints = [
#         {'type': 'ineq', 'fun': lambda x: x[0] - x[2]},
#         {'type': 'ineq', 'fun': lambda x: x[1] - x[3]},

#         {'type': 'ineq', 'fun': lambda x: x[4] - x[6]},
#         {'type': 'ineq', 'fun': lambda x: x[5] - x[7]},

#         {'type': 'ineq', 'fun': lambda x: x[8] - x[10]},
#         {'type': 'ineq', 'fun': lambda x: x[9] - x[11]},

#         {'type': 'ineq', 'fun': lambda x: x[12] - x[14]},
#         {'type': 'ineq', 'fun': lambda x: x[13] - x[15]},

#         {'type': 'ineq', 'fun': lambda x: x[16] - x[18]},
#         {'type': 'ineq', 'fun': lambda x: x[17] - x[19]},

#         {'type': 'ineq', 'fun': lambda x: x[20] - x[22]},
#         {'type': 'ineq', 'fun': lambda x: x[21] - x[23]},

#         {'type': 'ineq', 'fun': lambda x: x[24] - x[26]},
#         {'type': 'ineq', 'fun': lambda x: x[25] - x[27]},

#         {'type': 'ineq', 'fun': lambda x: x[28] - x[30]},
#         {'type': 'ineq', 'fun': lambda x: x[29] - x[31]},

#         {'type': 'ineq', 'fun': lambda x: x[32] - x[34]},
#         {'type': 'ineq', 'fun': lambda x: x[33] - x[35]},

#         {'type': 'ineq', 'fun': lambda x: x[36] - x[38]},
#         {'type': 'ineq', 'fun': lambda x: x[37] - x[39]},

#         {'type': 'ineq', 'fun': lambda x: x[40] - x[42]},
#         {'type': 'ineq', 'fun': lambda x: x[41] - x[43]},

#         {'type': 'ineq', 'fun': lambda x: x[44] - x[46]},
#         {'type': 'ineq', 'fun': lambda x: x[45] - x[47]},

#         {'type': 'ineq', 'fun': lambda x: x[48] - x[50]},
#         {'type': 'ineq', 'fun': lambda x: x[49] - x[51]},

#         {'type': 'ineq', 'fun': lambda x: x[52] - x[54]},
#         {'type': 'ineq', 'fun': lambda x: x[53] - x[55]},

#         {'type': 'ineq', 'fun': lambda x: x[56] - x[58]},
#         {'type': 'ineq', 'fun': lambda x: x[57] - x[59]},

#         {'type': 'ineq', 'fun': lambda x: x[60] - x[62]},
#         {'type': 'ineq', 'fun': lambda x: x[61] - x[63]},

#         {'type': 'ineq', 'fun': lambda x: x[64] - x[66]},
#         {'type': 'ineq', 'fun': lambda x: x[65] - x[67]},

#         {'type': 'ineq', 'fun': lambda x: x[68] - x[70]},
#         {'type': 'ineq', 'fun': lambda x: x[69] - x[71]},

#         {'type': 'ineq', 'fun': lambda x: x[72] - x[74]},
#         {'type': 'ineq', 'fun': lambda x: x[73] - x[75]},

#         {'type': 'ineq', 'fun': lambda x: x[76] - x[78]},
#         {'type': 'ineq', 'fun': lambda x: x[77] - x[79]},

#         {'type': 'ineq', 'fun': lambda x: x[80] - x[82]},
#         {'type': 'ineq', 'fun': lambda x: x[81] - x[83]},

#         {'type': 'ineq', 'fun': lambda x: x[84] - x[86]},
#         {'type': 'ineq', 'fun': lambda x: x[85] - x[87]},
#     ]