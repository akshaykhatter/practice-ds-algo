#include<iostream>
using namespace std;

int main() {
	
	int n = 0;
	cin>>n;
	
	int l_s = 1; // left side of symmetry line
	int r_s = n * n + 2 * n + 2; // right side of symmetry line
	
	for(int i = 0; i < n; i++) {
		for(int s = 0; s < (2 * i); s++) {
			cout<<'-';
		}
		
		for(int j = 0; j < (n - i); j++) {
			
			cout<<l_s++;
			
			if(j != (n - i - 1)) {
				cout<<"*";
			}
		}
		
		cout<<"*";
		
		r_s = r_s - 2 * (n - i) - 1;
		
		for(int j = 0; j < (n - i); j++) {
			
			cout<<r_s++;			
			
			if(j != (n - i - 1)) {
				cout<<"*";
			}
		}
		
		cout<<endl;
	}
	
	return 0;
}
