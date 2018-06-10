import json

def getdata(lst,index):
    l = len(lst)
    return index>1 and lst[index-1] or 0 , index<l-1 and lst[index+1] or 0
if __name__ =="__main__":
    m = {}
    data =[ i["bus_stops"] for i in  json.load(open("buslines.json"))]
    for i in data:
        for j,k in enumerate(i):
            if k in m :
                a ,b = getdata(i,j)
                if a : m[k].update([a])
                if b : m[k].update([b])
            else:
                a ,b = getdata(i,j)
                s=set()
                if a : s.update([a])
                if b : s.update([b])
                m[k]=s



def bfs_path(start,end,graph):
    data = [start ,[ start, ] ] # start ,[path]
    st = [data]
    visited = []
    while st :
        x ,path = st.pop(0)
        for neighbour in graph[x]:
            if not  neighbour in visited:
                if end == neighbour : return path+[neighbour]
                visited.append(neighbour)
                st.append( [neighbour, path + [neighbour]] )
    return visited
for i ,v in m.items():m[i]=list(v)
if __name__=="__main__":

    #print(json.dumps(m,ensure_ascii=False))
    graph = json.load(open("ybs_graph/ybs_graph.json"))
    print(bfs_path(' ဂိတ်ဟောင်း',  ' သစ်ဆိုင်ကွေ့',graph))
    print(bfs_path(' ဂိတ်ဟောင်း', ' ဆည်မြောင်း',graph))
    print(bfs_path(' သိမ်ဖြူစာတိုက်', ' လှည်းတန်းဈေး',graph))

