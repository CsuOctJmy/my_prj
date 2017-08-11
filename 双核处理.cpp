#include<iostream>
#include<algorithm>
#include<set>
using namespace std;
int n;
int a[51];
set<int>s;
int sum=0;
int main(){
    cin>>n;
    for(int i=0;i<n;i++){
        int tmp;
        cin>>tmp;
        a[i]=tmp/1024;
        sum+=a[i];
    }
    s.insert(0);
    for(int i=0;i<n;i++){
        set<int>added;
        for(set<int>::iterator it=s.begin();it!=s.end();it++){
            added.insert(*it+a[i]);
        }
        s.insert(added.begin(),added.end());
    }
    int ans=sum;
    for(set<int>::iterator it=s.begin();it!=s.end();it++){
        ans=min(ans,max(*it,sum-*it));
    }
    cout<<ans*1024<<endl;
}