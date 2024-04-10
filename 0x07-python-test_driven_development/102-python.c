#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Print information about a Python string object
 * @p: Pointer to a PyObject representing a Python string
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	Py_UCS1 *str;

	printf("[.] string object info\n");

	// Check if the object is a string
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	// Get string length
	length = PyUnicode_GET_LENGTH(p);

	// Get string value
	str = PyUnicode_AsUTF8AndSize(p, &length);

	// Determine string type
	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		printf("  type: compact ascii\n");
	}
	else if (PyUnicode_IS_COMPACT(p))
	{
		printf("  type: compact unicode object\n");
	}
	else
	{
		printf("  type: unicode object\n");
	}

	// Print string length and value
	printf("  length: %zd\n", length);
	printf("  value: %s\n", str);
}
