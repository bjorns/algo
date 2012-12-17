#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef enum { RED, BLACK } color_t;

typedef struct node {
	int value;
	color_t color;
	struct node *left;
	struct node *right;
} node_t;

node_t* LEAF = NULL;

node_t *create_node(int value) {
	node_t *new_node = (node_t*)malloc(sizeof(node_t));
	new_node->value = value;
	new_node->color = RED;
	new_node->left = LEAF;
	new_node->right	= LEAF;
	return new_node;
}


node_t* insert(node_t* tree, node_t *new_node) {
	if (tree == NULL) {
		return new_node;
	} else {
		if (new_node->value <= tree->value) {
			tree->left = insert(tree->left, new_node);
		} else {
			tree->right = insert(tree->right, new_node);
		}
		return tree;
	}
}

const char* color_str(color_t color) {
	if (color == RED)
		return "Red";
	else if (color == BLACK)
		return "Black";
	else
		return "Blue"; // Should not happen.
}

// Returns next usable index.
int render_tree(FILE *file, node_t *tree, int nodeNbr) {
	if (tree == NULL)
		return nodeNbr;
	int current = nodeNbr;
	fprintf(file,"  Node%d [label=\"%d\", style=filled, color=Black, fillcolor=%s, fontcolor=Black]\n", current, tree->value, color_str(tree->color));

	int left = nodeNbr + 1;
	int right = render_tree(file, tree->left, left);
	int ret = render_tree(file, tree->right, right);

	if (tree->left != NULL)
		fprintf(file, "  Node%d->Node%d\n", current, left);
	if (tree->right != NULL)
		fprintf(file, "  Node%d->Node%d\n", current, right);


	return ret;
}

int render_tree_arcs(FILE *file, node_t *tree, int nodeNbr) {
	return 0;
}

void render(node_t *tree, const char* filename) {
	FILE *file = fopen(filename,"w");
	fprintf(file,"digraph mygraph {\n");

	render_tree(file, tree, 0);

	fprintf(file,"}\n");

	fclose(file);
}

int main(int argc, char** argv) {
	node_t* tree = LEAF;

	srand(time(NULL));
	for (int i = 0; i < 100; ++i) {
		tree = insert(tree, create_node(rand() % 100));
	}

	render(tree, "redblack.dot");

	return 0;
}