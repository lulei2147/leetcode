#include<stdio.h>

// 树的结点
typedef struct node{
    int data;
    struct node *left;
    struct node *right;
}Node;

// 树根
typedef struct{
    Node *root;
}Tree;

// 创建树 -- 插入数据
void insert(Tree *tree, int value)
{
    Node *node = (Node *)malloc(sizeof(Node));
    node->data = value;
    node->left = NULL;
    node->right = NULL;

    if(tree->root == NULL)
    {
        tree->root = node;
    }
    else
    {
        Node *temp = tree->root;

        while(temp != NULL)
        {
            if(value < temp->data)
            {
                if(temp->left == NULL)
                {
                    temp->left = node;
                    return;
                }
                else
                {
                    temp = temp->left;
                }
            }
            else
            {
                if(temp->right == NULL)
                {
                    temp->right = node;
                    return;
                }
                else
                {
                    temp = temp->right;
                }
            }
        }
    }
    return;
}

// 树的中序遍历
void inorder(Node *node)
{
    if(node != NULL)
    {
        inorder(node->left);
        printf("%d ", node->data);
        inorder(node->right);
    }
}

int main(void)
{
    Tree tree;

    tree.root = NULL;
    int n;

    return 0;
}