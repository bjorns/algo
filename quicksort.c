#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int *generate_data(int size) {
	int *data = (int*)malloc(size*sizeof(int));
	srand(time(NULL));

	for (int i = 0; i< size; ++i) {
		data[i] = rand() % 100;
	}
	return data;
}

void print(int* data, int l, int u) {
	for (int i = l; i <= u; ++i) {
		printf("%d ", data[i]);
	}
	printf("\n");
}

void swap(int* data, int l, int r) {
	int tmp = data[l];
	data[l] = data[r];
	data[r] = tmp;
}

int partition(int* data, int l, int u) {
	int pivot = data[l];
	int left = l + 1;
	int right = u;

	while (left < right) {
		if (data[left] <= pivot) {
			++left;
		} else {
			if (data[right] <= pivot)
				swap(data, left, right);
			--right;
		}
	}

	if (data[left] >= pivot) 
		--left;

	swap(data, left, l);
	return left;
}

void quicksort_recursive(int* data, int l, int u) {
	if (l >= u)
		return;
	
	int midpoint = partition(data, l, u);
	
	quicksort_recursive(data, l, midpoint - 1);
	quicksort_recursive(data, midpoint + 1, u);
}

void quicksort(int* data, int l, int u) {
	quicksort_recursive(data, l, u);
}

int main(int argc, char** argv) {
	int SIZE = 10;
	int *data = generate_data(SIZE);

	print(data, 0, SIZE-1);
	quicksort(data, 0, SIZE - 1);

	print(data, 0, SIZE-1);
	return 0;
}

