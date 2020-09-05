#pragma once
#include <string>

using namespace std;

class timbru {

private:
	int id;
	string nume;
	int an;
	string tara;
	int pret;


public:

	timbru(int id, string nume, int an, string tara, int pret) : id{ id }, nume{ nume }, an{ an }, tara{ tara }, pret{ pret }{
	};

	timbru(const timbru& ot) : id{ ot.get_id() }, nume{ ot.get_nume() }, an{ ot.get_an() }, tara{ ot.get_tara() }, pret{ ot.get_pret() }{};


	bool operator==(const timbru& ot) const {
		return this->id == ot.get_id();
	};

	int get_id() const { return this->id; };

	string get_nume() const { return this->nume; };

	int get_an() const { return this->an; };

	int get_pret() const { return this->pret; };

	string get_tara() const { return this->tara; };

	string to_str() const {

		return to_string(this->id) + ',' + this->nume + ',' + to_string(this->an) + ',' + tara + ',' + to_string(this->pret);
	}


};
