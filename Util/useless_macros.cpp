
// SQL's IF, i just found it really funny
template <typename T>
inline T IF(bool condition, T val, T elseval)
{
	return condition ? val : elseval;
}

// https://stackoverflow.com/questions/2745074/fast-ceiling-of-an-integer-division-in-c-c
#define DIVCEIL(x, y) IF(x == 0, 0, 1 + ((x - 1) / y)

