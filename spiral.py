import turtle
from random import randint
turtle.bgcolor("black")
seurat=turtle.Turtle()
width=5
height=7
dot_distance=25
seurat.setpos(-250,250)
seurat.penup()
list_color=['white','yellow','brown','red','blue','green','orange','pink','violet','grey','cyan']
def spiral(m,n):
    k=0 #index of starting row
    l=0 #index of stating column
    f=0
    col=randint(0,10)
    seurat.color(list_color[col])
    while(k<m and l<n):
        if(f==1):
            seurat.right(90)
        #printing first row
        for i in range(l,n):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[k][i],end=' ')
        k+=1
        f=1
        seurat.right(90)
        col=randint(0,10)
        seurat.color(list_color[col])
        #printing last column
        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[i][n-1],end=' ')
        n-=1
        seurat.right(90)
        col=randint(0,10)
        seurat.color(list_color[col])
        if(k<m):
            #printing last row
            for i in range(n-1,l-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[m-1][i],end=' ')
            m-=1
        seurat.right(90)
        col=randint(0,10)
        seurat.color(list_color[col])
        if(l<n):
            #printing first column
            for i in range(m-1,k-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[i][l],end=' ')
            l+=1
'''            
a=[]
count=1
for i in range(4):
    l=[]
    for j in range(4):
        l.append(count)
        count+=1
    a.append(l)
'''
spiral(20,20)
turtle.done()
