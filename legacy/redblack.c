#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef enum { RED, BLACK } color_t;

typedef struct node {
	int value;
	color_t color;
	struct node *left;
	struct node *right;

	struct node *parent;
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

node_t *grandparent(node_t *node) {
	if (node->parent != NULL && node->parent->parent != NULL) {
		return node->parent->parent;
	} else {
		return NULL;
	}
}

node_t *uncle(node_t *node) {
	node_t *g = grandparent(node);
	if (g != NULL) {
		if (g->left == node->parent)
			return g->right;
		else
			return g->left;
	}
	return NULL;
}

void color_case1(node_t *);
void color_case2(node_t *);
void color_case3(node_t *);
void color_case4(node_t *);

void color_case1(node_t *node) {
	if (node->parent == NULL) {
		node->color = BLACK; // Case 1
	} else {
		color_case2(node);
	}
}

void color_case2(node_t *node) {
	if (node->parent->color == BLACK)
		return; // Case 2.
	else {
		color_case3(node);
	}
}

void color_case3(node_t *node) {
	node_t *p = node->parent;
	node_t *u = uncle(node);
	if (p != NULL && p->color == RED && u != NULL && u->color == RED) {
		p->color = BLACK;
		u->color = BLACK;

		node_t *g = p->parent; // Safe.
		g->color = RED;

		color_case1(g);
	} else {
		color_case4(node);
	}
}


void left_rotate(node_t *node) {
	node_t *p = node->parent;
	if (p->left == node) {
		p->left = node->right;
	}
}

void color_case4(node_t *node) {
	node_t *p = node->parent;
	node_t *u = uncle(node);


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
		new_node->parent = tree;
	}

	color_case1(new_node);

	return tree;
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
int render_tree(FILE *file, node_t *tree, int nodeNbr, int parentNbr) {
	if (tree == NULL)
		return nodeNbr;
	int current = nodeNbr;
	fprintf(file,"  Node%d [label=\"%d\", style=filled, color=Black, fillcolor=%s, fontcolor=Black]\n", current, tree->value, color_str(tree->color));

	int left = nodeNbr + 1;
	int right = render_tree(file, tree->left, left, current);
	int ret = render_tree(file, tree->right, right, current);

	if (tree->left != NULL)
		fprintf(file, "  Node%d->Node%d\n", current, left);
	if (tree->right != NULL)
		fprintf(file, "  Node%d->Node%d\n", current, right);
	if (tree->parent != NULL && parentNbr != -1)
		fprintf(file, "  Node%d->Node%d\n", current, parentNbr);

	return ret;
}

void render(node_t *tree, const char* filename) {
	FILE *file = fopen(filename,"w");
	fprintf(file,"digraph mygraph {\n");

	render_tree(file, tree, 0, -1);

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