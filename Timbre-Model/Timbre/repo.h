#pragma once
#include "model.h"
#include <vector>
#include <fstream>
#include <exception>


class repo {

private:
	vector<timbru> rep;
	string file_name;

	void load_from_file();
	void write_to_file();

public:
	repo(string file_name) :file_name{ file_name } {
		load_from_file();
	};
	repo(const repo& ot) = delete;

	void add(const timbru& tmb);

	void del(const timbru& tmb);

	vector<timbru>& get_all() {
		return this->rep;
	};

	void clear_repo() {
		this->rep.clear();
		write_to_file();
	}

};

class repo_exception : public exception {
private: 
	string msg;
public :

	repo_exception(string msg) : msg{ msg } {};

	string get_msg() { return this->msg; };
};