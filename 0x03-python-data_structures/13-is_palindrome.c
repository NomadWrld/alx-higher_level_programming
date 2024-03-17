#include "lists.h"

/**
 * reverse_list - Reverses a linked list.
 * @head: A pointer to the head of the linked list.
 *
 * Return: A pointer to the head of the reversed linked list.
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *next;

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	return (prev);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: A pointer to a pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *mid = NULL, *second_half = NULL;
	listint_t *prev_slow = *head, *temp_head = *head;
	int result = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			mid = slow;
			slow = slow->next;
		}

		second_half = slow;
		prev_slow->next = NULL;
		second_half = reverse_list(&second_half);
		result = compare_lists(temp_head, second_half);
	}
	return (result);
}
