#pragma once
#include "model.h"


class validator {

public:
	validator() = default;

	void validate_tibru(const timbru& tb);
};


class valid_exception : public exception {
private:
	string msg;
public:

	valid_exception(string msg) : msg{ msg } {};

	string get_msg() { return this->msg; };
};
