#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints Python list information
 * @p: Python object (list)
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	size = PyList_Size(p);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints Python bytes information
 * @p: Python object (bytes)
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("  size: %ld\n", size);

	str = PyBytes_AsString(p);
	printf("  trying string: %s\n", str);

	printf("  first %ld bytes: ", (size < 10 ? size + 1 : 10));

	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx%s", str[i], (i == size - 1 || i == 9 ? "\n" : " "));
	}
}

/**
 * print_python_float - Prints Python float information
 * @p: Python object (float)
 */
void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	printf("  value: %lf\n", PyFloat_AsDouble(p));
}

