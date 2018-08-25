#include<iostream>
#include<string>
using namespace std;

int main() {
	int n, m;
	cin>>n>>m;
	string s[n];
	
	for(int i=0; i<n; i++) {
		cin>>s[i];
	}
	
	int max = 0;
	bool flag = false;
	
	// Beginning of L vertical cannot start on last row and last column
	for(int i=0; i<(n-1); i++) {
		for(int j=0; j<(m-1); j++) {
			int count = 0, count_h = 0, count_v = 0;
			
			// Check if beginning of L vertical exists
			if(s[i][j] == '.' && s[i+i][j] == '.') {
				
//				cout<<"L vertical exists" <<i<<j;
				
				// Counting elements in L vertical
				int k = i;
				for(; k<n; k++) {
					if(s[k][j] == '.') {
						count_v++;
					} else {
						break;
					}
				}
				
				// Check if beginning of L horizontal exists
				if (s[k-1][j+1] == '.') {
					
//					cout<<"L horizontal exists";
					
					// Counting elements in L horizontal
					for(int l = j+1; l<n; l++) {
						if(s[k-1][l] == '.') {
							count_h++;
						} else {
							break;
						}
					}
					
//					cout<<"L was found";
					// L is present
					flag = true;
					count = count_v + count_h;
//					cout<<count;
					if(max < count) {
						max = count;
					}
					
				} else {
					// terminate, this one is not L
					continue;
				}
			} else {
				// terminate this one is not L
			}
		}
	}
	
	if(flag) {
		cout<<"YES"<<endl;
		cout<<max;
	} else {
		cout<<"NO";
	}
}

// * * * * *
// * . * . *
// * . * . .
// * . . * *
// * * * * *
