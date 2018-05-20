#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
map< pair<string,string> ,ll>cost;
map<string,vector<string> >graph;
map<string, ll>dis;
set<string>uniq;
set<string>::iterator it;
map<string,string>path;
ll shortest_path(string src)
{
    ll i,j,k,l;
    string str,tm;
    for(it=uniq.begin(); it!=uniq.end(); it++)
    {
        dis[*it]=LLONG_MAX;
    }
    queue<string>q;
    q.push(src);
    dis[src]=0;
    while(!q.empty())
    {
        string adj=q.front();
        for(i=0; i<graph[adj].size(); i++)
        {
            tm=graph[adj][i];
            if((dis[adj]+cost[make_pair(adj,tm)])<dis[tm])
            {
                dis[tm]=(dis[adj]+cost[make_pair(adj,tm)]);
                q.push(tm);
                path[tm]=adj;
            }
        }
        q.pop();
    }
    return 0;
}
int main()
{
    ll i,j,station,road,cst;
    printf("\n\n\t\t\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\n");
    printf("\t\t\xB1@ WELCOME TO MY PIZZA DELIVARY PROJECT @\xB1\n");
    printf("\t\t\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\xB1\n");
    string nod1,nod2;
    cout<<"\nHow many station and road.."<<endl;
    cin>>station>>road;
    cout<<"Now give me the road connection and Distance :"<<endl;
    for(i=0; i<road; i++)
    {
        cin>>nod1>>nod2>>cst;
        graph[nod1].push_back(nod2);
        graph[nod2].push_back(nod1);
        uniq.insert(nod1);
        uniq.insert(nod2);
        cost[make_pair(nod1,nod2)]=cst;
        cost[make_pair(nod2,nod1)]=cst;
    }
    cout<<endl;
    cout<<"Now where do u want to deliver.."<<endl;
    cin>>nod1;
    shortest_path(nod1);
    cout<<"Path calculation has already done"<<endl;
    cout<<endl<<endl;
    cout<<"From which place do u want to deliver..?"<<endl;
    cin>>nod2;
    printf("\n\t\t shortest path is: %lld unit\n",dis[nod2]);
    cout<<"YOUR WAY FROM "<<nod2<<" TO "<<nod1<<" IS.... "<<endl;
    string pt=nod1;
    cout<<nod2<<" ";
    while(1)
    {
        cout<<path[nod2]<<" ";
        nod2=path[nod2];
        if(pt==path[nod2])
            break;
    }
    cout<<pt;
    return 0;
}
/*

Input:

13 19
merul Badda 4
merul Gulshan 5
merul Tbgate 3
Badda Baridhara 3
Baridhara Jamuna 2
Jamuna kuril 4
jamuna Zia 5
kuril mirpur 6
Gulshan Zia 4
Zia mirpur 5
merul harirjeel 3
hatirjeel Banani 4
Tbgate Banani 2
Banani Ecb 5
Gulshan Ecb 4
Zia Ecb 4
Ecb mirpur 5
Banani Army 3
Army mirpur 2

*/

