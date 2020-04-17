class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  def setRight(self,node):
    self.right=node

  def setLeft(self,node):
    self.left=node

  def PrintTree(self):
    print(self.data)

def arbol(node):
    if node.left!=None:
        arbol(node.left)
    print('data: ' + node.data)
    if node.right!=None:
        arbol(node.right)

data_path = "../data/medium_Tree.in"
f = open(data_path, "r")
lines = f.readlines()
nodos=[]
for i in range(len(lines)):
  a = lines[i]
  #a='5 3 2 # 6 1 # # # 4 0'
  dividir = a.split(' ')
  huecos=0
  j=0
  while j <len(dividir):
    if j==0:
      root = Node(dividir[j])
      nodos.append(root)
    else:
      node = nodos[int((j + huecos - 1) / 2)]
      if node.data == None:
        newNode = Node(None)
        j = j - 1
        huecos = huecos + 1
      elif dividir[j]=='#':
        newNode=Node(None)
      else:
        newNode = Node(dividir[j])
        if j%2==0:
          node.setRight(newNode)
        else:
          node.setLeft(newNode)
      nodos.append(newNode)
    j=j+1

a=[]
for i in nodos:
  a.append(i.data)
print(a)
arbol(root)