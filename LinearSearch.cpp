// C++ code to linearly search x in arr[]. If x
// is present then return its location, otherwise
// return -1

#include <iostream>
using namespace std;

int search(int arr[], int n, int x)
{
	int i;
	for (i = 0; i < n; i++)
		if (arr[i] == x)
			return i;
	return -1;
}

// Driver code
int main(void)
{
	int n;
  cin>>n;//array size
  
    int *ar = new int[n];
  for(int i=0;i<n;i++)
    cin>>ar[i];
	int x;
  cin>>x;//Key To be searched

	// Function call
	int result = search(arr, n, x);
	(result == -1)
		? cout << "Element is not present in array"
		: cout << "Element is present at index " << result;
	return 0;
}
