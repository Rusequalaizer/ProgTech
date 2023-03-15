extern "C" __declspec(dllexport) int euler(int a) {
	/*
	 * This library provides 
	 * the user to find the 
	 * value of the Euler 
	 * function.
	 */

	int resultException = 1;

	if (a == 1) {
		return resultException;
	}
	else if (a <= 0) {
		return (resultException - 1);
	}
	else {
		int result = a;
		for (int i = 2; i * i <= a; ++i)
			if (a % i == 0) {
				while (a % i == 0)
					a /= i;
				result -= result / i;
			}
		if (a > 1)
			result -= result / a;
		return result;
	}
}