# ranksToRows = {0:'10',1:'9', 2:'8', 3:'7', 4:'6', 5:'5', 6:'4', 7:'3', 8:'2', 9:'1'}
# ranksToCols = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i'}
# print(ranksToRows)
# print(ranksToCols)
# x=1
# y=5
# stayaway = [(x,y),(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
# candidate = [(x,y) for x in range(10) if (x,y) not in stayaway ] + [(x,y) for y in range(9) if (x,y) not in stayaway ]

board= [
        #     ['bxe','bma','bvo','bsi','btu','bsi','bvo','bma','bxe'],
        #     ['---','---','---','---','---','rch','---','---','---'],
        #     ['---','bph','---','---','---','---','---','bph','---'],
        #     ['bch','---','---','---','bch','---','bch','rma','bch'],
        #     ['---','---','---','---','---','---','---','---','---'],
        #     ['---','---','---','---','---','---','---','---','---'],
        #     ['rch','---','rch','---','rch','---','---','---','rch'],
        #     ['---','rph','---','---','---','---','---','rph','---'],
        #     ['---','---','---','bch','---','---','---','---','---'],
        #     ['rxe','rma','rvo','rsi','rtu','rsi','rvo','---','rxe']
        # ]
        
        # [
            ['bxe','bma','bvo','bsi','btu','bsi','bvo','bma','bxe'],
            ['---','---','---','---','---','---','---','---','---'],
            ['---','bph','---','---','---','---','---','bph','---'],
            ['bch','---','bch','---','bch','---','bch','---','bch'],
            ['---','---','---','---','---','---','---','---','---'],
            ['---','---','---','---','---','---','---','---','---'],
            ['rch','---','rch','---','rch','---','rch','---','rch'],
            ['---','rph','---','---','---','---','---','rph','---'],
            ['---','---','---','---','---','---','---','---','---'],
            ['rxe','rma','rvo','rsi','rtu','rsi','rvo','rma','rxe']
        ]
# for i in range(10):
#     for j in range(9):
#         if board[i][j][0] == 'r':
#             board[i][j] = 'b'+ board[i][j][1:]
#         elif board[i][j][0]== 'b':
#             board[i][j] = 'r'+ board[i][j][1:]
            
# print(board)
# import csv
# position = {'xe':[], 'ma':[], 'tuong':[], 'si':[], 'tuong':[], 'phao':[], 'chot':[]}
# for i in position.keys():
#     name = i+'.csv'
#     with open ('C:/Users/OnDoing/ChineseChess/unity/'+name, 'r') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             for r in range(len(row)):
#                 row[r] = float(row[r])
#             position[i] += [row]
            
            
# # for i in position.keys():
# #     print(i, position[i])

# bxe = position['xe'][::-1]
# print(bxe)


board = [[0 for i in range(5)] for j in range(4)]
a=1
for i in range(4):
    for j in range(5):
        board[i][j]= a
        a = a+1

for i in range(4):
    print(board[i])
b = board[::-1]
for i in range(4):
    print(b[i])