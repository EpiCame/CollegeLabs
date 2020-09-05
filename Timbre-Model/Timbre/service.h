#pragma once
#include "repo.h"
#include "validator.h"

class service {

private:
	repo& rep;
	validator& valid;

public:
	service(repo& rep, validator& valid) : rep{ rep }, valid{ valid }{
		
	};

	service(const service& ot) = delete;

	vector<timbru>& get_all() {
		return this->rep.get_all();
	};

	void clear_timbre() {
		this->rep.clear_repo();
	}

	void add(int id, string nume, int an, string tara, int pret);

	


};
